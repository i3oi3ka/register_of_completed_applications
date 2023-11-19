from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from .forms import ReportCreateForm
from .models import Report


# Create your views here.

class ReportCreateView(CreateView):
    template_name = 'report/report_create.html'
    form_class = ReportCreateForm


class ReportDetailView(DetailView):
    template_name = 'report/report_detail.html'
    model = Report
    context_object_name = 'report'


class ReportListView(ListView):
    template_name = 'report/report_list.html'
    model = Report
    context_object_name = 'reports'
    paginate_by = 10


class ReportUpdateView(UpdateView):
    template_name = 'report/report_update.html'
    model = Report
    fields = "__all__"


class ReportDeleteView(DeleteView):
    model = Report
    template_name = 'report/report_delete.html'
    success_url = reverse_lazy('report_list')
