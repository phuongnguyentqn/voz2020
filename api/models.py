from django.db import models
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


class User(models.Model):
    pass


class Thread(DateTimeMixin):
    pass


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
        'self', on_delete=models.PROTECT, related_name='replies'
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


class Forum(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=32)

    class Meta:
        db_table = 'voz_forum'
        # TBD: index, get_latest_by, order


class Box(models.Model):
    pass
