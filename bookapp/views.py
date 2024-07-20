from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView, TemplateView
from .models import Book
from .forms import BookForm, BookModelForm

class ListBook(ListView):
    model = Book
    template_name = 'listbook.html'
    context_object_name = 'books'

class DetailBook(DetailView):
    model = Book
    template_name = 'detailbook.html'
    context_object_name = 'book'

class CreateBook(CreateView):
    model = Book
    template_name = 'createbook.html'
    form_class = BookModelForm
    success_url = reverse_lazy('book_success')

class UpdateBook(UpdateView):
    model = Book
    template_name = 'createbook.html'
    form_class = BookModelForm
    success_url = reverse_lazy('book_success')

class DeleteBook(DeleteView):
    model = Book
    template_name = 'deletebook.html'
    success_url = reverse_lazy('listbook')

class BookFormView(FormView):
    form_class = BookForm
    template_name = 'createbook.html'
    success_url = reverse_lazy('book_success')

    def form_valid(self, form):
        # Create a new Book instance but don't save it to the database yet
        book = Book(
            title=form.cleaned_data['title'],
            author=form.cleaned_data['author'],
            published_date=form.cleaned_data['published_date'],
            ISBN=form.cleaned_data['ISBN'],
            pages=form.cleaned_data['pages'],
            cover=form.cleaned_data.get('cover', '')
        )
        # Save the instance to the database
        book.save()
        return super().form_valid(form)

class SuccessView(TemplateView):
    template_name = 'success.html'
