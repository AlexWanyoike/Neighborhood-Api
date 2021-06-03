from django.urls import path , re_path
from . import views
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns=[
    
    path('',views.base,name = 'base'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/neighbors/',views.NeighborhoodList.as_view(),name='neighbor'),
    path('api/business/',views.BusinessList.as_view(),name='business'),
    path('api/users/',views.UserList.as_view(),name='users'),
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)