import json
import pandas as pd
import os
import shutil
import datetime

DATA_DIR = "./data/"

keyword_columns = (
    "gu",  # 구 단위
    "rank", # 순위
    "keyword", # 키워드
    "type", # 감성어 타입
)

"""
payment_columns = (
    ""
)

population_columns = (
    "gu",  # 구 단위
    "rank", # 순위
    "keyword", # 키워드
    "type", # 감성어 타입
)
"""

def import_data():
    """
        핫플레이스 평가
        인구수평가 + 매출액 평가
    """
    """
        핫플레이스
        인구수로 평가 (10대~40대)
        주말 평일비교 : 30점 만점 
        1년전 현재 비교 : 18점 만점
    """

    """
        1-1) 주말 평일 비교
    """
    file_dir = os.path.join(DATA_DIR, "dong_code.csv")
    dong_code_frame = pd.read_csv(file_dir)
    file_dir = os.path.join(DATA_DIR, "LOCAL_PEOPLE_DONG_202003.csv")
    people_frame_2003 = pd.read_csv(file_dir)

    dong_code_frame.drop('H_SDNG_CD(통계청행정동코드)', axis='columns', inplace=True)
    dong_code_frame.rename(columns={'H_DNG_CD(행자부행정동코드)':'dong_code',
        'DO_NM(시도명)':'see', 'CT_NM(시군구명)':'gu', 'H_DNG_NM(행정동명)': 'dong'}, inplace=True)
    
    people_frame_2003.rename(columns={'기준일ID':'date', 
        '시간대구분':'time', '행정동코드':'dong_code', '총생활인구수':'population',
        '남자15세부터19세생활인구수': 'man_15_19', '남자20세부터24세생활인구수': 'man_20_24',
        '남자25세부터29세생활인구수':'man_25_29', '남자30세부터34세생활인구수':'man_30_34',
        '여자15세부터19세생활인구수': 'woman_15_19', '여자20세부터24세생활인구수': 'woman_20_24',
        '여자25세부터29세생활인구수':'woman_25_29', '여자30세부터34세생활인구수':'woman_30_34',
        }, inplace=True)

    population_frame_2003 = pd.merge(
        dong_code_frame, people_frame_2003, on="dong_code"
    )
    
    pop_frame_200314 = population_frame_2003[population_frame_2003['date'] == 20200314]
    pop_frame_200316 = population_frame_2003[population_frame_2003['date'] == 20200316]
    
    pop_frame_200314 = pop_frame_200314[(pop_frame_200314['time'] >10) & (pop_frame_200314['time'] <= 23)]
    pop_frame_200314 = pop_frame_200314.groupby(pop_frame_200314['gu']).sum()
    pop_frame_200314['total'] = (pop_frame_200314['man_15_19'] + pop_frame_200314['man_20_24'] + 
        pop_frame_200314['man_30_34'] + pop_frame_200314['woman_15_19'] + pop_frame_200314['woman_20_24'] + 
        pop_frame_200314['woman_30_34'] + pop_frame_200314['man_25_29'] + pop_frame_200314['woman_25_29']) / 10000
    pop_frame_200314.drop(['time', 'dong_code', 'date', 'man_15_19', 'man_20_24', 'man_25_29',
        'man_30_34', 'woman_15_19', 'woman_20_24', 'woman_25_29', 'woman_30_34'], axis='columns', inplace=True)

    pop_frame_200316 = pop_frame_200316[(pop_frame_200316['time'] >10) & (pop_frame_200316['time'] <= 23)]
    pop_frame_200316 = pop_frame_200316.groupby(pop_frame_200316['gu']).sum()
    pop_frame_200316['total'] = (pop_frame_200316['man_15_19'] + pop_frame_200316['man_20_24'] + 
        pop_frame_200316['man_30_34'] + pop_frame_200316['woman_15_19'] + pop_frame_200316['woman_20_24'] + 
        pop_frame_200316['woman_30_34'] + pop_frame_200316['man_25_29'] + pop_frame_200316['woman_25_29']) / 10000
    pop_frame_200316.drop(['time', 'dong_code', 'date', 'man_15_19', 'man_20_24', 'man_25_29',
        'man_30_34', 'woman_15_19', 'woman_20_24', 'woman_25_29', 'woman_30_34'], axis='columns', inplace=True)

    result_frame_population = (pop_frame_200314-pop_frame_200316).sort_values(by=['total'], ascending=False)
    result_frame_population = result_frame_population.reset_index()
    result_frame_population['score'] = 30 - ((result_frame_population.index +1))/25 *30
    print(result_frame_population)

    """
        1-2) 6개월전과 현재 비교 (주말)
    """
    pop_frame_200316


    """ 
        Data 3월 14일 (토요일), 3월 16일 (월요일) 비교
        랭크세워서 30점만점
    """
    
    
    """ dataframes 이어붙이기 """
    #location_frame =pd.concat([location_frame_cultural])

    #return {"location": location_frame}


def main():

    print("[*] Parsing data...")
    data = import_data()
    print("[+] Done\n")

    term_w = shutil.get_terminal_size()[0] - 1
    separater = "-" * term_w

    print("[핫플레이스 스코어]")
    print(f"{separater}\n")
    #print(data["location"])
    print(f"\n{separater}\n\n")

if __name__ == "__main__":
    main()
