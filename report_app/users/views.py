from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from .forms import CustomUserCreationForm, LoginForm, ChangeUserInfo
from .models import User


class UserList(ListView):
    model = User
    template_name = 'users/users_list.html'
    context_object_name = 'users'


class UserDetail(DetailView):
    model = User
    template_name = 'users/user_detail.html'
    context_object_name = 'user_info'


class UserCreate(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/user_create.html'

    def form_valid(self, form):
        to_return = super().form_valid(form)
        login(self.request, self.object)
        return to_return


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('users_list')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', context={'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


class UserUpdate(UpdateView):
    form_class = ChangeUserInfo
    template_name = 'users/user_update.html'
    model = User

    def form_valid(self, form):
        form.instance.user = self.request.user  # Передаємо користувача
        return super().form_valid(form)


def password_reset_request(request):
    if request.method == "POST":
        print("post")
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            mail = password_reset_form.cleaned_data['email']
            try:
                user = User.objects.get(email=mail)
            except Exception:
                user = False
            if user:
                subject = 'Запит на скидання пароля'
                email_template_name = "users/password_reset_msg.html"
                print(user.email)
                cont = {
                    "email": user.email,
                    "domain": '127.0.0.1:8000',
                    "site_name": 'Сайт',
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "user": user,
                    "token": default_token_generator.make_token(user),
                    "protokol": 'http',
                }
                msg_html = render_to_string(email_template_name, cont)
                print(cont['uid'], cont['token'])
                try:
                    # msg = EmailMessage(subject,
                    #                    msg_html, to=[user.email])
                    # msg.send()
                    # print(msg.connection)
                    req = send_mail(subject, 'посилання', 'i3oi3ka@ukr.net', [user.email],
                                    fail_silently=True, html_message=msg_html)
                    print("листа відправлено ", req)
                except BadHeaderError:
                    return HttpResponse('Виявлено недопустимий заголовок')
                return redirect("password_reset_done")
            else:
                messages.error(request, 'користувача не знайдено, напишіть адміністратору')
                return redirect('password_reset')
    return render(request=request, template_name='users/password_reset.html')
