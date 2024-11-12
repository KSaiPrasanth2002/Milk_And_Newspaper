from django.urls import path
from django.http import HttpResponseNotFound
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('favicon.ico', lambda request: HttpResponseNotFound()),
    path('', views.website_page, name='website'),
    path('website.html', views.website_page, name='website'),
    path('our-story.html', views.our_story_view, name='OurStory'),
    path('products.html', views.products_view, name='Products'),
    path('subscription.html', views.subscription_view, name='subscription'),
    path('login.html', views.login, name='login'),
    path('login/website/', views.website_page, name='website'),
    path('website/Products/', views.products_view, name='website_products'),
    path('registration.html', views.registration, name='registration'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout, name='logout'),
    path('our-story/website.html', views.our_story_view, name='our_story'),
    path('our-story/OurStory.html', views.our_story_view, name='our_story'),
    path('our-story/subscription.html', views.our_story_view, name='our_story'),
    path('registration/login.html', views.registration, name='registration_index'),

    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('transactions/', views.transactions, name='transactions'),
    path('my_subscriptions/', views.my_subscriptions, name='my_subscriptions'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html', html_email_template_name='password_reset_email.html'), name='password-reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)