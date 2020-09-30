from django.shortcuts import render, redirect
from .models import Book, Author


def index(req):
    context = {
        "all_books": Book.objects.all()
    }
    return render(req, 'index.html', context)


def new_book(req):
    print(req.POST)

    form_book_title = req.POST.get('form_book_title', 'C#')
    form_book_desc = req.POST.get('form_book_desc', 'Impressive.')

    Book.objects.create(title=form_book_title, desc=form_book_desc)
    return redirect('/')


def delete(req, idBook):
    book = Book.objects.get(id=idBook)
    book.delete()
    return redirect("/")


def edit(req, idBook):
    context = {
        book: Book.objects.get(id=idBook)
    }
    return render(req, "edit.html", context)


def update_book(req, idBook):
    print(req.POST)
    book = Book.objects.get(id=idBook)
    book.title = req.POST.get("title", "ooo")
    book.save()
    return redirect("/")


def books(req, idBook):
    book = Book.objects.get(id=idBook)
    all_authors = Author.objects.all()
    context = {
        "book": book,
        "all_authors": all_authors
    }
    return render(req, 'books.html', context)


def author_to_book(req, idBook):
    print(req.POST)
    this_book = Book.objects.get(id=idBook)
    this_author = req.POST.get('form_author_info', 1)

    this_book.authors.add(this_author)

    return redirect(f'/books/{idBook}')
