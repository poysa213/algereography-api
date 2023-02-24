from typing import Any, Optional
import json
from django.core.management.base import BaseCommand
from algereography.models import Wilaya

class Command(BaseCommand):
    help = "Load algeria wilaya and daira data to the db"
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        with open('algereography/data/wilaya.json', 'r') as f:
            data = json.load(f)
            

        for item in data:
            wilaya = Wilaya(ar_name=item['ar_name'], name=item['name'],)
            wilaya.save()
            
        self.stdout.write(self.style.SUCCESS(('All wilayas successfully loaded')))