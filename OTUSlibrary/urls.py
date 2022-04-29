"""OTUSlibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from catalog import views
from catalog.views import BookListView
from catalog.models import Book
from catalog.views import BookDetailView
# from catalog.admin import Book # n

from django.views.generic import RedirectView

urlpatterns = [
#4
#     path('', views.BookListView.as_view()),
#     path('<slug:pk>/', views.BookDetailView.as_view()),

#3
    # path('', BookDetailView),  # n
#2
    # path('blog/<slug:slug>/', BookDetailView.as_view(), name='book-detail'), # n
    # path('blog/<int:pk>/', BookDetailView.as_view(), name='book-detail'), # n # blog/<int:pk>/ [name='book-detail']
    # path('', BookDetailView.as_view(), name='book-detail'), # n
#1
    path('', BookListView.as_view(), name='home'), # ищет catalog/book_list.html
    path('admin/', admin.site.urls),
    # path('catalog/', include('catalog.urls')),
]
urlpatterns += [
    path('catalog/', include('catalog.urls')),
]

#  RedirectView - перенаправление запроса с корневого URL, на URL приложения catalog
# urlpatterns += [
#     path('', RedirectView.as_view(url='/catalog/', permanent=True)),
# ]

# Использование static() чтобы включить размещение статических файлов.
# Только на период разработки
# from django.conf import settings
# from django.conf.urls.static import static
#
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)