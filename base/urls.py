from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from . import views

urlpatterns=[

  path('api/neighbors/',views.NeighborhoodList.as_view(),name='neighbor'),
  path('api/update/neighbors/<int:pk>/',views.NeighborhoodList.as_view(),name='update_neighbors'),
  re_path('api/delete/(?P<pk>[0-9]+)/',views.NeighborhoodList.as_view(),name='delete_neighbors'),

  path('api/business/',views.BusinessList.as_view(),name='business'),
  re_path('api/update/business/(?P<pk>[0-9]+)/',views.BusinessList.as_view(),name='update_business'),
  path('api/delete/business/<int:pk>/',views.BusinessList.as_view(),name='delete_business'),

  path('api/users/',views.UserList.as_view(),name='users'),
  path('api/update/users/<int:pk>/',views.UserList.as_view(),name='update_users'),
  path('api/delete/users/<int:pk>/',views.UserList.as_view(),name='delete_users'),
  
  path('api/post/',views.PostList.as_view(),name='post'),
  path('api/update/post/<int:pk>/',views.PostList.as_view(),name='update_post'),
  path('api/delete/post/<int:pk>/',views.PostList.as_view(),name='delete_post'),
  
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)