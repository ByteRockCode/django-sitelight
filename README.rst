=====
Sitelight
=====

Sitelight is a simple Django app to provide a content management system.

Quick start
-----------

1. Add "sitelight" to your INSTALLED_APPS setting like this::

      INSTALLED_APPS = (
          ...
          'sitelight',
      )

2. Include the sitelight URLconf in your project urls.py like this::

      url(r'^', include('sitelight.urls')),

3. Run `python manage.py syncdb` to create the sitelight models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/.
