from parse import load_dataframes
import pandas as pd
import shutil


def sort_stores_by_score(dataframes, n=20, min_reviews=30):
    """
    Req. 1-2-1 각 음식점의 평균 평점을 계산하여 높은 평점의 음식점 순으로 `n`개의 음식점을 정렬하여 리턴합니다
    Req. 1-2-2 리뷰 개수가 `min_reviews` 미만인 음식점은 제외합니다.
    """
    stores_reviews = pd.merge(
        dataframes["stores"], dataframes["reviews"], left_on="id", right_on="store"
    )
    delete_list = stores_reviews["store"].value_counts()
    delete_list = list(delete_list[delete_list < min_reviews].index)

    scores_group = stores_reviews.groupby(["store", "store_name"])
    scores = scores_group.mean()
    scores.drop(delete_list, axis = "index", inplace=True)
    
    return scores.head(n=n).sort_values(by=["score"], ascending=False).reset_index()
 
def get_most_reviewed_stores(dataframes, n=20):
    """
    Req. 1-2-3 가장 많은 리뷰를 받은 `n`개의 음식점을 정렬하여 리턴합니다
    """
    stores_reviews = pd.merge(
        dataframes["stores"], dataframes["reviews"], left_on="id", right_on="store"
    )
    search_condition = stores_reviews.loc[:,'store_name'].value_counts().head(n=n).to_frame().reset_index()
    search_condition.columns = ["store_name","counts"]
    return search_condition


def get_most_active_users(dataframes, n=20):
    """
    Req. 1-2-4 가장 많은 리뷰를 작성한 `n`명의 유저를 정렬하여 리턴합니다.
    """
    reviews = dataframes["reviews"]
    user_info = dataframes["users"].set_index("user")
    user_rank = reviews["user"].value_counts()
    user_list = list(user_rank.head(n=n).index)

    top_reviewer = []
    for user in user_list:
        gender = user_info.loc[user, "user_gen"]
        age = user_info.loc[user, "user_age"]
        top_reviewer.append({"user":user, "gender": gender,
            "age": age, "reviews":user_rank[user]})

    df_top_reviewers = pd.DataFrame(data = top_reviewer)
    
    return df_top_reviewers


def main():
    data = load_dataframes()

    term_w = shutil.get_terminal_size()[0] - 1
    separater = "-" * term_w

    stores_most_scored = sort_stores_by_score(data)
    
    print(f"{separater}\n")
    print("[최고 평점 음식점]\n")
    for i, store in stores_most_scored.iterrows():
        print(
            "{rank}위: {store} ({score}점)".format(
                rank=i + 1, store=store.store_name, score=round(store.score,2)
            )
        )
    print(f"\n{separater}\n\n")


    most_reviewed_stores = get_most_reviewed_stores(data);
    
    print(f"{separater}\n")
    print("[많은 리뷰 음식점]\n")
    for i, store in most_reviewed_stores.iterrows():
        print(
            "{rank}위: {store} ({count} reviews)".format(
                rank=i + 1, store=store.store_name, count=store.counts
            )
        )
    print(f"\n{separater}\n\n")

    most_active_users = get_most_active_users(data)

    print(f"{separater}\n")
    print("[가장 많은 리뷰를 남겨주신 유저]\n")
    for i, user in most_active_users.iterrows():
        print(
            "{rank}위: id: {user}  gender: {gender}  age: {age}  ({reviews} reviews)".format(
                rank=i + 1, user=user.user, gender=user.gender,
                age=user.age, reviews=user.reviews
            )
        )
    print(f"\n{separater}\n\n")
    
if __name__ == "__main__":
    main()
