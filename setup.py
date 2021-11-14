from distutils.core import setup
from setuptools import find_packages

setup(name='yd57yjac',
      version='0.1',
      author='DSSS',
      author_email='yipeng.sun@fau.de',
      packages=find_packages(),
      install_requires=['numpy', 'Pillow', 'ipywidgets', '[matplotlib.pyplot]'])
