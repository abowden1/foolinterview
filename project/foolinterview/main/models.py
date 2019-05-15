from django.db import models


class Article_Comments(models.Model):
    id = models.AutoField(primary_key=True)
    article_reference = models.UUIDField()
    comment = models.TextField(max_length=1000)

    def __str__(self):
        return self.comment