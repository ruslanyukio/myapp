
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .models import UserLoginForm
from django.conf.urls.static import static
from django.conf import settings

app_name = 'main'

urlpatterns = [
	path('', views.index, name = 'index'),
	# path('accounts/login', views.log_in, name = 'login'),
	path('accounts/login', LoginView.as_view(template_name='accounts/login.html', form_class=UserLoginForm), name = 'login'),
	path('accounts/signup', views.signup, name = 'register'),
	path('accounts/logout', LogoutView.as_view(next_page='/'), name = 'logout'),
	path('accounts/add', views.ChildAdd, name='add'),
	path('profile/', views.myprofile, name='myprofile'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)