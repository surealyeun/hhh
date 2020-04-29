import json
import pandas as pd
import numpy as np
import os
import shutil
import datetime
import pymysql
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import TruncatedSVD
from scipy.sparse.linalg import svds

DATA_DIR = "./data/"
DATA_FILE = os.path.join(DATA_DIR, "dining.json")
DUMP_FILE = os.path.join(DATA_DIR, "dining.pkl")

def import_data():
    
    connection = pymysql.connect(
        host='13.125.113.171', user='root', password='ssafya202!@#', db='HHH',
        charset='utf8mb4', autocommit=True, cursorclass=pymysql.cursors.DictCursor
    )

    cursor = connection.cursor()

    sql = "select * from HHH.api_diningstore"
    cursor.execute(sql)
    result = cursor.fetchall()
    df_store = pd.DataFrame(result)

    sql = "select * from HHH.api_location"
    cursor.execute(sql)
    result = cursor.fetchall()
    df_location = pd.DataFrame(result)

    sql = "select * from HHH.places_review"
    cursor.execute(sql)
    result = cursor.fetchall()
    df_review = pd.DataFrame(result)

    connection.close()
    
    df_store.drop([
        'branch', 'area', 'tel', 'address_dong', 'latitude', 'longitude',
        'category', 'address_see'
    ], axis='columns', inplace=True)
    df_location.drop([
        'address_dong', 'latitude', 'longitude', 'tel',
        'description', 'address_see'
    ], axis='columns', inplace=True)

    df_store.rename(columns={'store_name':'name'}, inplace=True)
    df_location.rename(columns={'location_name':'name'}, inplace=True)
    
    location_bound = df_store['id'].max() + 1
    df_location['id'] = df_location['id'] + location_bound

    df = pd.concat([df_store, df_location])
    df_store = pd.concat([df_store, df_location])
    df_review['store_id'] = df_review["store_id"].fillna(0).astype("int")
    df_review['location_id'] = df_review["location_id"].fillna(0).astype("int")
    

    df_review_store = df_review[df_review['store_id'] != 0]
    df_review_store.drop(
        'location_id', axis='columns', inplace=True
    )
    df_review_location = df_review[df_review['location_id'] != 0]
    df_review_location.drop(
        'store_id', axis='columns', inplace=True
    )
    df_review_location['location_id'] = df_review_location['location_id'] + location_bound
    df_review_location.rename(columns={'location_id':'store_id'}, inplace=True)

    df_review = pd.concat([df_review_store, df_review_location])
    df_review.drop('id', axis='columns', inplace=True)
    
    df_review.rename(columns={'store_id':'id'}, inplace=True)

    df = pd.merge(df_review, df, on='id', how='outer')
    df = df.fillna(0)
    
    """
        유저 맞춤 가게 추천
    """
    gu_list = [
        '송파구','동작구','관악구','금천구','영등포구','구로구','양천구','강서구',
        '강남구','서초구','강동구','광진구','중랑구','노원구','성동구','동대문구',
        '성북구','강북구','도봉구','종로구','중구','용산구','마포구','서대문구',
        '은평구'
    ]
    gu_eng = {
        '송파구':'songpa','동작구':'dongjak','관악구':'gwanak','금천구':'geumcheon',
        '영등포구':'yeongdeungpo','구로구':'guro','양천구':'yangcheon','강서구':'gangseo',
        '강남구':'gangnam','서초구':'seocho','강동구':'gangdong','광진구':'gwangjin',
        '중랑구':'jungnang','노원구':'nowon','성동구':'seongdong','동대문구':'dongdaemun',
        '성북구':'seongbuk','강북구':'gangbuk','도봉구':'dobong','종로구':'jongno',
        '중구':'jung','용산구':'yongsan','마포구':'mapo','서대문구':'seodaemun',
        '은평구':'eunpyeong'
    }

    for i in range(len(gu_list)):
        print("---------------------------------------")
        print(gu_list[i])
        print("---------------------------------------")
        df_loc = df[df['address_gu'] == gu_list[i]]
        # gu 기준으로 위에서 정렬해서 넘어 와야함
        df_loc.drop(['name','address_gu'],axis='columns', inplace=True)
        df_loc.rename(columns={'id':'store', 'user_id':'user'}, inplace=True)
        
        df_loc['user'] = df_loc['user'].fillna(0).astype(int)
        df_loc['score'] = df_loc['score'].fillna(0).astype(int)
        df_loc['store'] = df_loc['store'].fillna(0).astype(int)

        user_store_rating = df_loc.pivot_table('score', index='user', columns='store').fillna(0)
        user_num_list = list(user_store_rating.index)
        matrix = user_store_rating.as_matrix()
        user_ratings_mean = np.mean(matrix, axis=1)
        matrix_user_mean = matrix - user_ratings_mean.reshape(-1, 1)
        
        U, sigma, Vt = svds(matrix_user_mean, k = 1)
        sigma = np.diag(sigma)

        svd_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt) + user_ratings_mean.reshape(-1, 1)
        df_svd_preds = pd.DataFrame(svd_user_predicted_ratings, columns=user_store_rating.columns)
        
        rank = []
        for k in range(1,51):
            rank.append(k)
        recommend = []
        data = pd.DataFrame()
        for j in range(len(user_num_list)):
            if j == 0 : continue
            usernumber_index = user_num_list.index(user_num_list[j])
            recommend, predictions = recommend_spot(df_svd_preds, usernumber_index, df_store, df_review, 10, user_num_list)                
            
            isLoc = []
            for k in range(50):
                if recommend[k] > location_bound:
                    recommend[k] -= location_bound
                    isLoc.append(True)
                else:
                    isLoc.append(False)
            
            dict = {'rank': rank, 'recommend':recommend, 'user_id':user_num_list[j], 'isLocation':isLoc}
            print(dict)
            data_user = pd.DataFrame(dict)
            data = pd.concat([data, data_user])
        
        data = data.reset_index(drop=True)
        print(data)
        DUMP_FILE = os.path.join(DATA_DIR, 'recommend_'+gu_eng[gu_list[i]]+'.pkl') 
        dump_dataframes(data, DUMP_FILE)

def recommend_spot(df_svd_preds, user, ori_spot_df, ori_ratings_df, num_recommendations=20, user_list = []):

    user_row_number = user_list[user]
    sorted_user_predictions = df_svd_preds.iloc[user].sort_values(ascending=False)

    user_data = ori_ratings_df[ori_ratings_df.user_id == user_row_number]
    
    user_history = user_data.merge(ori_spot_df, on='id').sort_values(['score'], ascending=False)

    recommendations = ori_spot_df[~ori_spot_df['id'].isin(user_history['id'])]
    recommendations = recommendations.merge(pd.DataFrame(sorted_user_predictions).reset_index(), left_on='id', right_on='store')
    recommendations = recommendations.rename(columns = {(user): 'Predictions'}).sort_values('Predictions')

    return list(recommendations["id"])[:50], recommendations


def dump_dataframes(dataframes, path):
    pd.to_pickle(dataframes, path)


def load_dataframes():
    return pd.read_pickle(DUMP_FILE)


def main():

    print("[*] Parsing data...")
    import_data()
    print("[+] Done")


    term_w = shutil.get_terminal_size()[0] - 1
    separater = "-" * term_w




if __name__ == "__main__":
    main()
