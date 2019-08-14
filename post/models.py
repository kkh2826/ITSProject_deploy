from django.db import models
from django.contrib.auth.models import User
from django import forms
from ckeditor_uploader.fields import RichTextUploadingField
from itsapp.models import Language, Electronics
from PIL import Image
from tagging.fields import TagField



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자')
    lang_category = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, blank=True, verbose_name='언어카테고리')
    elec_category = models.ForeignKey(Electronics, on_delete=models.CASCADE, null=True, blank=True, verbose_name='기기카테고리')
    content = RichTextUploadingField(config_name='special', 
                                    external_plugin_resources=[('youtube',
                                    '/static/ckeditor/ckeditor/plugins/youtube/',
                                    'plugin.js',)], verbose_name='게시물')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='생성일자')
    tag = TagField(verbose_name='태그')

    class Meta:
        ordering = ['-create_date']
    

    def __str__(self):
        return f'{self.user.username} Post'

class Comment(models.Model) :
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} Comment'
