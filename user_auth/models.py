from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


class User(models.Model):
    owner = models.ForeignKey(
        'auth.User', related_name='snippets', on_delete=models.CASCADE
        )

    highlighted = models.TextField()
    
    
    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'table': self.title} if self.title else {}
        
        formatter = HtmlFormatter(
            style=self.style, linenos=linenos, full=True, **options
        )
        self.highlighted = highlight(self.code, lexer, formatter)
        super(User, self).save(*args, **kwargs)
    