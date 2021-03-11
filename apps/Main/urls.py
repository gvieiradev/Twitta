from django.urls import path
from apps.Main import views
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView

urlpatterns=[
    path('', LoginView.as_view(template_name='social/login.html'), name='login'),
    path('feed', views.feed, name='feed'),
    path('profile/', views.profile, name='profile'),
    path('profile/<str:username>/',views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('password_reset/', PasswordResetView.as_view(template_name='social/recuperar.html', email_template_name='social/password_reset_email.html'), name='password_reset'),
    path('password_reset_done/', PasswordResetDoneView.as_view(template_name='social/password_reset_done.html'), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='social/password_reset_confirm.html'), name='password_reset_confirm'),
    path('done/', PasswordResetCompleteView.as_view(template_name='social/password_reset_complete.html'), name='password_reset_complete'),
    path('logout/', LogoutView.as_view(template_name='social/logout.html'), name='logout'),
    path('follow/<str:username>/', views.follow, name='follow'),
    path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
    path('trends/',views.trends, name='trends'),
    url(r'^edit/(?P<user_id>\d+)/$',views.editarPerfil, name='edit'),
    path('notificaciones/', views.notificaciones, name='notificaciones'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)