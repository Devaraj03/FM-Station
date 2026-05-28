import csv
from django.core.management.base import BaseCommand
from fm_app.models import Station

class Command(BaseCommand):
    help = "Import radio stations from CSV"

    def handle(self, *args, **kwargs):
        with open('stations_100.csv', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Station.objects.get_or_create(
                    name=row['name'],
                    country=row['country'],
                    latitude=float(row['latitude']),
                    longitude=float(row['longitude']),
                    stream_url=row['stream_url']
                )
        self.stdout.write(self.style.SUCCESS("Stations imported successfully"))
