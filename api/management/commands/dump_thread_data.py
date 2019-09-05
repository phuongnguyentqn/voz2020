import random

from django.core.management.base import BaseCommand, CommandError

from faker import Faker

from api import models

faketory = Faker()


class Command(BaseCommand):
    help = 'Dump thread data'

    def add_arguments(self, parser):
        parser.add_argument('-n', type=int, help='Number of threads to be generated')

    def handle(self, *args, **options):
        n = options['n']
        users = list(models.User.objects.values_list('id', flat=True).all())
        forums = list(models.Forum.objects.values_list('id', flat=True).all())
        for i in range(n):
            total_posts = random.randrange(1, 40)
            t = models.Thread.objects.create(
                forum_id=random.choice(forums),
                author_id=random.choice(users),
                title=faketory.sentence(
                    nb_words=6, variable_nb_words=True,
                    ext_word_list=None
                ),
                last_poster_id=random.choice(users),
                total_posts=total_posts,
            )
            for j in range(total_posts):
                models.Post.objects.create(
                    title=f'Re - {t.title}',
                    thread_id=t.id,
                    author_id=random.choice(users),
                    content_format=random.choice([1, 2]),
                    raw=faketory.text(max_nb_chars=200, ext_word_list=None),
                    order_number=j+1,
                )
            self.stdout.write(self.style.SUCCESS(
                f'Successfully created n[{i+1}] thread[{t.title}]')
            )
