"""meeseeks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('geo/', include('geo.urls', namespace='geo')),
    path('fil/', include('fil.urls', namespace='fil')),
    path('fil/results', include('fil.urls', namespace='fil_results')),
    path('portal/', include('portal.urls', namespace='portal')),
    path('', RedirectView.as_view(url='/portal/')),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
