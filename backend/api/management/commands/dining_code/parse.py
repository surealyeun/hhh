import json
import pandas as pd
import os
import shutil
import datetime

DATA_DIR = "./data/"
DATA_FILE = os.path.join(DATA_DIR, "dining.json")
DUMP_FILE = os.path.join(DATA_DIR, "dining.pkl")

store_columns = (
    "id",  # 음식점 고유번호
    "store_name",  # 음식점 이름
    "branch",  # 음식점 지점 여부
    "area",  # 음식점 위치
    "tel",  # 음식점 번호
    "address",  # 음식점 주소
    "latitude",  # 음식점 위도
    "longitude",  # 음식점 경도
    "category",  # 음식점 카테고리
)

review_columns = (
    "id",  # 리뷰 고유번호
    "store",  # 음식점 고유번호
    "user",  # 유저 고유번호
    "score",  # 평점
    "content",  # 리뷰 내용
    "reg_time",  # 리뷰 등록 시간
)

user_columns = (
    "user",     # 유저 아이디
    "user_gen", # 유저 성별 
    "user_age"  # 유저 나이
)

bhour_columns = (
    "store", # 음식점 고유번호
    "type",  # 영업시간 종류  / 1-영업시간, 2-쉬는시간, 3-휴무일
    "week_type",  # 주단위 종류 / 1-매주, 2-첫째 주, 3-둘째 주 , 4-셋째 주, 5-넷째 주, 6-공휴일
    "mon",  #  월요일 포함 유무  / 1-포함, 0-미포함
    "tue",  #  화요일 포함 유무  / 1-포함, 0-미포함
    "wed",  #  수요일 포함 유무  / 1-포함, 0-미포함
    "thu",  #  목요일 포함 유무  / 1-포함, 0-미포함
    "fri",  #  금요일 포함 유무  / 1-포함, 0-미포함
    "sat",  #  토요일 포함 유무  / 1-포함, 0-미포함
    "sun",  #  일요일 포함 유무  / 1-포함, 0-미포함
    "start_time", # 시작 시간
    "end_time", # 종료 시간
    "etc", # 기타
)

menu_columns = (
    "menu_id",  # 메뉴 아이디
    "store",    # 가게 이름
    "menu_name",# 메뉴 이름
    "price"     # 메뉴 가격
)

def import_data(data_path=DATA_FILE):
    """
    Req. 1-1-1 음식점 데이터 파일을 읽어서 Pandas DataFrame 형태로 저장합니다
    """

    try:
        with open(data_path, encoding="utf-8") as f:
            data = json.loads(f.read())
    except FileNotFoundError as e:
        print(f"`{data_path}` 가 존재하지 않습니다.")
        exit(1)

    stores = []  # 음식점 테이블
    reviews = []  # 리뷰 테이블
    users = [] # 유저 테이블
    bhours = [] # 운영시간 테이블
    menus = [] # 음식 테이블

    year = datetime.datetime.today().year
    user_set = set()
    menu_id = 1
    for d in data:
        if d["address"] is None: continue
        if '&amp;' in d['name'] : continue
        if "서울특별시" in d["address"] :
            categories = [c["category"] for c in d["category_list"]]
            stores.append(
                [
                    d["id"],
                    d["name"],
                    d["branch"],
                    d["area"],
                    d["tel"],
                    d["address"],
                    d["latitude"],
                    d["longitude"],
                    "|".join(categories)
                ]
            )

            for review in d["review_list"]:
                r = review["review_info"]
                u = review["writer_info"]
                age = (year-int(u["born_year"]))+1 if int(u["born_year"]) > 0  else 0

                reviews.append(
                    [r["id"], d["id"], u["id"], r["score"], r["content"], r["reg_time"]]
                )
                
                if u["id"] not in user_set:
                    users.append([u["id"], u["gender"], age])
                    user_set.add(u["id"])

            for bhour in d["bhour_list"]:
                b = bhour

                bhours.append(
                    [d["id"], b["type"], b["week_type"], b["mon"], b["tue"], b["wed"],
                    b["thu"], b["fri"], b["sat"], b["sun"], b["start_time"], b["end_time"], b["etc"]]
                )

            for menu in d["menu_list"]:
                m = menu

                menus.append(
                    [menu_id, d["id"], m["menu"], m["price"]]
                )
                menu_id += 1


    store_frame = pd.DataFrame(data=stores, columns=store_columns)
    review_frame = pd.DataFrame(data=reviews, columns=review_columns)
    user_frame = pd.DataFrame(data=users, columns=user_columns)
    bhour_frame = pd.DataFrame(data=bhours, columns=bhour_columns)
    menu_frame = pd.DataFrame(data=menus, columns=menu_columns)

    address_split = store_frame["address"].str.split(n=2, expand=True)
    store_frame["address_see"] = address_split[0]
    store_frame["address_gu"] = address_split[1]
    store_frame["address_dong"] = address_split[2]    
    store_frame.drop('address', axis='columns', inplace=True)

    return {"stores": store_frame, "reviews": review_frame, 
        "bhours": bhour_frame, "users": user_frame, "menus": menu_frame}


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

    print("[음식점]")
    print(f"{separater}\n")
    print(data["stores"].head(15))
    print(f"\n{separater}\n\n")

    print("[리뷰]")
    print(f"{separater}\n")
    print(data["reviews"].head())
    print(f"\n{separater}\n\n")

    print("[유저 정보]")
    print(f"{separater}\n")
    print(data["users"].head())
    print(f"\n{separater}\n\n")

    print("[영업 시간]")
    print(f"{separater}\n")
    print(data["bhours"].head())
    print(f"\n{separater}\n\n")

    print("[메뉴 정보]")
    print(f"{separater}\n")
    print(data["menus"].head())
    print(f"\n{separater}\n\n")


if __name__ == "__main__":
    main()
