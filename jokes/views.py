from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)

from .forms import JokeForm

from .models import Joke

class JokeCreateView(LoginRequiredMixin, CreateView):
    model = Joke
    # fields = ['question', 'answer']
    form_class = JokeForm

    # 'instance' holds the data in the 'form' object
    # 'return' handles saving the form + redirecting to the success URL
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class JokeDeleteView(UserPassesTestMixin, DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user

class JokeDetailView(DetailView):
    model = Joke

class JokeListView(ListView):
    model = Joke

class JokeUpdateView(UserPassesTestMixin, UpdateView):
    model = Joke
    # fields = ['question', 'answer']
    form_class = JokeForm

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user