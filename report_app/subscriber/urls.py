from django.urls import path

from .views import SubscriberUpdateView, SubscriberDeleteView, SubscriberListView, SubscriberCreateView, \
    SubscriberDetailView

urlpatterns = [
    path('subscriber_create/', SubscriberCreateView.as_view(), name='subscriber_create'),
    path('subscriber_detail/<int:pk>', SubscriberDetailView.as_view(), name='subscriber_detail'),
    path('subscriber_update/<int:pk>', SubscriberUpdateView.as_view(), name='subscriber_update'),
    path('subscriber_delete/<int:pk>', SubscriberDeleteView.as_view(), name='subscriber_delete'),
    path('subscriber_list/', SubscriberListView.as_view(), name='subscriber_list'),
]
