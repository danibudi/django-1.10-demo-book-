# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context


def bad_example(request):
    context = {}
    title = request.GET.get('title', None)

    if title is None:
        return HttpResponseRedirect('/?title=<script>alert(42)</script>')

    context['title'] = title
    t = loader.get_template('bad_example.html')
    c = Context(context)
    return HttpResponse(t.render(c))


def good_example(request):
    context = {}
    title = request.GET.get('title', None)

    context['title'] = title
    t = loader.get_template('good_example.html')
    c = Context(context)
    return HttpResponse(t.render(c))
