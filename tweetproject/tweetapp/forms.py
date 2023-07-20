from django import forms
from django.forms import ModelForm
from tweetapp.models import Tweet

class addtweetform(forms.Form):
    nickname_input = forms.CharField(label="username",max_length=50)
    message_input = forms.CharField(label="message",max_length=100,widget=forms.Textarea(attrs={"class":"tweetmessage"}))
    
    
class addtweetmodelform(ModelForm):
    class Meta:
        model = Tweet
        fields = ["username","message"]