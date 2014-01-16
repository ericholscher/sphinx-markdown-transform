Sphinx Markdown Transform
=========================

A Sphinx extension that supports turning Markdown-style links into RST links::

    [Link](Target)

Is transformed into::
    
    `Link <Target>`_

That is the only transformation currently supported.
If you care about other syntax,
feel free to add it.

Install
-------

::

    pip install git+https://github.com/ericholscher/sphinx-markdown-transform#egg=sphinx-markdown-transform

Then in your Sphinx config::

    extensions += ['markdowntransform']

