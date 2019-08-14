from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse

class Board(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="작성자", null=True)
    title = models.CharField(max_length=50, verbose_name='제목')
    subject = models.IntegerField(verbose_name='종류')
    content = RichTextField(verbose_name='내용')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='생성일자')
    update_date = models.DateTimeField(auto_now=True, verbose_name='수정일자')


    def __str__(self):
        return f'{self.user.username} Board'
    
    def get_absolute_url(self):
        return reverse("board:index", args=(self.id,))
    


  