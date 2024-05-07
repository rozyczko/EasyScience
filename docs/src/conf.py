# -*- coding: utf-8 -*-

#  SPDX-FileCopyrightText: 2021 EasyScience contributors  <core@easyscience.software>
#  SPDX-License-Identifier: BSD-3-Clause
#  © 2021 Contributors to the EasyScience project <https://github.com/easyScience/EasyScience>

#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
# import toml
from pathlib import Path
# import easyscience
# sys.path.insert(0, os.path.abspath('.'))
main_root = Path(__file__).parents[2]
sys.path.append(str(main_root))

import datetime

# project_info = toml.load(os.path.join(main_root, 'pyproject.toml'))

# -- Project information -----------------------------------------------------

project = 'EasyScience'
copyright = f"{datetime.date.today().year}, EasyScience Contributors"
author = "EasyScience Contributors"
# copyright = f"2021, {project_info['tool']['poetry']['authors'][0]}"
# author = project_info['tool']['poetry']['authors'][0]

# # The short X.Y version
# version = ''
# # The full version, including alpha/beta/rc tags
# release = project_info['tool']['poetry']['version']
# The short X.Y version.
#version = project_info['project']['version'] 
# The full version, including alpha/beta/rc tags.
#version = project_info['project']['version']
# version = easyscience.__version__
version = "0.6.0" # hardcoded for testing


intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'pint': ('https://pint.readthedocs.io/en/stable/', None),
    'xarray': ('https://xarray.pydata.org/en/stable/', None)
}

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinx_autodoc_typehints',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'sphinx.ext.intersphinx',
    'sphinx_rtd_theme',
    'sphinx_gallery.gen_gallery',
]
autoclass_content = 'init'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'
highlight_language = 'python3'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_logo = os.path.join('_static', 'ec_sidebar_w.png')
html_favicon = os.path.join('_static', 'favicon.ico')
html_theme_options = {'logo_only': True}
# html_theme_options = {
#     'logo': os.path.join('ec_logo_single.png'),
#     'github_user': project_info['tool']['github']['info']['organization'],
#     'github_repo': project_info['tool']['github']['info']['repo'],
# }



# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'easySciencedoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'EasyScience.tex', 'EasyScience Documentation',
     'Simon Ward', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'EasyScience', 'EasyScience Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'EasyScience', 'EasyScience Documentation',
     author, 'EasyScience', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


sphinx_gallery_conf = {
     'examples_dirs': [os.path.join(main_root, 'Examples', 'base'),
                       os.path.join(main_root, 'Examples', 'fitting')],   # path to your example scripts
     'gallery_dirs': ['base_examples', 'fitting_examples'],  # path to where to save gallery generated output
    'backreferences_dir': 'gen_modules/backreferences',     # directory where function/class granular galleries are stored
    # Modules for which function/class level galleries are created. In
    # this case sphinx_gallery and numpy in a tuple of strings.
    'doc_module':         ('sphinx_gallery', 'numpy', 'EasyScience'),
}