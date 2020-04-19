import json
import pandas as pd
import os
import shutil
import datetime

DATA_DIR = "./data/"
DUMP_FILE = os.path.join(DATA_DIR, "hotplace.pkl")

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

    """ dataframes 이어붙이기 """
    location_frame =pd.concat([location_frame_cultural])

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

    print("[핫플레이스 스코어]")
    print(f"{separater}\n")
    print(data["location"])
    print(f"\n{separater}\n\n")

if __name__ == "__main__":
    main()
