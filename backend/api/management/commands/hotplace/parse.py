import json
import pandas as pd
import os
import shutil
import datetime

DATA_DIR = "./data/"
DUMP_FILE = os.path.join(DATA_DIR, "hot_place.pkl")

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
        1)
        인구수 평가 (15~35살까지)
        주말 평일비교 : 30점 만점 
        6개월 전 현재 비교 : 18점 만점
        기저 생활인구 랭킹 : 20점 만점
    """

    """
        1-1) Data 3월 14일 (토요일), 3월 16일 (월요일) 비교
            랭크세워서 30점만점
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
    
    result_frame_base = pop_frame_200314.sort_values(by=['total'], ascending=False)
    result_frame_base = result_frame_base.reset_index()
    result_frame_base['score'] = 20 - ((result_frame_base.index +1))/25 * 20

    result_frame_week = (pop_frame_200314-pop_frame_200316).sort_values(by=['total'], ascending=False)
    result_frame_week = result_frame_week.reset_index()
    result_frame_week['score'] = 30 - ((result_frame_week.index +1))/25 * 30
    
    """
        1-2) 6개월전과 현재 비교 (주말)
    """
    
    file_dir = os.path.join(DATA_DIR, "LOCAL_PEOPLE_DONG_201909.csv")
    people_frame_1909 = pd.read_csv(file_dir)

    people_frame_1909.rename(columns={'기준일ID':'date', 
        '시간대구분':'time', '행정동코드':'dong_code', '총생활인구수':'population',
        '남자15세부터19세생활인구수': 'man_15_19', '남자20세부터24세생활인구수': 'man_20_24',
        '남자25세부터29세생활인구수':'man_25_29', '남자30세부터34세생활인구수':'man_30_34',
        '여자15세부터19세생활인구수': 'woman_15_19', '여자20세부터24세생활인구수': 'woman_20_24',
        '여자25세부터29세생활인구수':'woman_25_29', '여자30세부터34세생활인구수':'woman_30_34',
        }, inplace=True)
    population_frame_1909 = pd.merge(
        dong_code_frame, people_frame_1909, on="dong_code"
    )
    

    
    pop_frame_190922 = population_frame_1909[population_frame_1909['date'] == 20190922]

    pop_frame_190922 = pop_frame_190922[(pop_frame_190922['time'] >10) & (pop_frame_190922['time'] <= 23)]
    pop_frame_190922 = pop_frame_190922.groupby(pop_frame_190922['gu']).sum()
    pop_frame_190922['total'] = (pop_frame_190922['man_15_19'] + pop_frame_190922['man_20_24'] + 
        pop_frame_190922['man_30_34'] + pop_frame_190922['woman_15_19'] + pop_frame_190922['woman_20_24'] + 
        pop_frame_190922['woman_30_34'] + pop_frame_190922['man_25_29'] + pop_frame_190922['woman_25_29']) / 10000
    pop_frame_190922.drop(['time', 'dong_code', 'date', 'man_15_19', 'man_20_24', 'man_25_29', 'population',
        'man_30_34', 'woman_15_19', 'woman_20_24', 'woman_25_29', 'woman_30_34'], axis='columns', inplace=True)

    result_frame_term = (pop_frame_200314-pop_frame_190922).sort_values(by=['total'], ascending=False)
    result_frame_term = result_frame_term.reset_index()
    result_frame_term['score'] = 18 - ((result_frame_term.index +1))/25 *18
  
    
    """ 인구 스코어 합산 """
    
    result_frame_population = (result_frame_week.set_index('gu')+result_frame_term.set_index('gu')+result_frame_base.set_index('gu')).sort_values(by=['score'], ascending=False).reset_index()
    result_frame_population.drop('total', axis='columns', inplace=True)
    
    
    
    
    """ 
        카드사 데이터
        2) 매출액 평가
        19년도 서울 카드사 데이터
        9월, 12월 차이 
        
        기준 : 매출 발생 지역
               구 단위로 묶어서 계산
        
        2-1) 주말과 평일 차이 30점
        2-2) 9월대비 12월 현황 차이 18점

    """

    file_dir = os.path.join(DATA_DIR, "2019-09_22.csv")
    payment_frame_190921 = pd.read_csv(file_dir)
    payment_frame_190921 = payment_frame_190921[payment_frame_190921['매출년월일']==190921]
    payment_frame_190923 = pd.read_csv(file_dir)
    payment_frame_190923 = payment_frame_190923[payment_frame_190923['매출년월일']==190923]

    for i in range(23, 48):
        file_dir = os.path.join(DATA_DIR, "2019-09_"+str(i)+".csv")
        payment_frame_1909 = pd.read_csv(file_dir)
        condition = (
            (payment_frame_1909['가맹점_시도명'] == '서울') &
            # 연령 10대~30대까지
            ((payment_frame_1909['연령'] == '2.20대') | 
             (payment_frame_1909['연령'] == '3.30대') | 
             (payment_frame_1909['연령'] == '1.10대')) &
                # 결제 분류 (의생활, 식생활, 유흥(노래방), 여행, 운송수단(택시), 레포츠/문화/취미, 미용)
                #  의생활 (기타의류, 악세서리, 가방, 안경, 일반신발, 기타 신변잡화)
            (   
                (payment_frame_1909['가맹점업종코드'] == 1099) |
                (payment_frame_1909['가맹점업종코드'] == 1201) |
                (payment_frame_1909['가맹점업종코드'] == 1203) |
                (payment_frame_1909['가맹점업종코드'] == 1204) |
                (payment_frame_1909['가맹점업종코드'] == 1205) |
                (payment_frame_1909['가맹점업종코드'] == 1207) |
                (payment_frame_1909['가맹점업종코드'] == 1299) |
                # 식생활 (출장뷔페, 인삼, 건강식품, 정육점, 미곡상, 주류전문판매, 농수축산, 기타 식품을 제외한 모든식품)
                ((payment_frame_1909['가맹점업종코드'] > 2000) &
                (payment_frame_1909['가맹점업종코드'] < 2199)) |
                # 쇼핑센터 및 편의점
                (payment_frame_1909['가맹점업종코드'] == 4001) |
                (payment_frame_1909['가맹점업종코드'] == 4107) |
                (payment_frame_1909['가맹점업종코드'] == 4123) |
                (payment_frame_1909['가맹점업종코드'] == 4112) |
                # 숙박
                (payment_frame_1909['가맹점업종코드'] == 5001) |
                (payment_frame_1909['가맹점업종코드'] == 5101) |
                (payment_frame_1909['가맹점업종코드'] == 5102) |
                (payment_frame_1909['가맹점업종코드'] == 5103) |
                # 택시
                (payment_frame_1909['가맹점업종코드'] == 5306) |
                # 레포츠 / 문화 / 취미
                ((payment_frame_1909['가맹점업종코드'] > 6000) &
                (payment_frame_1909['가맹점업종코드'] < 7000)) |
                # 미용
                ((payment_frame_1909['가맹점업종코드'] > 7100) &
                (payment_frame_1909['가맹점업종코드'] <= 7106))
            ) &
            # 평상시에 사용하는 금액중 1회 결제금액으로 치기에 너무 높은 금액은 제외
            ((payment_frame_1909['결제금액'] / payment_frame_1909['결제건수']) <= 300000) &
            # 노는 시간이라고 생각되지 않는 시간은 제외
            (payment_frame_1909['승인시간대1'] > 9)
        )
        payment_frame_1909 = payment_frame_1909[condition]
        payment_frame_1909_21 = payment_frame_1909[payment_frame_1909['매출년월일']==190921]
        payment_frame_190921 = pd.concat([payment_frame_190921, payment_frame_1909_21])
        payment_frame_1909_23 = payment_frame_1909[payment_frame_1909['매출년월일']==190923]
        payment_frame_190923 = pd.concat([payment_frame_190923, payment_frame_1909_23])
    

    payment_frame_190921.drop(['회원_시도명', '회원_시군구명', '개인기업구분', '성별', '가맹점업종코드',
        '연령', '매출년월일', '승인시간대1', '가맹점_시도명', '가맹점_읍면동명', '결제건수', '회원수'], axis='columns', inplace=True)
    
    payment_frame_190923.drop(['회원_시도명', '회원_시군구명', '개인기업구분', '성별', '가맹점업종코드',
        '연령', '매출년월일', '승인시간대1', '가맹점_시도명', '가맹점_읍면동명', '결제건수', '회원수'], axis='columns', inplace=True)
    
    payment_frame_190921.rename(columns={'가맹점_시군구명':'gu'}, inplace=True)
    payment_frame_190923.rename(columns={'가맹점_시군구명':'gu'}, inplace=True)
    payment_frame_190921 = payment_frame_190921.groupby(payment_frame_190921['gu']).sum()
    payment_frame_190923 = payment_frame_190923.groupby(payment_frame_190923['gu']).sum()


    result_frame_week = (payment_frame_190921-payment_frame_190923).sort_values(by=['결제금액'], ascending=False).reset_index()
    result_frame_week['score'] = 30 - ((result_frame_week.index +1))/25 * 30
    result_frame_week.drop('결제금액', axis='columns', inplace=True)


    """ 9월과 12월 비교 """

    
    file_dir = os.path.join(DATA_DIR, "2019-12_22.csv")
    payment_frame_191221 = pd.read_csv(file_dir)
    payment_frame_191221 = payment_frame_191221[payment_frame_191221['가맹점_시도명'] == '서울']
    payment_frame_191221 = payment_frame_191221[payment_frame_191221['매출년월일']==191221]

    for i in range(23, 48):
        file_dir = os.path.join(DATA_DIR, "2019-09_"+str(i)+".csv")
        payment_frame_1912 = pd.read_csv(file_dir)
        condition = (
            (payment_frame_1912['가맹점_시도명'] == '서울') &
            # 연령 10대~30대까지
            ((payment_frame_1912['연령'] == '2.20대') | 
             (payment_frame_1912['연령'] == '3.30대') | 
             (payment_frame_1912['연령'] == '1.10대')) &
                # 결제 분류 (의생활, 식생활, 유흥(노래방), 여행, 운송수단(택시), 레포츠/문화/취미, 미용)
                #  의생활 (기타의류, 악세서리, 가방, 안경, 일반신발, 기타 신변잡화)
            (   
                (payment_frame_1912['가맹점업종코드'] == 1099) |
                (payment_frame_1912['가맹점업종코드'] == 1201) |
                (payment_frame_1912['가맹점업종코드'] == 1203) |
                (payment_frame_1912['가맹점업종코드'] == 1204) |
                (payment_frame_1912['가맹점업종코드'] == 1205) |
                (payment_frame_1912['가맹점업종코드'] == 1207) |
                (payment_frame_1912['가맹점업종코드'] == 1299) |
                # 식생활 (출장뷔페, 인삼, 건강식품, 정육점, 미곡상, 주류전문판매, 농수축산, 기타 식품을 제외한 모든식품)
                ((payment_frame_1912['가맹점업종코드'] > 2000) &
                (payment_frame_1912['가맹점업종코드'] < 2199)) |
                # 쇼핑센터 및 편의점
                (payment_frame_1912['가맹점업종코드'] == 4001) |
                (payment_frame_1912['가맹점업종코드'] == 4107) |
                (payment_frame_1912['가맹점업종코드'] == 4123) |
                (payment_frame_1912['가맹점업종코드'] == 4112) |
                # 숙박
                (payment_frame_1912['가맹점업종코드'] == 5001) |
                (payment_frame_1912['가맹점업종코드'] == 5101) |
                (payment_frame_1912['가맹점업종코드'] == 5102) |
                (payment_frame_1912['가맹점업종코드'] == 5103) |
                # 택시
                (payment_frame_1912['가맹점업종코드'] == 5306) |
                # 레포츠 / 문화 / 취미
                ((payment_frame_1912['가맹점업종코드'] > 6000) &
                (payment_frame_1912['가맹점업종코드'] < 7000)) |
                # 미용
                ((payment_frame_1912['가맹점업종코드'] > 7100) &
                (payment_frame_1912['가맹점업종코드'] <= 7106))
            ) &
            # 평상시에 사용하는 금액중 1회 결제금액으로 치기에 너무 높은 금액은 제외
            ((payment_frame_1912['결제금액'] / payment_frame_1912['결제건수']) <= 300000) &
            # 노는 시간이라고 생각되지 않는 시간은 제외
            (payment_frame_1912['승인시간대1'] > 9)
        )
        payment_frame_1912 = payment_frame_1912[condition]
        payment_frame_1912_21 = payment_frame_1912[payment_frame_1912['매출년월일']==191221]
        payment_frame_191221 = pd.concat([payment_frame_191221, payment_frame_1912_21])


    
    
    payment_frame_191221.drop(['회원_시도명', '회원_시군구명', '개인기업구분', '성별', '가맹점업종코드',
        '연령', '매출년월일', '승인시간대1', '가맹점_시도명', '가맹점_읍면동명', '결제건수', '회원수'], axis='columns', inplace=True)
    
    payment_frame_191221.rename(columns={'가맹점_시군구명':'gu'}, inplace=True)
    payment_frame_191221 = payment_frame_191221.groupby(payment_frame_191221['gu']).sum()


    result_frame_term = (payment_frame_191221-payment_frame_190921).sort_values(by=['결제금액'], ascending=False).reset_index()
    result_frame_term['score'] = 18 - ((result_frame_term.index +1))/25 * 18
    result_frame_term.drop('결제금액', axis='columns', inplace=True)

    result_frame_payment = (result_frame_week.set_index('gu')+result_frame_term.set_index('gu')).sort_values(by=['score'], ascending=False).reset_index()

    result = (result_frame_population.set_index('gu')+result_frame_payment.set_index('gu')).sort_values(by=['score'], ascending=False).reset_index()
    
    
    return {"hotplace_result": result}

def dump_dataframes(dataframes):
    pd.to_pickle(dataframes, DUMP_FILE)


def load_dataframes():
    return pd.read_pickle(DUMP_FILE)

def main():

    print("[*] Parsing data...")
    data = import_data()
    print("[+] Done\n")

    print("[*] Dumping data...")
    dump_dataframes(data)
    print("[+] Done\n")

    data = load_dataframes()

    term_w = shutil.get_terminal_size()[0] - 1
    separater = "-" * term_w

    print("[핫플레이스 스코어]")
    print(f"{separater}\n")
    print(data["hotplace_result"])
    print(f"\n{separater}\n\n")

if __name__ == "__main__":
    main()
