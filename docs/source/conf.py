# Configuration file for the Sphinx documentation builder.

# -- Project information


project = 'PCA Geospatial Data Documentation'
copyright = '2022, Pre-Construct Archaeology'
author = 'Pinna V.'

release = '0.0.1'
version = '0.0.1'

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

html_favicon = 'source/images/PCA_logos/PCA_favicon_64x64.ico'

html_static_path = ['_static']
html_logo = "docs/source/static_images/PCA_logos/PCA_logo_rect_800x588.png"
html_theme_options = {
    'logo_only': False,
    'display_version': False,
    'inner_theme': True,
    'inner_theme_name': 'bootswatch-amelia',
}






# -- Options for EPUB output
# epub_show_urls = 'footnote'
