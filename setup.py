from setuptools import setup, find_packages

setup(
    name='sphinx-markdown-transform',
    version='0.1',
    author='Eric Holscher',
    author_email='eric@ericholscher.com',
    url='http://github.com/ericholscher/sphinx-markdown-transform',
    license='BSD',
    description='Source transformations of Markdown constructs for Sphinx',
    package_dir={'': '.'},
    packages=find_packages('.'),
)
