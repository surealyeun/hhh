import itertools
from collections import Counter
from parse import load_dataframes
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import folium
from folium import plugins

def set_config():
    # 폰트, 그래프 색상 설정
    font_list = fm.findSystemFonts(fontpaths=None, fontext="ttf")
    if any(["notosanscjk" in font.lower() for font in font_list]):
        plt.rcParams["font.family"] = "Noto Sans CJK JP"
    else:
        if not any(["malgun" in font.lower() for font in font_list]):
            raise Exception(
                "Font missing, please install Noto Sans CJK or Malgun Gothic. If you're using ubuntu, try `sudo apt install fonts-noto-cjk`"
            )

        plt.rcParams["font.family"] = "Malgun Gothic"

    sns.set_palette(sns.color_palette("Spectral"))
    plt.rc("xtick", labelsize=6)


def show_stores_distribution_graph(dataframes):
    """
    Req. 1-3-5 각 음식점의 위치 분포를 지도에 나타냅니다.
    """
    m = folium.Map(
        location=[37.503309,126.7636763],
        zoom_start=13
    )
    
    # 부천의 레스토랑 검색
    stores = dataframes["stores"]
    restaurant = stores["category"].str.contains("레스토랑")
    restaurant = stores.loc[restaurant[restaurant].index]
    buchon = restaurant["address"].str.contains("부천")
    buchon = buchon.fillna(False)
    buchon_restaurant = restaurant[buchon].set_index("id")
    
    buchon_res_loc = buchon_restaurant[["latitude", "longitude", "store_name"]]

    for i in range(0, len(buchon_res_loc)):
        folium.Marker([buchon_res_loc.iloc[i]["latitude"],
                    buchon_res_loc.iloc[i]["longitude"]],
                    popup=buchon_res_loc.iloc[i]['store_name']
        ).add_to(m)
    m.save('map.html')


def main():
    set_config()
    data = load_dataframes()
    show_stores_distribution_graph(data)

if __name__ == "__main__":
    main()
