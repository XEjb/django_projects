from django import forms
from .models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'age']

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': "Имя автора",
            }),
            'age': forms.NumberInput()
        }


class NameForm(forms.Form):
    name = forms.IntegerField(label='Enter age')
