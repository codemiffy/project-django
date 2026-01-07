# mysite/urls.py
from django.contrib import admin
from django.urls import path, include  # Pastikan include di-import
from django.contrib.auth import views
from blog import views as blog_views
from django.conf import settings
from django.conf.urls.static import static 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('accounts/logout/', blog_views.custom_logout, name='logout'),
    path('', include('blog.urls')),  # Tambahkan baris ini
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
