from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
# Create your models here.


Lexers = [i for i in get_all_lexers() if i[1]]
language_choice = sorted([(item[1][0], item[0]) for item in Lexers])
style = sorted([(item, item) for item in get_all_styles()])


class snipet(models.Model):
    created = models.DateField(auto_now=True)
    title = models.CharField(max_length=55, blank=True, default='')
    code = models.TextField()
    lineos = models.BooleanField(default=False)
    language = models.CharField(
        choices=language_choice, default='py', max_length=100)
    style = models.CharField(choices=style, max_length=100, default='Friendly')

    class Meta:
        ordering = ['created']
