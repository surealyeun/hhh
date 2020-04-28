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

    connection.close()

    print(df_store)
    print(df_location)

    # df = pd.merge(df_review, df_store, left_on='store', right_on='id', how='outer')
    # df.rename(columns={'id_x':'id'}, inplace=True)

    """
        유저 맞춤 가게 추천
    """
    gu_list = [
        '서초구','동작구','관악구','금천구','영등포구','구로구','양천구','강서구',
        '강남구','송파구','강동구','광진구','중랑구','노원구','성동구','동대문구',
        '성북구','강북구','도봉구','종로구','중구','용산구','마포구','서대문구',
        '은평구'
    ]
    # for i in range(1):#len(gu_list)):
    #     address_list = []
    #     df = df[df['address_gu'] == gu_list[i]]

    #     # gu 기준으로 위에서 정렬해서 넘어 와야함
    #     df.drop(['id','branch', 'area', 'category', 'address_see', 'address_gu', 'address_dong'],axis='columns', inplace=True)
    #     df['user'] = df['user'].fillna(0).astype(int)
    #     df['score'] = df['score'].fillna(0).astype(int)
    #     df['store'] = df['store'].fillna(0).astype(int)

    #     user_dining_store_rating = df.pivot_table('score', index='user', columns='store').fillna(0)
    #     user_num_list = list(user_dining_store_rating.index)
        
    #     matrix = user_dining_store_rating.as_matrix()
    #     user_ratings_mean = np.mean(matrix, axis=1)
    #     matrix_user_mean = matrix - user_ratings_mean.reshape(-1, 1)
    #     df = pd.DataFrame(matrix_user_mean, columns=user_dining_store_rating.columns)
    #     U, sigma, Vt = svds(matrix_user_mean, k = 12)
    #     sigma = np.diag(sigma)

    #     svd_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt) + user_ratings_mean.reshape(-1, 1)
    #     df_svd_preds = pd.DataFrame(svd_user_predicted_ratings, columns=user_dining_store_rating.columns)
        
    #     usernumber_index = user_num_list.index(13)
    #     already_rated, predictions = recommend_spot(df_svd_preds, usernumber_index, df_store, df_review, 10, user_num_list)

    #     print(already_rated)
    #     print(predictions)


def recommend_spot(df_svd_preds, user, ori_spot_df, ori_ratings_df, num_recommendations=20, user_list = []):

    user_row_number = user_list[user]
    sorted_user_predictions = df_svd_preds.iloc[user].sort_values(ascending=False)

    user_data = ori_ratings_df[ori_ratings_df.user == user_row_number]
    user_history = user_data.merge(ori_spot_df, on='id').sort_values(['score'], ascending=False)

    recommendations = ori_spot_df[~ori_spot_df['id'].isin(user_history['id'])]
    recommendations = recommendations.merge(pd.DataFrame(sorted_user_predictions).reset_index(), left_on='id', right_on='store')
    recommendations = recommendations.rename(columns = {(user): 'Predictions'}).sort_values('Predictions', ascending=False)

    return user_history, recommendations


def dump_dataframes(dataframes):
    pd.to_pickle(dataframes, DUMP_FILE)


def load_dataframes():
    return pd.read_pickle(DUMP_FILE)


def main():

    print("[*] Parsing data...")
    data = import_data()
    print("[+] Done")

    # print("[*] Dumping data...")
    # dump_dataframes(data)
    # print("[+] Done\n")

    data = load_dataframes()

    term_w = shutil.get_terminal_size()[0] - 1
    separater = "-" * term_w

    print("[리뷰]")
    print(f"{separater}\n")
    #print(data["reviews"].head())
    print(f"\n{separater}\n\n")



if __name__ == "__main__":
    main()
