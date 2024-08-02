import pandas as pd
from django.core.management.base import BaseCommand
from api.models import UserProfile, HealthData

class Command(BaseCommand):
    help = 'Load dummy data into the database'

    def handle(self, *args, **kwargs):
        # Load the dataset
        df = pd.read_csv('data/dummy_data.csv')

        # Iterate over the rows and save to the database
        for _, row in df.iterrows():
            user_profile, created = UserProfile.objects.get_or_create(
                name=row['name'],
                age=row['age'],
                gender=row['gender'],
                chronic_diseases=row['chronic_diseases']
            )
            HealthData.objects.create(
                user=user_profile,
                metric=row['metric'],
                value=row['value']
            )
        self.stdout.write(self.style.SUCCESS('Successfully loaded dummy data'))
