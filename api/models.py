from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import JSONField
from django.utils.timezone import now

class DateTimeMixin(models.Model):
    """ Handle datetime for actions like create, modified """
    created_date = models.DateTimeField(default=now)
    modified_date = models.DateTimeField(default=now)

    class Meta:
        abstract = True

    def save(self):
        """
        Override to generate create/update time on save
        """
        if not self.id:
            self.created_date = now()
        self.modified_date = now()
        return super().save()


class Box(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=32)

    class Meta:
        db_table = 'voz_box'


class Forum(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=32)
    box = models.ForeignKey(
        Box, on_delete=models.PROTECT, related_name='forums'
    )

    class Meta:
        db_table = 'voz_forum'


class User(AbstractUser):
    email = models.EmailField(unique=True)
    title = models.CharField(max_length=128)
    avatar_url = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    total_posts = models.PositiveIntegerField(default=0)
    is_banned = models.BooleanField(default=False)
    last_active = models.DateTimeField()

    class Meta:
        db_table = 'voz_user'


class Thread(DateTimeMixin):
    id = models.BigAutoField(primary_key=True)
    forum = models.ForeignKey(
        Forum, on_delete=models.PROTECT, related_name='threads'
    )
    author = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='threads'
    )
    title = models.CharField(max_length=256)
    rating = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    replies = models.PositiveIntegerField(default=0)    
    visible = models.BooleanField(default=True)
    is_sticky = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    delete_reason = models.CharField(max_length=128)
    last_post_data = JSONField(default=None)

    class Meta:
        db_table = 'voz_thread'


class Post(DateTimeMixin):
    CONTENT_FORMATS = (
        (1, 'bbcode'), (2, 'markdown')
    )
    id = models.BigAutoField(primary_key=True)
    thread = models.ForeignKey(
        Thread, on_delete=models.PROTECT, related_name='posts'
    )
    author = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='posts'
    )
    parent = models.ForeignKey(
        'self', on_delete=models.PROTECT, related_name='replies', null=True
    )
    title = models.CharField(max_length=256)
    raw = models.TextField(blank=False, null=False)
    content_format = models.PositiveSmallIntegerField(choices=CONTENT_FORMATS)
    order_number = models.PositiveIntegerField()
    upvotes = models.PositiveIntegerField(default=0)
    visible = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=True)
    delete_reason = models.CharField(max_length=128)

    class Meta:
        db_table = 'voz_post'
        unique_together = (
            ('thread', 'order_number')
        )

    @property
    def html_content(self):
        """
        TODO: Parse raw to html arcording to content_format(bbcode|markdown)
        """
        return self.raw
