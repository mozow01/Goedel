# -- Project information -----------------------------------------------------
project = "Gödel kurzus jegyzet"
author = "mozow01"

# -- General configuration ---------------------------------------------------
extensions = [
    "myst_parser",
    "sphinx_copybutton",
]

# MyST (Markdown) beállítások – később bővíthető (pl. $...$ matekhoz)
myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "tasklist",
    "colon_fence",
]

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_rtd_theme"

html_static_path = ["_static"]
html_css_files = ["custom.css"]

# Ha repo-nevet is beírod, a "Edit on GitHub" / linkek szépek lesznek
html_context = {
    "display_github": True,
    "github_user": "mozow01",
    "github_repo": "Goedel-2026",  # <-- ezt állítsd a *jegyzet* repód nevére
    "github_version": "main",
    "conf_py_path": "/docs/",
}