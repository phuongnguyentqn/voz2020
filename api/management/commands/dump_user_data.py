from django.core.management.base import BaseCommand, CommandError

from faker import Faker

from api import models

faketory = Faker()


class Command(BaseCommand):
    help = 'Dump user data'

    def add_arguments(self, parser):
        parser.add_argument('-n', type=int, help='Number of users to be generated')

    def handle(self, *args, **options):
        n_users = options['n']
        for i in range(n_users):
            fake_profile = faketory.profile(fields=None, sex=None)
            user = models.User.objects.create(
                username=fake_profile['username'],
                email=fake_profile['mail'],
                title=faketory.sentences(nb=2),
                date_joined=faketory.date_object(end_datetime=None),
                last_active=faketory.date_between(start_date="-30d", end_date="today")
            )
            self.stdout.write(self.style.SUCCESS(
                f'Successfully created n[{i+1}] user[{user.username}]')
            )
