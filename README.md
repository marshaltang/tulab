Template for the Read the Docs tutorial
=======================================

This GitHub template includes fictional Python library
with some basic Sphinx docs.

Read the tutorial here:

https://docs.readthedocs.io/en/stable/tutorial/

Installation Steps by Steps
----------------------------

    
Download Sphinx

.. code:: bash
    
    python -m pip install Sphinx -i https://pypi.tuna.tsinghua.edu.cn/simple |默认源可能失败，或网速比较慢|

安装主题

.. code:: bash

    python -m pip install sphinx_theme_pd -i https://pypi.tuna.tsinghua.edu.cn/simple||


add markdown支持 

.. code:: bash

    pip install --upgrade myst-parser


add mermaid支持

.. code:: bash

    pip install sphinxcontrib-mermaid
