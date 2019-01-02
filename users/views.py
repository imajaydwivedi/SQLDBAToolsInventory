from django.shortcuts import render
from users.forms import UserForm,UserProfileInfoForm
from django.core.mail import send_mail

# Create your views here.


def index(request):
    return render(request, 'users/index.html')

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
            

    return render(request, 'users/registration.html',
                                {'user_form':user_form,
                                 'profile_form':profile_form,
                                 'registered':registered,
                                }
    )

'''
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
'''