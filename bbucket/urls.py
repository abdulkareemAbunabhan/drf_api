from django.urls import path
from .views import BucketList, BucketDetail

urlpatterns = [
    path('', BucketList.as_view(), name='buckets_list'),
    path('<int:pk>/', BucketDetail.as_view(), name='buckets_detail'),
]