import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name = 'django-sitelight',
    version = '0.1',
    packages = ['sitelight'],
    include_package_data = True,
    license = 'MIT License',
    description = 'A simple Django app to provide a content management system.',
    long_description = README,
    url = 'https://github.com/ByteRockCode/django-sitelight',
    author = 'ByteRock',
    author_email = 'hola@byterock.cl',
    classifiers = [
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)