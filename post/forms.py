from ckeditor_uploader.widgets import CKEditorUploadingWidget
from post.models import Post
from itsapp.models import Language, Electronics
from django.contrib.auth.models import User
from multiupload.fields import MultiFileField
from tagging.fields import TagField, TagFormField
from tagging.forms import TagField
from django import forms
from django.forms import ModelForm
from .models import Comment

class CommentForm(forms.ModelForm) :
    class Meta :
        model = Comment
        fields = ['message']
        widgets = {
            'message' : forms.TextInput(
                attrs = {
                    'class' : 'form-control type_msg form-control-lg',
                    'placeholder' : 'Type your message...',
                    'style' : 'width:500px;',
                     
                }
            )
        }

class PostAddForm(forms.ModelForm):
    class Meta:
        model = Post
        lang_category = forms.ModelChoiceField(queryset=Language.objects.all())
        elec_category = forms.ModelChoiceField(queryset=Electronics.objects.all())
        fields = ['content', 'lang_category', 'elec_category', 'tag']
        widgets = {
            'content' : forms.CharField(
                widget = CKEditorUploadingWidget(
                    attrs={
                        'placeholoder' : '내용',
                    }
                )   
            ),
           
            'lang_category' : forms.Select(
                attrs = {
                    'class' : 'form-control form-control-lg'
                }
            ),

            'elec_category' : forms.Select(
                attrs = {
                    'class' : 'form-control form-control-lg'
                }
            ),
            'tag' : forms.TextInput(
                attrs={
                    'class' : 'form-control form-control-lg',
                    'placeholder' : '키워드를 입력해주세요.(ex : 홍길동, 화이팅)'
                }
            ),
        }
       
        def __init__(self, *args, **kwargs):
            super(PostAddForm, self).__init__(*args, **kwargs)


