from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Адрес эл. почты'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Тема'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Сообщение'}))

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field_name, filed in self.fields.items():
            filed.widget.attrs['class'] = 'form-control mt-1'