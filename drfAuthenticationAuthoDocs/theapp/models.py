from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pygments import highlight
# Create your models here.


Lexers = [i for i in get_all_lexers() if i[1]]
language_choice = sorted([(item[1][0], item[0]) for item in Lexers])
style = sorted([(item, item) for item in get_all_styles()])


class snipet(models.Model):
    created = models.DateField(auto_now=True)
    title = models.CharField(max_length=55, blank=True, default='')
    code = models.TextField()
    language = models.CharField(
        choices=language_choice, default='py', max_length=100)
    style = models.CharField(choices=style, max_length=100, default='Friendly')
    highlight = models.TextField()
    owner = models.ForeignKey(
        'auth.User', related_name='snipets', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos='title',
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['created']
