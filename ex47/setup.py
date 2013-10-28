try:
    from setuptools import setup
except ImportError:
    from disutils.core import setup

config = {
    'description': 'Ex 47 learn python the hard way',
    'author': 'My name',
    'url': 'Where to get it',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME']
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
