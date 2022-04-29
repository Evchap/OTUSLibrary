from django.shortcuts import render

# Create your views here.
#  1 =====================================================

from django.views.generic import ListView

from catalog.models import Book


class BookListView(ListView):
    model = Book

#  2 =====================================================
from django.views.generic.detail import DetailView

from .models import Book


class BookDetailView(DetailView):
    model = Book

# 2

    # def get_object(self, queryset=None):
    #     return Book.objects.get(uuid=self.kwargs.get("uuid"))