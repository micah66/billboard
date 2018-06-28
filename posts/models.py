from django.db import models

# Create your models here.
class Post(models.Model):
    date = models.DateTimeField('Date Created', auto_now_add=True)
    title = models.CharField('Title', max_length=75)
    body = models.TextField('Body', )
    author = models.CharField('Author', max_length=40)

    def __str__(self):
        return '{0} - {1}'.format(self.title, self.author)
