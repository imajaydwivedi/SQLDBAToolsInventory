from django.shortcuts import render
from . import forms
from django.core.mail import send_mail

# Create your views here.


def index(request):
    return render(request, 'loginauth/index.html')


def signup(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # Do Something
            print("Validation Success")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])
            send_mail('Signup - SQLDBATools',
                      'Thanks for signing up for SQLDBATools portal. We are verifying your details.',
                      'SQLDBATools@tivo.com',
                      [form.cleaned_data['email']],
                      fail_silently=False,
                      )

    return render(request, 'loginauth/signup.html', {'form': form})
