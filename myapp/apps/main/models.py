from django.db import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView

class UserRegisterForm(UserCreationForm):
	username = forms.EmailField(widget=(
			forms.TextInput(attrs={"placeholder": "Электронная почта"})
		))
	first_name = forms.CharField(widget=(
		forms.TextInput(attrs={'placeholder': 'Введите имя'})
		))
	last_name = forms.CharField(widget=(
		forms.TextInput(attrs={'placeholder': 'Введите фамилию'})
		))
	lastname = forms.CharField(widget=(
		forms.TextInput(attrs={'placeholder': 'Введите отчество'})
		))
	password1 = forms.CharField(widget=(
		forms.PasswordInput(attrs={'placeholder': 'Введите пароль'})
		))
	password2 = forms.CharField(widget=(
		forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'})
		))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'lastname', 'password1', 'password2')


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	lastname = models.CharField('Отчество', max_length=150)
	avatar = models.ImageField('Аватарка', default='default.png', upload_to="users_avatar")

	def __str__(self):
		return self.user.username




class UserLoginForm(AuthenticationForm):
	username = forms.EmailField(required=True, widget=(
			forms.TextInput(attrs={'placeholder': 'Введите почту'})
		))
	password = forms.CharField(widget=(
			forms.PasswordInput(attrs={'placeholder': 'Введите пароль'})
		))

	class Meta:
		fields = ['username', 'password']


class Children(models.Model):
	OPTIONS = (
			("Мужской", "Мужской"),
			("Женский", "Женский")
		)
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	first_name = models.CharField('Имя ребенка', max_length = 150)
	last_name = models.CharField('Фамилия ребенка', max_length = 150)
	father = models.CharField('Отчество ребенка', max_length = 150)
	bored = models.DateField('Дата рождения')
	# sex = models.Select(choices = OPTIONS)
	img = models.ImageField('Изображение ребенка', default = 'default.png', upload_to = 'users_avatar')

	def __str__(self):

		return self.user.username

	class Meta:
		verbose_name = 'Ребенок'
		verbose_name_plural = "Дети"

# class UploadFile(forms.Form):
# 	def __init__(self, *args, **kwargs):
# 		super(UploadFile, self).__init__(*args, **kwargs)

# 	class Meta:
# 		model = Children
# 		fields = ['img']

class ChildrenForm(forms.Form):
	OPTIONS = (
			("Мужской", "Мужской"),
			("Женский", "Женский")
		)
	first_name = forms.CharField(max_length = 150, widget=(
			forms.TextInput(attrs={'placeholder': "Имя"})
		))
	last_name = forms.CharField(max_length = 150, widget=(
			forms.TextInput(attrs={'placeholder': "Фамилия"})
		))
	father = forms.CharField(max_length = 150, widget=(
			forms.TextInput(attrs={'placeholder': "Отчество"})
		))
	bored = forms.DateField(widget=(
			forms.SelectDateWidget(attrs={'placeholder': "Дата рождения"})
		))
	sex = forms.ChoiceField(choices = OPTIONS)
	img = forms.ImageField()

	class Meta:
		model = Children
		fields = ['first_name', 'last_name', 'father', 'bored',  'sex','img']


