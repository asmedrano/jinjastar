try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Jinja Template rendering from the command line',
    'author': 'Angel Medrano',
    'url': 'angelmedrano.com',
    'download_url': '',
    'author_email': 'asmedrano@gmail.com',
    'version': '0.1',
    'install_requires': ['jinja2'],
    'packages': ['jinjastar'],
    'scripts': ['bin/jstar.py'],
    'name': 'jinjastar'
}

setup(**config)
