import uuid
from django.core.management.base import BaseCommand, CommandError
import pandas as pd
import sqlite3
from django.conf import settings


class Command(BaseCommand):
    help = 'Loads csv data to db'

    def handle(self, *args, **options):
        try:
            print("Started Importing")
            db_name = settings.DATABASES['default']['NAME']
            con = sqlite3.connect(db_name)
            df = pd.read_csv('movies.csv')

            # Generate UUIDs for public_id and add it as a new column to df
            df['public_id'] = [str(uuid.uuid4()) for _ in range(len(df.index))]

            df.to_sql('Quickstart_movie', con, if_exists='append', index=False)
            self.stdout.write('Data imported successfully')
        except Exception as e:
            print("An Error occurred", str(e))
            raise CommandError('Failed to import data: ' + str(e))
