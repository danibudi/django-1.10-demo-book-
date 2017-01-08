# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from models import Book
from django.template import loader, Context
import logging


def bad_example(request):
    context = {}
    title = request.GET.get('title', None)

    if title is None:
        return HttpResponseRedirect('/?title=a')
    """
    SQL Injection
    """
    qry = "SELECT * FROM books_book WHERE title='%s'" % (title)
    logging.debug(qry)
    try:
        book = Book.objects.raw(qry)
    except:
        book = None
    context['book'] = book
    logging.debug(qry)
    t = loader.get_template('bad_example.html')
    c = Context(context)
    return HttpResponse(t.render(c))


def good_example(request):
    context = {}
    title = request.GET.get('title', None)

    if title is None:
        return HttpResponseRedirect('/?title=a')
    """
    SQL Injection
    """
    qry = "SELECT * FROM books_book WHERE title=%s"
    logging.debug(qry)
    try:
        book = Book.objects.raw(qry, [title])
        book = book[:]
    except:
        book = None
    context['book'] = book
    logging.debug(qry)
    t = loader.get_template('good_example.html')
    c = Context(context)
    return HttpResponse(t.render(c))
