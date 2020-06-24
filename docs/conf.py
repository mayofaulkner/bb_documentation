# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import os
import sys

#src = os.path.abspath('../src')
#os.environ['PYTHONPATH'] = src


# -- Project information -----------------------------------------------------

project = 'bb_documentation'
copyright = '2020, M Faulkner'
author = 'M Faulkner'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
   #'nbsphinx',
    'sphinx.ext.mathjax',
    'recommonmark',
    'sphinx.ext.githubpages'
]

nbsphinx_execute_arguments = [
    "--InlineBackend.figure_formats={'svg', 'pdf'}",
    "--InlineBackend.rc={'figure.dpi': 96}",
]

# Only execute Jupyter notebooks that have no evaluated cells
#nbsphinx_execute = 'never'
# Kernel to use for execution
#nbsphinx_kernel_name = 'python3'
# Cancel compile on errors in notebooks
#nbsphinx_allow_errors = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.ipynb_checkpoints']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Look for md and rst files
source_parsers = {
    '.md': 'recommonmark.parser.CommonMarkParser',
}
source_suffix = ['.rst', '.md']

plot_formats = [('png', 512)]
# -- Run and convert the notebook files to RST --------------------------------

_root = os.path.abspath(os.path.join(os.path.dirname(__file__)))
_scripts_path = os.path.join(_root, 'scripts')
if _scripts_path not in sys.path:
    sys.path.insert(1, _scripts_path)

from convert import process_notebooks
nb_tutorials_path = os.path.join(_root, 'notebooks_processed')
template_path = os.path.join(_root, 'templates', 'template.tpl')
rst_output_path = os.path.join(_root, 'rst-notebooks')
colab_template_path = os.path.join(_root, 'templates', 'colab_template.ipynb')

#processkwargs = dict(output_path=rst_output_path, template_file=template_path)
#if os.environ.get('NBCONVERT_KERNEL'):  # this allows access from "make html"
#    processkwargs['kernel_name'] = os.environ.get('NBCONVERT_KERNEL')
#
#if os.environ.get('NBFILE'):  # this allows only building a single tutorial file
#    nb_tutorials_path = os.path.abspath(os.environ.get('NBFILE'))

process_notebooks(nb_tutorials_path, output_path=rst_output_path, template_file=template_path,
                  colab_template=colab_template_path, overwrite=True)


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
html_static_path = ['notebooks_processed', '_static']
html_static_path = [os.path.join(_root, x)
                    for x in html_static_path]


