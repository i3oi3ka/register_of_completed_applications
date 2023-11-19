from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from .forms import SubscriberCreateForm
from .models import Subscriber


# Create your views here.

class SubscriberCreateView(CreateView):
    template_name = 'subscriber/subscriber_create.html'
    form_class = SubscriberCreateForm


class SubscriberDetailView(DetailView):
    template_name = 'subscriber/subscriber_detail.html'
    model = Subscriber
    context_object_name = 'subscriber'


class SubscriberListView(ListView):
    template_name = 'subscriber/subscriber_list.html'
    model = Subscriber
    context_object_name = 'subscribers'
    paginate_by = 2


class SubscriberUpdateView(UpdateView):
    template_name = 'subscriber/subscriber_update.html'
    model = Subscriber
    fields = "__all__"


class SubscriberDeleteView(DeleteView):
    model = Subscriber
    template_name = 'subscriber/subscriber_delete.html'
    success_url = reverse_lazy('subscriber_list')
