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


def show_store_categories_graph(dataframes, n=100):
    """
    Tutorial: 전체 음식점의 상위 `n`개 카테고리 분포를 그래프로 나타냅니다.
    """

    stores = dataframes["stores"]

    # 모든 카테고리를 1차원 리스트에 저장합니다
    categories = stores.category.apply(lambda c: c.split("|"))
    categories = itertools.chain.from_iterable(categories)

    # 카테고리가 없는 경우 / 상위 카테고리를 추출합니다
    categories = filter(lambda c: c != "", categories)
    categories_count = Counter(list(categories))
    best_categories = categories_count.most_common(n=n)
    df = pd.DataFrame(best_categories, columns=["category", "count"]).sort_values(
        by=["count"], ascending=False
    )

    # 그래프로 나타냅니다
    chart = sns.barplot(x="category", y="count", data=df)
    chart.set_xticklabels(chart.get_xticklabels(), rotation=45)
    plt.title("음식점 카테고리 분포")
    plt.show()


def show_store_review_distribution_graph(dataframes):
    """
    Req. 1-3-1 전체 음식점의 리뷰 개수 분포를 그래프로 나타냅니다. 
    """
    # 리뷰가 없는 데이터가 너무 많아
    # 리뷰가 존재하는 데이터들만 간추렸습니다.
    #total_stores_cnt = dataframes["stores"].size    
    #unreviewed_store = total_stores_cnt - reviews.size
    
    stores_reviews = pd.merge(
        dataframes["stores"], dataframes["reviews"], left_on="id", right_on="store"
    )
   
    reviews = stores_reviews["store"].value_counts().to_frame()
    reviews.rename(columns = {"store":"Reviews"}, inplace=True)

    chart = sns.stripplot(data=reviews)
    chart.set_xticklabels(chart.get_xticklabels())
    plt.title("음식점 리뷰 수 분포")
    plt.show() 


def show_store_average_ratings_graph(dataframes):
    """
    Req. 1-3-2 각 음식점의 평균 평점을 그래프로 나타냅니다.
    """
    reviews = dataframes["reviews"]
    store_scores = reviews["score"].groupby(reviews["store"]).mean()

    chart = store_scores.plot(kind="box", y="score")
    plt.title("음식점 평점")
    plt.show()


def show_user_review_distribution_graph(dataframes):
    """
    Req. 1-3-3 전체 유저의 리뷰 개수 분포를 그래프로 나타냅니다.
    """
    reviews = dataframes["reviews"]
    
    user_reviews = reviews["user"].value_counts().to_frame()

    chart = sns.stripplot(y=user_reviews["user"], alpha=0.7)
    chart.set_xticklabels(chart.get_xticklabels())
    plt.title("유저 리뷰수 분포")
    plt.show()


def show_user_age_gender_distribution_graph(dataframes):
    """
    Req. 1-3-4 전체 유저의 성별/나이대 분포를 그래프로 나타냅니다.
    """
    users = dataframes["users"].set_index("user")
    print(users[users["user_age"]>1000])

    sns.catplot(data=users, x="user_gen", y="user_age", kind="strip", hue="user_gen")
    plt.title("유저 성별/ 나이대 분포")
    plt.show()


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
    # show_store_categories_graph(data)
    # show_store_review_distribution_graph(data)
    # show_store_average_ratings_graph(data)
    # show_user_review_distribution_graph(data)
    # show_user_age_gender_distribution_graph(data)
    show_stores_distribution_graph(data)

if __name__ == "__main__":
    main()
