from ckeditor.widgets import CKEditorWidget
from board.models import Board
from django.contrib.auth.models import User
from django import forms

class BoardAddForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'subject', 'content']
        exclude = ('user',)
        widgets = {
            'title' : forms.TextInput(
                attrs={
                    'class' : 'form-control form-control-lg',
                    'placeholder' : '제목',
                    'required' : True
                }
            ),
            
            'subject' : forms.Select(
                choices=(('1', '언어관련문의'), ('2' , '기기관련문의'), ('3' , '기타사항')),
                attrs={
                    'class' : 'form-control form-control-lg',
                    'placeholder': '선택해주세요',
                    'required' : True,
                }
            ),
            'content' : forms.CharField(
                widget = CKEditorWidget(
                    attrs={
                        'placeholoder' : '내용',
                    }
                )   
            ),
        }

        def __init__(self, *args, **kwargs):
            super(BoardAddForm, self).__init__(*args, **kwargs)
            

