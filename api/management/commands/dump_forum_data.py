import random

from django.core.management.base import BaseCommand, CommandError

from faker import Faker

from api import models

faketory = Faker()


class Command(BaseCommand):
    help = 'Dump forum data'

    def add_arguments(self, parser):
        parser.add_argument('-n', type=int, help='Number of forums to be generated')

    def handle(self, *args, **options):
        n = options['n']
        for i in range(n):
            fid = random.randrange(1, 269)
            try:
                f = models.Forum.objects.create(
                    id=fid,
                    title=f'F{fid}',
                )
                self.stdout.write(self.style.SUCCESS(
                    f'Successfully created n[{i+1}] forum[{f.title}]')
                )
            except:
                pass
