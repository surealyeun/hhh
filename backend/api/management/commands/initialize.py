from pathlib import Path
import pandas as pd
from django.core.management.base import BaseCommand
from django.conf import settings
from api import models

class Command(BaseCommand):
    help = "initialize database"

    def _initialize(self):
        """
        Sub PJT 1에서 만든 Dataframe을 이용하여 DB를 초기화합니다.
        """
        print("[*] Loading data...")
        DATA_DIR = Path(settings.BASE_DIR).parent / "data"
        dataframes = pd.read_pickle(str(DATA_DIR / "dining.pkl"))

        print("[*] Initializing stores...")
        models.DiningStore.objects.all().delete()
        stores = dataframes["stores"]
        stores_bulk = [
            models.DiningStore(
                id=store.id,
                store_name=store.store_name,
                branch=store.branch,
                area=store.area,
                tel=store.tel,
                address_see=store.address_see,
                address_gu=store.address_gu,
                address_dong=store.address_dong,
                latitude=store.latitude,
                longitude=store.longitude,
                category=store.category,
            )
            for store in stores.itertuples()
        ]
        
        #models.DiningStore.objects.bulk_create(stores_bulk)
        
        print("[*] Loading data...")
        dataframes = pd.read_pickle(str(DATA_DIR / "location.pkl"))
        
        print("[*] Initializing locations...")
        models.Location.objects.all().delete()
        locations = dataframes["location"]
        locations_bulk = [
            models.Location(
                location_name=location.location_name,
                address_see = location.address_see,
                address_gu = location.address_gu,
                address_dong = location.address_dong,
                tel = location.tel,
                latitude = location.latitude,
                longitude = location.longitude,
                description = location.description
                
            )
            for location in locations.itertuples()
        ]
        #models.Location.objects.bulk_create(locations_bulk)

        print("[+] Done")

    def handle(self, *args, **kwargs):
        self._initialize()
