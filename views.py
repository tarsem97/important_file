import json
from django.http import HttpResponse
from .models import User,Message,Response_message
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import signUp,loginform,message_date_filterform,Response_messages_form
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django_perfect import settings

from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == 'POST':
        form_login = loginform(request.POST)
        if form_login.is_valid():
            email = form_login.cleaned_data['email']
            password = form_login.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                auth_login(request, user)
                request.session['user_id'] = user.id
                request.session['role'] = request.user.role
                response_data = {'url': settings.SITE_URL + "dashboard/", 'message': 'login Successfully',
                                 'status': 'success'}
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                response_data = {'url': settings.SITE_URL, 'message': 'Invalid Details',
                                 'status': 'error'}
                return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        url = settings.SITE_URL
        form_login = loginform()
        page_title="Signin"
        return render(request, 'administrator/login.html', {'page_title':page_title,'form_login':form_login,'url': url})




def sign_up(request):
    url = settings.SITE_URL
    if request.method == 'POST':
        #print(request.POST)
        form = signUp(request.POST)
        print(form)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                response_data = {'message': 'username already exsist',
                                 'status': 'error', 'url': url + 'signup/'}
                return HttpResponse(json.dumps(response_data), content_type="application/json")
            else:
                email = form.cleaned_data['email']
                if User.objects.filter(email=email).exists():
                    response_data = {'message': 'email already exsist',
                                     'status': 'error', 'url': url + 'signup/'}
                    return HttpResponse(json.dumps(response_data), content_type="application/json")
                else:
                    password = form.cleaned_data['password']
                    confirm_password = form.cleaned_data['confirm_password']
                    role = form.cleaned_data['role']
                    if password != confirm_password:
                        response_data = {'message': 'password and conform password do not matched',
                                         'status': 'error','url': url + 'signup/'}
                        return HttpResponse(json.dumps(response_data), content_type="application/json")
                    else:
                        myuser=User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password, role=role)
                        myuser.save()
                        response_data = {'message': 'Thanks for your Registration user has been created Successfully',
                                         'status': 'success', 'url': url}
        else:
            response_data = {'message': 'There is an error to submit a form please check and resubmit again',
                             'status': 'error', 'url': url + 'signup/'}

        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        url = settings.SITE_URL
        form = signUp()
        page_title = "Signup"
        return render(request, 'administrator/signup.html', {'page_title':page_title,'form': form, 'url': url})

@login_required(login_url=settings.SITE_URL)
def dashboard(request):
    url = settings.SITE_URL
    current_user = request.user.first_name
    user_first_capital=request.user.first_name[0]
    page_title = "Dashboard"
    user_email = request.user.email
    return render(request,'administrator/dashboard.html', {'page_title':page_title,'url': url, 'user_logged_in':current_user,'user_email':user_email,'user_first_capital':user_first_capital})


def logout(request):
    auth_logout(request)
    messages.success(request, "Logout Successfully")
    return redirect(settings.SITE_URL)

@login_required(login_url=settings.SITE_URL)
def perfect(request):
    url = settings.SITE_URL
    if request.method == 'POST':
        form = message_date_filterform(request.POST)

        # start_date = form.cleaned_data['start_date']
        # end_date = form.cleaned_data['end_date']
        start_date=request.POST['start_date']
        end_date=request.POST['end_date']
        add=Message.objects.filter(start_date__gte=start_date, end_date__gte=end_date)
        print(add)
        current_user = request.user.first_name
        user_first_capital=request.user.first_name[0]
        page_title = "Dashboard"
        user_email = request.user.email
        return render(request, 'administrator/perfect.html',
                  {'page_title': page_title, 'url': url, 'user_logged_in': current_user, 'user_email': user_email,'user_first_capital': user_first_capital, 'form': form,'add':add})
    else:
        current_user = request.user.first_name
        user_first_capital = request.user.first_name[0]
        page_title = "Dashboard"
        user_email = request.user.email
        add = Message.objects.all()
        form = message_date_filterform(request.POST)
        return render(request,'administrator/perfect.html', {'page_title':page_title,'url': url, 'user_logged_in':current_user,'user_email':user_email,'user_first_capital':user_first_capital,'add':add,'form': form})


def create_response_message(request):
    url = settings.SITE_URL
    if request.method == "POST":
        form = Response_messages_form(request.POST, request.FILES)
        if form.is_valid:
            #print(request.FILES)
            title = request.POST.get('message')
            image=request.FILES.get('image')
            description = request.POST.get('description')
            message = request.POST.get('message')
            responseobj=Response_message.objects.create(title=title, description=description, message=message, image=image)
            response = responseobj.save()
            if response == 0:
                response_data = {'message': 'There is an error to inserting',
                                 'status': 'error'}
            else:
                response_data = {'message': 'response messages created successfully',
                                 'status': 'success'}
            return HttpResponse(json.dumps(response_data), content_type="application/json")
    current_user = request.user.first_name
    user_first_capital = request.user.first_name[0]
    page_title = "Dashboard"
    user_email = request.user.email
    form = Response_messages_form()
    return render(request, 'administrator/response_message.html',
                  {'page_title': page_title, 'url': url, 'user_logged_in': current_user, 'user_email': user_email,
                   'user_first_capital': user_first_capital, 'form': form})



def view_response_message(request):
    url = settings.SITE_URL
    current_user = request.user.first_name
    user_first_capital = request.user.first_name[0]
    page_title = "Dashboard"
    user_email = request.user.email
    view_data=Response_message.objects.all()
    return render(request, 'administrator/view_response_message.html',
                  {'page_title': page_title, 'url': url, 'user_logged_in': current_user, 'user_email': user_email,
                   'user_first_capital': user_first_capital,'view_data':view_data})


def delete_response_message(request, id):
    response_data = Response_message.objects.get(id=id)
    response_data.delete()
    return redirect(settings.SITE_URL + 'view-response-message/')


def update_response_message(request, id):
    url = settings.SITE_URL
    if request.method == 'POST':
        test_data = Response_message.objects.get(id=id)
        form = Response_messages_form(request.POST, request.FILES, instance=test_data)
        if form.is_valid():
            response_update=form.save()
            if response_update == 0:
                response_data = {'message': 'There is an error to updating the data',
                                 'status': 'error'}
            else:
                response_data = {'message': 'response messages updated successfully',
                                 'status': 'success'}
            return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        edit_response_data = Response_message.objects.filter(id=id)
        initial_data = {'title': edit_response_data[0].title, 'message': edit_response_data[0].message,
                        'description': edit_response_data[0].description}
        form = Response_messages_form(initial=initial_data)
    current_user = request.user.first_name
    user_first_capital = request.user.first_name[0]
    page_title = "Dashboard"
    user_email = request.user.email
    image_response_data = Response_message.objects.get(id=id)
    image_url=image_response_data.image
    return render(request, 'administrator/update_response_message.html', {'id':id,'form': form,'page_title': page_title, 'url': url, 'user_logged_in': current_user, 'user_email': user_email,
                   'user_first_capital': user_first_capital,'image_url':image_url})