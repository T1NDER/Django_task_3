import csv
import os

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    help = 'Import phones data from a CSV file'
    def add_arguments(self, parser):
        parser.add_argument('csv_file', type='str')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        if not os.path.exists('csv_file_path'):
            print(f'Error: File {csv_file_path} not found')
            return

        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone_data in phones:
            phone = Phone(
                name=phone_data['name'],
                price=phone_data['price'],
                image=phone_data['image'],
                release_date=phone_data['release_date'],
                lte_exists=phone_data['lte_exists'].lower() == 'true',
            )
            phone.save()
            print(f"Phone '{phone_data['name']}' imported successfully.")