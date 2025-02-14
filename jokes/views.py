from django.urls import reverse_lazy

from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)

from .forms import JokeForm

from .models import Joke

class JokeCreateView(CreateView):
    model = Joke
    # fields = ['question', 'answer']
    form_class = JokeForm

    # 'instance' holds the data in the 'form' object
    # 'return' handles saving the form + redirecting to the success URL
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class JokeDeleteView(DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')

class JokeDetailView(DetailView):
    model = Joke

class JokeListView(ListView):
    model = Joke

class JokeUpdateView(UpdateView):
    model = Joke
    # fields = ['question', 'answer']
    form_class = JokeForm