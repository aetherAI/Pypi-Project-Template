# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os


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

html_title = project
html_static_path = ['_static']

# Sphinx-Immaterial theme options
# https://jbms.github.io/sphinx-immaterial/customization.html#
html_theme = 'sphinx_immaterial'
html_theme_options = {
    # Set the name of the project to appear in the navigation.
    'palette': [
        {
            'scheme': 'slate',
            'toggle': {
                'icon': 'material/brightness-4',
                'name': 'Switch to light mode',
            },
        },
        {
            'scheme': 'default',
            'toggle': {
                'icon': 'material/brightness-7',
                'name': 'Switch to dark mode',
            },
        },
    ],
    'repo_url': 'https://gitlab.com/DYSK_Labs/pypi-project-template',
    'repo_name': 'DYSK_Labs/pypi-project-template',
    'repo_type': 'gitlab',
    'icon': {
        'repo': 'fontawesome/brands/gitlab',
    },
    'version_dropdown': True,
}

ref_name = os.getenv('CI_COMMIT_REF_NAME')
if ref_name:
    html_theme_options['edit_uri'] = f'edit/{ref_name}/docs/source/'
