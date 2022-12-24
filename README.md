# Pypi Project Template

This project provides snippets for python library developers.

- [GitLab CI Templates](#gitlab-ci-templates)
  - [Requirements](#requirements)
  - [Usage](#usage)
  - [Docs Site](#docs-site)
- [Shared Configuration](#shared-configuration)
- [Auto Docstring Template](#auto-docstring-template)

## GitLab CI Templates

Template of `gitlab.ci.yml` for pypi package CI/CD.

### Requirements

1. `pyproject.toml`.
    - `ci-templates/test.gitlab-ci.yml` requires `pytest`, `flake8`.
    - `ci-templates/docs.gitlab-ci.yml` requires `sphinx`, `sphinx-immaterial` (for version dropdown).
2. `python` pre-installed in `image` (default image: `python:3.7`).
3. `build`, `test`, `deploy` stages. (included in [default stages](https://docs.gitlab.com/ee/ci/yaml/#stages))
4. `docs` requires
    - `$CI_PUSH_TOKEN` environment variable.
    - `docs/` generated by `sphinx-quickstart docs --sep`.
    - `docs/build/html`, `public/` are *RESERVED* for generated docs.
    - `pages` branch is *RESERVED* for public pages.

poetry will be installed in `script` of each jobs.

### Usage

Example `.gitlab-ci.yml`:

```yaml
include:
  - project: 'DYSK_Labs/pypi-project-template'
    ref: master  # or other branch / commit / tag
    file:
      - ci-templates/test.gitlab-ci.yml
      - ci-templates/publish.gitlab-ci.yml
      - ci-templates/docs.gitlab-ci.yml
```

All jobs in templates extend corresponding hidden jobs with leading `.`. When override jobs, reference to the hidden one to avoid circular reference.

```yaml
build:
  script:
    - echo "before"
    # !reference [build, script] causes circular reference
    - !reference [.build, script]
    - echo "after"
```

There's also a [.snippet](ci-templates/snippets.gitlab-ci.yml#L10) section to be reused.

```yaml
test:
  script:
    - echo "before install poetry"
    - !reference [.snippet, install-poetry]
    ...
```

`before_script` & `after_script` are not defined by templates. Feel free to add commands like `apt-get install`.

### Docs Site

The generated docs site will be served by [GitLab Pages](https://docs.gitlab.com/ee/user/project/pages/), located at `https://dysk_labs.gitlab.io/${project_name}`, check the [demo site](https://dysk_labs.gitlab.io/pypi-project-template/).

It's also included in `test-docs` job's artifact (only single version).

Don't forget to add `version_dropdown` to your `conf.py`:

```python
extensions = [
    ...
    'sphinx_immaterial',
]
html_theme = 'sphinx_immaterial'
html_theme_options = {
    ...
    'version_dropdown': True,
}
```

## Shared Configuration

Configuration includes `flake8`, `isort` & `coverage`.

[nitpick](https://nitpick.readthedocs.io/en/latest/index.html)

```bash
$ pip install nitpick
```

add the following section to your `.nitpick.toml` or `pyproject.toml` ([detail](https://nitpick.readthedocs.io/en/latest/configuration.html#configuration))

```toml
[tool.nitpick]
style = [
    # don't forget to replace the <REF>
    "https://github.com/aetherAI/Pypi-Project-Template/blob/<REF>/nitpick-style/lint.toml",
    # ...,  optional, will override the former
    "https://github.com/aetherAI/Pypi-Project-Template/blob/<REF>/nitpick-style/coverage.toml",
]
cache = "never"
```

finally, run:

```bash
$ nitpick check -v
$ nitpick fix -v
```

## Auto Docstring Template

Custom template file for VSCode extension [Python Docstring Generator](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring).

1. Add Custom Template Path

    <img src="https://i.imgur.com/ktMKnIC.png" alt="drawing" width="800"/>

2. Generate docstring for function

    <img src="https://i.imgur.com/ExJ9TsP.png" alt="drawing" width="800"/>

3. Result of generation

    <img src="https://i.imgur.com/MTIdFsI.png" alt="drawing" width="800"/>

4. Result of Pylance display

    <img src="https://i.imgur.com/FUgWYut.png" alt="drawing" width="800"/>
