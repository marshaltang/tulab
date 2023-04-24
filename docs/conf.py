# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'tulab'
copyright = '2019~2023, tulab'
author = 'tulab'

release = '0.1'
version = '0.1'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
language = 'zh_CN'
# -- Options for EPUB output
html_show_sourcelink = False
html_last_updated_fmt = '%b %d, %Y'
epub_show_urls = 'footnote'
