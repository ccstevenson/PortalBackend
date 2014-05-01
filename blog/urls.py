from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

from views import *

urlpatterns = patterns('',
                       # Use 'localhost:8001/blog/' to access these views. Ex., 'localhost:8001/blog/booklist'.
                       url(r'booklist$', nested_book_list, name='nested-book-list'),
                       )
