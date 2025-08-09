from distutils.core import setup
from setuptools import find_packages
import os
import codecs

setup_path = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(setup_path, 'README.md'), encoding='utf-8-sig') as f:
    README = f.read()

setup(name='csigver',
      version='1.0',
      install_requires=[
          'numpy',
          'torch',
          'torchvision',
          'scikit-learn',
          'matplotlib',
          'tqdm',
          'scikit-image'
      ],
      python_requires='>=3',
     
      packages=find_packages())
