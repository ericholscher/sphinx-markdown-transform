Sphinx Markdown Link
====================

A Sphinx extension that supports turning Markdown-style links into RST links::

    [Link](Target)

Is transformed into::
    
    `Link <Target>`_

That is the only transformation currently supported.
If you care about other syntax,
feel free to add it.

