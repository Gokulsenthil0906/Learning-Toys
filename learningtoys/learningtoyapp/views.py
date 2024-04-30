from django.shortcuts import render
from .models import contact 
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ['firstname', 'lastname', 'email', 'phone', 'subject', 'message']


def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return render(request, 'index.html')
            except Exception as e:
                print("Error saving contact:", e)
        else:
            print("Form is not valid:", form.errors)
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})