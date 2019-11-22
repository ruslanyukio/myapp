from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate
from .models import UserRegisterForm, Profile, ChildrenForm, Children
from django.contrib import messages


def index(request):
	if request.user.is_authenticated:
		a = Children.objects.filter(user = request.user)
		context = {
			'profile': Profile.objects.get(user = 1),
			'children': a
		}
	else:
		context = {}


	return render(request, 'base.html', context)


def log_in(request):

	return render(request, 'main/login.html')


def signup(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, "Аккаунт успешно создан!")

			return HttpResponseRedirect( reverse('main:login') )
	else:
		form = UserRegisterForm()
	return render(request, 'main/signup.html', {'form': form})



def ChildAdd(request):
	if request.user.is_authenticated:
		if request.method == "POST":

			form = ChildrenForm(request.POST)
			a = Children.objects.create(user = request.user,
						first_name = request.POST['first_name'], last_name = request.POST['last_name'],
						father = request.POST['father'], bored = request.POST['bored'], img = request.FILES['img']
					)
			a.save()

			return HttpResponseRedirect( reverse('main:index') )

		else:
			form = ChildrenForm()
	else:
		return HttpResponseRedirect( reverse('main:login') )

	return render(request, 'main/add.html', {'form': form})


def myprofile(request):
	if request.user.is_authenticated:
		context = {
			'profile': Profile.objects.get(user = request.user),
			'children': Children.objects.filter(user = request.user)
		}
	else:
		return HttpResponseRedirect( reverse('main:login') )

	return render(request, 'main/myprofile.html', context)