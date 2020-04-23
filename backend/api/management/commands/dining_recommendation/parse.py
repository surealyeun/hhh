import json
import pandas as pd
import os
import shutil
import datetime
from sklearn.metrics.pairwise import cosine_similarity

DATA_DIR = "./data/"
DATA_FILE = os.path.join(DATA_DIR, "dining.json")
DUMP_FILE = os.path.join(DATA_DIR, "dining.pkl")

def import_data(data_path=DATA_FILE):
    
    data = load_dataframes()
    df_review = data["reviews"]
    df_store = data["stores"]
    
    df = pd.merge(df_review, df_store, left_on='store', right_on='id', how='outer')
    df.drop(['content', 'reg_time', 'latitude', 'longitude', 'tel'], axis='columns', inplace=True)
        
    store_user_rating = df.pivot_table('score', index = 'id_y', columns='user')
    store_user_rating.fillna(0, inplace=True)

    item_based_collabor = cosine_similarity(store_user_rating)

    item_based_collabor = pd.DataFrame(data = item_based_collabor, index=store_user_rating.index, columns=store_user_rating.index)
    print(item_based_collabor)

    def get_item_based_collabor(title):
        return item_based_collabor[title].sort_values(ascending=False)
    
    print(get_item_based_collabor(360348))

    #return {"stores": store_frame}


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
