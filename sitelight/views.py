from django.shortcuts import render


def index(request):

    from models import Category

    categories = Category.objects.all()

    return render(request, 'sitelight/index.html', { 'categories' : categories })


def sitemap(request):

    from models import Category

    categories = Category.objects.all()
    host = '%s://%s' % ( request.META.get('wsgi.url_scheme') , request.get_host() )

    return render(request, 'sitelight/sitemap.xml', { 'categories' : categories , 'host' : host }, content_type='application/xhtml+xml')


def page(request, slug):

    from django import template

    try:
        path = 'sitelight/%s.html' % slug
        template.loader.get_template( path )
        return render(request, path)

    except template.TemplateDoesNotExist:

        from django.shortcuts import get_object_or_404
        from models import Category

        category = get_object_or_404( Category , slug=slug )
        return render(request, 'sitelight/category.html', { 'category' : category })


def entry(request, category, entry):

    from django.shortcuts import get_object_or_404
    from models import Entry

    entry = get_object_or_404( Entry , slug=entry)
    return render(request, 'sitelight/entry.html', { 'entry' : entry })
