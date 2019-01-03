from django.shortcuts import render
from users.forms import UserForm, UserProfileInfoForm, LoginForm
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):
    return render(request, 'users/index.html')


@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")


def user_login(request):
    loggedin = False

    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)

        if login_form.is_valid():
            #username = login_form.cleaned_data['username']
            username = login_form.cleaned_data['username']
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    loggedin = True
                    return HttpResponseRedirect(reverse('projectindex'))
                else:
                    return HttpResponse("Account Not Active")
            else:
                print("Someone tried to login and failed!")
                print("Username: {0} and password {1}".format(
                    username, password))
                return HttpResponse("Invalid login details supplied!")

            # If form is Valid, then
            emailmessage = "username ["+username + \
                "] tried to login in SQLDBATools portal with password '"+password+"'."
            admin_email = 'ajay.dwivedi@tivo.com'

            send_mail('Registration - SQLDBAToolsInventory',
                      emailmessage,
                      'SQLDBATools@tivo.com',
                      [admin_email],
                      fail_silently=False,
                      )

        else:
            print("Invalid details submitted!")
            return HttpResponse("Form details are not valid!")

    else:
        login_form = LoginForm()
        return render(request, 'users/login.html', {'login_form': login_form,
                                                    'loggedin': loggedin,
                                                    }
                      )


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('projectindex'))


def user_register(request):
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

            send_mail('Registration - SQLDBAToolsInventory',
                      'Thanks for signing up for SQLDBATools portal. We are verifying your details.',
                      'SQLDBATools@tivo.com',
                      [user_form.cleaned_data['email']],
                      fail_silently=False,
                      )

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'users/registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered,
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
