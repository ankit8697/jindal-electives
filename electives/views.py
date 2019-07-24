from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Elective, Comment
from .forms import CommentForm
from tablib import Dataset
from .resources import ElectiveResource

# Create your views here.

def about(request):
    return render(request, 'electives/about.html')

def login(request):
    return render(request, 'electives/login.html')

class ElectiveListView(ListView):
    model = Elective
    template_name = 'electives/home.html'
    context_object_name = 'electives'
    ordering = ['name']


class ElectiveDetailView(DetailView):
    model = Elective

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ElectiveDetailView, self).get_context_data(**kwargs)
        # Add extra context from another model
        context['comments'] = Comment.objects.filter(elective_id=self.kwargs['pk']) 
        return context


class CommentCreateView(CreateView):
    model = Comment
    fields = ['body']


# class CommentDetailView(DetailView):
#     model = Comment
#     context_object_name = "comment"
#     template_name = "comment_detail.html"


def add_comment_to_elective(request, pk):
    elective = Elective.objects.get(pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.elective = elective
            comment.save()
            return redirect('electives-detail', pk=elective.pk)
    else:
        form = CommentForm()
    return render(request, 'electives/add_comment_to_elective.html', {'form': form})
