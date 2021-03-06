from django import forms
from my_blog.models import Article
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(required=True, label=u'username', error_messages={'required': 'username is required'},
                               widget=forms.TextInput(attrs={'placeholder': u'username'}))
    password = forms.CharField(required=True, label=u'password', error_messages={'required': 'password is required'},
                               widget=forms.PasswordInput(attrs={'placeholder': u'password'}))

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"username and password are required")
        else:
            cleaned_data = super(LoginForm, self).clean()


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
