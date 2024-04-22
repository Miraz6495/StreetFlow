import random
from django.core.management.base import BaseCommand
from map.models import Vehicle


class Command(BaseCommand):
    help = 'Generates vehicle objects in the database'

    def handle(self, *args, **options):
        NUM_VEHICLES_TO_GENERATE = 6
        for _ in range(NUM_VEHICLES_TO_GENERATE):
            Vehicle.objects.create(
                latitude=random.uniform(23.7, 23.9),
                longitude=random.uniform(90.3, 90.5)
            )

        print(f"{Vehicle.objects.count()} vehicles now in the database")
