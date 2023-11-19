from django.urls import path

from .views import ReportUpdateView, ReportDeleteView, ReportListView, ReportCreateView, \
    ReportDetailView

urlpatterns = [
    path('report_create/', ReportCreateView.as_view(), name='report_create'),
    path('report_detail/<int:pk>', ReportDetailView.as_view(), name='report_detail'),
    path('report_update/<int:pk>', ReportUpdateView.as_view(), name='report_update'),
    path('report_delete/<int:pk>', ReportDeleteView.as_view(), name='report_delete'),
    path('', ReportListView.as_view(), name='report_list'),
]
