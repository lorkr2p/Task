from django.urls import path
from .views import *


urlpatterns = [
    path('api/v1/', TaskApiView.as_view(), name='tasks'),
    path('api/v1/<int:detail_id>/', TaskApiView.as_view(), name='task'),
    path('api/v1/update/<int:put_id>/', TaskApiView.as_view(), name='update'),
    path('api/v1/delete/<int:put_id>/', TaskApiView.as_view(), name='delete'),
]
