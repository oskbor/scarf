import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

project = "Scarf"
copyright = "2020-2024, Parashar Dhapola"
author = "Parashar Dhapola"

extensions = [
    "IPython.sphinxext.ipython_console_highlighting",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx_external_toc",
    "sphinx_copybutton",
    "sphinx_tabs.tabs",
    "myst_nb",
]

templates_path = ["_templates"]
master_doc = "index"
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "**.ipynb_checkpoints",
    "vignettes/dev",
]
pygments_style = "sphinx"
language = "en"

external_toc_path = "toctree.yml"
external_toc_exclude_missing = False
myst_enable_extensions = [
    "colon_fence",
]

html_static_path = ["_static"]
html_css_files = ["styles.css"]
html_theme = "sphinx_book_theme"
html_favicon = "favicon.ico"
html_logo = "logo.png"
html_title = "Scarf documentation"
html_theme_options = {
    "repository_url": "https://github.com/parashardhapola/scarf",
    "use_repository_button": True,
    "use_issues_button": False,
    "use_edit_page_button": False,
    "path_to_docs": "docs/source",
    "use_download_button": True,
    "use_fullscreen_button": True,
    "home_page_in_toc": True,
    "show_navbar_depth": 2,
    "toc_title": "Sections",
}
htmlhelp_basename = "Scarf Documentation"
html_sidebars = {
    "**": [
        "globaltoc.html",
        "searchbox.html",
    ],
    'using/windows': ['windows-sidebar.html', 'searchbox.html'],
}

man_pages = [(master_doc, "scarf", "Scarf Documentation", [author], 1)]

nb_execution_allow_errors = True
nb_execution_mode = "auto"
nb_execution_timeout = 5000

import matplotlib

matplotlib.use("agg")
