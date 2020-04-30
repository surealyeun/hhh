import json
import pandas as pd
import os
import shutil
import datetime

DATA_DIR = "./data/"
DUMP_FILE = os.path.join(DATA_DIR, "location.pkl")

location_columns = (
    "id",  # 음식점 고유번호
    "location_name",  # 장소 이름
    "address_see",  # 장소 시
    "address_gu",  # 장소 구
    "address_dong",  # 장소 동
    "tel",  # 전화 번호
    "latitude",  # 장소 위도
    "longitude",  # 장소 경도
    "description",  # 장소 정보
)

def import_data():

    """ 서울시 문화공간 """    
    file_dir = os.path.join(DATA_DIR, "CulturalSpaceInformation_Seoul.csv")
    location_frame_cultural = pd.read_csv(file_dir)
    
    location_frame_cultural.rename(columns={'문화시설명':'location_name', 
    '전화번호':'tel', 'X좌표':'latitude', 'Y좌표':'longitude', '주제분류':'description'}, inplace=True)

    address_split = location_frame_cultural["주소"].str.split(n=2, expand=True)
    location_frame_cultural["address_see"] = address_split[0]
    location_frame_cultural["address_gu"] = address_split[1]
    location_frame_cultural["address_dong"] = address_split[2]

    location_frame_cultural.drop(['번호', 'BLUE', 'RED', 'GREEN', 'YELLOW', '주소',
     '대표이미지', '기타사항', '시설소개', '무료구분', '지하철', '팩스번호',
      '홈페이지', '관람시간', '관람료', '휴관일', '개관일자', '객석수', 
      '공항버스', '버스정거장'], axis='columns', inplace=True)
    
    location_frame_cultural = location_frame_cultural[['location_name', 'address_see',
    'address_gu', 'address_dong', 'tel', 'latitude', 'longitude', 'description']]
    
    
    """ 서울시 유적지 """    
    file_dir = os.path.join(DATA_DIR, "HistoricSiteInformation_Seoul.csv")
    location_frame_historic = pd.read_csv(file_dir)


    location_frame_historic.rename(columns={'분류3':'description', '명칭':'location_name', 
    '행정 시':'address_see', '행정 구':'address_gu', '행정 동':'address_dong'}, inplace=True)
    location_frame_historic.drop(['키', '분류1', '분류2', '도로명주소', '주소'], axis='columns', inplace=True)
    location_frame_historic['latitude'] = ''
    location_frame_historic['longitude'] = ''
    location_frame_historic['tel'] = ''
    
    
    location_frame_historic = location_frame_historic[['location_name', 'address_see',
    'address_gu', 'address_dong', 'tel', 'latitude', 'longitude', 'description']]


    """ 서울시 공원 """    
    file_dir = os.path.join(DATA_DIR, "PublicParkInformation_Seoul.csv")
    location_frame_park = pd.read_csv(file_dir)

    location_frame_park.rename(columns={'공원명' :'location_name', '공원개요': 'description',
    '전화번호':'tel', 'X좌표(WGS84)' : 'longitude', 'Y좌표(WGS84)' : 'latitude'}, inplace=True)

    location_frame_park.drop(['공원번호', '면적', '개원일', '주요시설', '주요식물',
    '안내도', '이용시참고사항', '오시는길', '이미지', '지역', '관리부서', 'X좌표(GRS80TM)',
    'Y좌표(GRS80TM)', '바로가기'], axis='columns', inplace=True)

    address_split = location_frame_park["공원주소"].str.split(n=2, expand=True)
    location_frame_park["address_see"] = address_split[0]
    location_frame_park["address_gu"] = address_split[1]
    location_frame_park["address_dong"] = address_split[2]
    
    location_frame_park = location_frame_park[['location_name', 'address_see',
    'address_gu', 'address_dong', 'tel', 'latitude', 'longitude', 'description']]
    

    """ 서울시 골목 데이터 """    
    file_dir = os.path.join(DATA_DIR, "TouristStreetInformation_Seoul.csv")
    location_frame_street = pd.read_csv(file_dir)

    location_frame_street.rename(columns={'alias' :'location_name', '검색 키워드':'description',
    '행정 시': 'address_see', '행정 구': 'address_gu', '행정 동' : 'address_dong',
    '중심 좌표 X':'longitude', '중심 좌표 Y':'latitude'}, inplace=True)

    location_frame_street.drop(['키', '최종 표기명', '법정 시', '법정 구', '법정 동', '지번 주소'], axis='columns', inplace=True)
    location_frame_street['tel'] = ""
    

    location_frame_street = location_frame_street[['location_name', 'address_see',
    'address_gu', 'address_dong', 'tel', 'latitude', 'longitude', 'description']]

    """ dataframes 이어붙이기 """
    location_frame =pd.concat([location_frame_cultural, location_frame_historic,
        location_frame_park, location_frame_street])

    location_frame["longitude"] = location_frame["longitude"].str.replace(' ','') 
    location_frame["latitude"] = location_frame["latitude"].str.replace(' ','') 

    location_frame.sort_values(by=['location_name'], inplace=True)
    print(location_frame)
    return {"location": location_frame}


def dump_dataframes(dataframes):
    pd.to_pickle(dataframes, DUMP_FILE)


def load_dataframes():
    return pd.read_pickle(DUMP_FILE)


def main():

    print("[*] Parsing data...")
    data = import_data()
    print("[+] Done")

    print("[*] Dumping data...")
    dump_dataframes(data)
    print("[+] Done\n")

    data = load_dataframes()

    term_w = shutil.get_terminal_size()[0] - 1
    separater = "-" * term_w

    print("[장소 정보]")
    print(f"{separater}\n")
    print(data["location"])
    print(f"\n{separater}\n\n")

if __name__ == "__main__":
    main()
