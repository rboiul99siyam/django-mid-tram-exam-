from django import forms
from posts.models import commentModel


class commentForm(forms.ModelForm):
    class Meta:
        model = commentModel
        fields = ["name", "email", "body"]
