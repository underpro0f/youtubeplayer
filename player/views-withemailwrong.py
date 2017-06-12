from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
#from django.core.context_processors import csrf
#from forms import *
#from models import *
from django.template import RequestContext
from django.core.mail import send_mail
import hashlib, datetime, random
from django.utils import timezone

def register_user(request):
    args = {}
    #args.update(csrf(request))
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        args['form'] = form

        if form.is_valid():
            form.save() # save user to database if form is valid
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
            activation_key = hashlib.sha1(salt+email).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(2)
            #Get user by username
            user=User.objects.get(username=username)
            # Create and save user profile
            new_profile = UserProfile(user=user, activation_key=activation_key,
            key_expires=key_expires)
            new_profile.save()
            # Send email with activation key
            email_subject = 'Подтверждение регистрации'
            email_body = "Hey %s, thanks for signing up. To activate your account, click this link within \48hours http://127.0.0.1:8082/accounts/confirm/%s" % (username, activation_key)
            send_mail(email_subject, email_body, 'myemail@example.com',
                      [email], fail_silently=False)
            return HttpResponseRedirect('/accounts/register_success')
        else:
            args['form'] = RegistrationForm()
            return render(request,'user_profile/register.html', args, )

def register_confirm(request, activation_key):
    #check if user is already logged in and if he is redirect him to some other url, e.g. home
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home')
    # check if there is UserProfile which matches the activation key (if not then display 404)
    else:
        user_profile = get_object_or_404(UserProfile, activation_key=activation_key)
    #check if the activation key has expired, if it hase then render confirm_expired.html
        if user_profile.key_expires < timezone.now():
            return render_to_response('user_profile/confirm_expired.html')
        #if the key hasn't expired save user and set him as active and render some template to confirm activation
        else:
            user = user_profile.user
            user.is_active = True
            user.save()
            return render_to_response('user_profile/confirm.html')
