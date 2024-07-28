# -- Path setup --------------------------------------------------------------
import os
import sys
from datetime import datetime as dt

#sys.path.append("scripts")
#from gallery_directive import GalleryDirective

# -- Project information -----------------------------------------------------

project = "NFETRA"
copyright = f"Betlem, Mohn, Tugend, Morzelle 2023-{dt.today().year}"
author = "Betlem, Mohn, Tugend, Morzelle"

import pydata_sphinx_theme


# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinxext.rediraffe",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx_carousel.carousel",
    # For extension examples and demos
    "ablog",
    "jupyter_sphinx",
    "matplotlib.sphinxext.plot_directive",
    "myst_nb",
    "sphinx_external_toc",
    # "nbsphinx",  # Uncomment and comment-out MyST-NB for local testing purposes.
    "numpydoc",
    "sphinx_togglebutton",
    "sphinxcontrib.bibtex"
]

bibtex_bibfiles = ['references.bib', 'latest-publications.bib']
bibtex_default_style = "plain"

carousel_bootstrap_prefix = ""

external_toc_path = "_toc.yml"  # optional, default: _toc.yml
external_toc_exclude_missing = False  # optional, default: False

# -- Internationalization ------------------------------------------------
# specifying the natural language populates some key tags
language = "en"

# ReadTheDocs has its own way of generating sitemaps, etc.
if not os.environ.get("READTHEDOCS"):
    extensions += ["sphinx_sitemap"]

    # -- Sitemap -------------------------------------------------------------
    html_baseurl = os.environ.get("SITEMAP_URL_BASE", "http://127.0.0.1:8000/")
    sitemap_locales = [None]
    sitemap_url_scheme = "{link}"

autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints", "**.ipynb"]

# -- Extension options -------------------------------------------------------

# This allows us to use ::: to denote directives, useful for admonitions
myst_enable_extensions = ["colon_fence", "linkify", "substitution"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"
#html_logo = "_static/logo.svg"
#html_favicon = "_static/logo.svg"
#html_sourcelink_suffix = ""

# Define the json_url for our version switcher.
#json_url = "https://pydata-sphinx-theme.readthedocs.io/en/latest/_static/switcher.json"

# Define the version we use for matching in the version switcher.
#version_match = os.environ.get("READTHEDOCS_VERSION")
# If READTHEDOCS_VERSION doesn't exist, we're not on RTD
# If it is an integer, we're in a PR build and the version isn't correct.
#if not version_match or version_match.isdigit():
    # For local development, infer the version to match from the package.#
#    release = pydata_sphinx_theme.__version__#
#    if "dev" in release or "rc" in release:
#        version_match = "latest"
        # We want to keep the relative reference if we are in dev mode
        # but we want the whole url if we are effectively in a released version
#        json_url = "_static/switcher.json"
#    else:
#        version_match = "v" + release

html_permalinks = False

html_theme_options = {
    "navigation_with_keys": False,
    "show_prev_next": False,
    "external_links": [
        #{
    #        "url": "index.html",
    #        "name": "Home",
    #    },
    #    {
    #        "url": "map.html",
    #        "name": "Map",
    #    },
    #    {
    #        "url": "team.html",
    #        "name": "Team",
    #    },
    #    {
    #        "url": "https://numfocus.org/",
    #        "name": "NumFocus",
    #    },
    #    {
    #        "url": "https://numfocus.org/donate",
    #        "name": "Donate to NumFocus",
    #    },
    ],
    #"github_url": "https://github.com/pydata/pydata-sphinx-theme",
    #"twitter_url": "https://twitter.com/PyData",
    "header_links_before_dropdown": 4,
    "icon_links": [
        #{
        #    "name": "PyPI",
        #    "url": "https://pypi.org/project/pydata-sphinx-theme",
        #    "icon": "fa-solid fa-box",
        #},
        {
            "name": "Github",
            "url": "https://github.com/nfetra",
            "icon": "_static/logos/github.svg",
            "type": "local",
            "attributes": {"target": "_blank"},
        },
    ],
    "logo": {
        "text": "NFETRA Project",
    #    "image_dark": "logo-dark.svg",
        "alt_text": "NFETRA",
    },
    #"use_edit_page_button": True,
    #"show_toc_level": 1,
    "article_header_start": [],
    "navbar_align": "content",  # [left, content, right] For testing that the navbar items align properly
    "navbar_center": ["navbar-nav"],
   # "announcement": "<p>These pages are under maintenance - check back regularly for the latest improvements!</p>",
    #"show_nav_level": 1,
    "navbar_start": ["navbar-logo"],
    #"navbar_end": ["navbar-icon-links"],
    #"navbar_persistent": ["search-button"],
    # "primary_sidebar_end": ["custom-template.html", "sidebar-ethical-ads.html"],
    #"content_footer_items": ,
    "footer_start": ["copyright"],
    "footer_end": []
    # "secondary_sidebar_items": ["page-toc.html"],  # Remove the source buttons
    #"switcher": {
    #    "json_url": json_url,
    #    "version_match": version_match,
    #},
    # "search_bar_position": "navbar",  # TODO: Deprecated - remove in future version
}

html_sidebars = {
    "**": []
    #"community/index": [
    #    "sidebar-nav-bs",
    #    "custom-template",
    #],  # This ensures we test for custom sidebars
    #"examples/no-sidebar": [],  # Test what page looks like with no sidebar items
    #"examples/persistent-search-field": ["search-field"],
    ## Blog sidebars
    ## ref: https://ablog.readthedocs.io/manual/ablog-configuration-options/#blog-sidebars
    #"examples/blog/*": [
    #    "postcard.html",
    #    "recentposts.html",
    #    "tagcloud.html",
    #    "categories.html",
    #    "authors.html",
    #    "languages.html",
    #    "locations.html",
    #    "archives.html",
    #],
}

myst_heading_anchors = 2
myst_substitutions = {"rtd": "[Read the Docs](https://readthedocs.org/)"}

#html_context = {
#    "github_user": "pydata",
#    "github_repo": "pydata-sphinx-theme",
#    "github_version": "main",
#    "doc_path": "docs",
#}

#rediraffe_redirects = {
#    "contributing.rst": "community/index.rst",
#}

# ABlog configuration
#blog_path = "examples/blog/index"
#blog_authors = {
#    "pydata": ("PyData", "https://pydata.org"),
#    "jupyter": ("Jupyter", "https://jupyter.org"),
#}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]
todo_include_todos = True

numfig = True

import sys
from sphinx.application import Sphinx
from sphinx.util import logging
sys.path.append("./scripts")

from people import build_teamgallery
from zotero import generate_zotero_library

def setup(app: Sphinx):
    app.connect("builder-inited", build_teamgallery)
    app.connect("builder-inited", generate_zotero_library)
