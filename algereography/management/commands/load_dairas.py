from typing import Any, Optional
import json
from django.core.management.base import BaseCommand
from algereography.models import Wilaya, Daira

class Command(BaseCommand):
    help = "Load algeria wilaya and daira data to the db"
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        with open('algereography/data/daira.json', 'r') as f:
            data = json.load(f)
            

        for item in data:
            wilaya = Wilaya.objects.get(pk=item['wilaya'])
            daira = Daira(ar_name=item['ar_name'], name=item['name'],wilaya=wilaya)
            daira.save()
            
        self.stdout.write(self.style.SUCCESS(('All Dairas successfully loaded')))