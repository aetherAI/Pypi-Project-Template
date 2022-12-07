# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'example_project'
copyright = '2022, Jsaon Lin'
author = 'Jsaon Lin'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_immaterial',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_immaterial'
html_static_path = ['_static']
html_theme_options = {
    # Set the name of the project to appear in the navigation.
    'nav_title': project,
    'palette': [
        {
            'scheme': 'slate',
            'toggle': {
                'icon': 'material/brightness-4',
                'name': 'Switch to light mode',
            },
            'primary': 'cyan',
        },
        {
            'scheme': 'default',
            'toggle': {
                'icon': 'material/brightness-7',
                'name': 'Switch to dark mode',
            },
            'primary': 'cyan',
        },
    ],

    # Set the repo location to get a badge with stats
    'features': [
        'navigation.expand',
        'navigation.indexes',
        'navigation.top',
        'search.highlight',
    ],
    'version_dropdown': True,
}
