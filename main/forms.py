# -*- coding: utf-8 -*-

from captcha.fields import CaptchaField
from ckeditor.fields import RichTextFormField
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(), label='نام کاربری')
    password = forms.CharField(widget=forms.TextInput(attrs={'type': 'password'}), label='پسورد')
    # captcha = CaptchaField(label='عبارت امنیتی')


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(), label='نام کاربری')
    password = forms.CharField(widget=forms.TextInput(attrs={'type': 'password'}), label='پسورد')
    email = forms.EmailField(widget=forms.TextInput(), label='آدرس ایمیل',
                             help_text='eg: example@example.com')
    first_name = forms.CharField(widget=forms.TextInput(), label='نام')
    last_name = forms.CharField(widget=forms.TextInput(), label='نام خانوادگی')
    # captcha = CaptchaField(label='عبارت امنیتی')


class SubmitResultForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(), label='عنوان')
    content = RichTextFormField(label='محتوای پاسخ')


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(widget=forms.TextInput(attrs={'type': 'password'}), label='پسورد فعلی')
    new_password = forms.CharField(widget=forms.TextInput(attrs={'type': 'password'}), label='پسورد جدید')
    new_password_confirm = forms.CharField(widget=forms.TextInput(attrs={'type': 'password'}), label='تایید پسورد جدید')