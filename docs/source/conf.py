# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


from socketsc.version import version as release, version
import datetime

project = 'socketsc'
copyright = f'{datetime.datetime.now().year}, Dan5py'
author = 'Dan5py'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_logo = "_static/logo.svg"
html_favicon = "_static/favicon.ico"

html_show_sphinx = False
html_theme_options = {
    "sidebar_hide_name": True,
}

html_title = f"{project} {version} documentation"

html_theme = 'furo'
html_static_path = ['_static']
