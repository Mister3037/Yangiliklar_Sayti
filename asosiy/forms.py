from django import forms
from .models import *

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"


class YangilikForm(forms.ModelForm):
    class Meta:
        model = Yangiliklar
        fields = ["sarlavha", "matn", "rasm", "category", "status",]