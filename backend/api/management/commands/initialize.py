from pathlib import Path
import pandas as pd
from django.core.management.base import BaseCommand
from django.conf import settings
from api import models

class Command(BaseCommand):
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
    
    help = "initialize database"

    def _initialize(self):
        
        DATA_DIR = Path(settings.BASE_DIR).parent / "data"

        for i in range(len(gu_list)):
            print("[*] Loading data...")
            dataframes = pd.read_pickle(str(DATA_DIR / "recommend_"+gu_list[gu_eng[i]]+".pkl"))
            
            print("[*] Initializing " + gu_list[gu_eng[i]] +"...")
            
            models.Recommend.objects.all().delete()
            recommend_bulk = [
                models.Recommend(
                    id=store.id,
                    store_name=store.store_name,
                    branch=store.branch,
                    area=store.area
                )
                for recommend in dataframes.itertuples()
            ]
        
        models.Recommend.objects.bulk_create(recommend_bulk)
        

        # print("[*] Initializing stores...")
        # models.DiningStore.objects.all().delete()
        # stores = dataframes["stores"]
        # stores_bulk = [
        #     models.DiningStore(
        #         id=store.id,
        #         store_name=store.store_name,
        #         branch=store.branch,
        #         area=store.area,
        #         tel=store.tel,
        #         address_see=store.address_see,
        #         address_gu=store.address_gu,
        #         address_dong=store.address_dong,
        #         latitude=store.latitude,
        #         longitude=store.longitude,
        #         category=store.category,
        #     )
        #     for store in stores.itertuples()
        # ]
        
        # models.DiningStore.objects.bulk_create(stores_bulk)
        
        # print("[*] Initializing reviews...")
        # models.DiningReview.objects.all().delete()
        # reviews = dataframes["reviews"]
        # reviews_bulk = [
        #     models.DiningReview(
        #         review_id=review.id,
        #         store_id=review.store,
        #         dining_user=review.user,
        #         score=review.score,
        #         content=review.content,
        #         reg_time=review.reg_time,
        #     )
        #     for review in reviews.itertuples()
        # ]
        # models.DiningReview.objects.bulk_create(reviews_bulk)


        # print("[*] Loading data...")
        # dataframes = pd.read_pickle(str(DATA_DIR / "location.pkl"))
        
        # print("[*] Initializing locations...")
        # models.Location.objects.all().delete()
        # locations = dataframes["location"]
        # locations_bulk = [
        #     models.Location(
        #         location_name=location.location_name,
        #         address_see = location.address_see,
        #         address_gu = location.address_gu,
        #         address_dong = location.address_dong,
        #         tel = location.tel,
        #         latitude = location.latitude,
        #         longitude = location.longitude,
        #         description = location.description
                
        #     )
        #     for location in locations.itertuples()
        # ]
        # models.Location.objects.bulk_create(locations_bulk)

        print("[+] Done")

    def handle(self, *args, **kwargs):
        self._initialize()
