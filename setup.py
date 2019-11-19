from distutils.core import setup
from setuptools import find_packages

setup(
  name = 'shexer',
  packages = find_packages(), # this must be the same as the name above
  version = '0.0.4',
  description = 'Automatic schema extraction for RDF graphs',
  author = 'Daniel Fernandez-Alvarez',
  author_email = 'danifdezalvarez@gmail.com',
  url = 'https://github.com/DaniFdezAlvarez/shexerp3',
  download_url = 'https://github.com/DaniFdezAlvarez/shexer/tarball/0.0.4',
  keywords = ['testing', 'shexer', 'shexerp3', "rdf", "shex", "schema"],
  classifiers = [],
)