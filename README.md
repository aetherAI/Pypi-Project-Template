# Pypi Project Template

## Pypi Jobs Template

Template of `gitlab.ci.yml` for pypi package CI/CD.

### Requirements

1. `pyproject.toml`.
    - `ci-templates/test.gitlab-ci.yml` requires `pytest`, `flake8`.
    - `ci-templates/docs.gitlab-ci.yml` requires `sphinx`.
2. `python` pre-installed in `image` (default image: `python3.7`).
3. `build`, `test`, `deploy` ci stages. (included in [default stages](https://docs.gitlab.com/ee/ci/yaml/#stages))

`poetry` is installed in `default:before_script`, beware that if you have to override `before_script`.

### How to use in your project

Example `.gitlab-ci.yml`:

```yaml
include:
  - project: 'DYSK_Labs/pypi-project-template'
    ref: 3.x  # or other branch / commit / tag
    file:
      - ci-templates/test.gitlab-ci.yml
      - ci-templates/publish.gitlab-ci.yml
      - ci-templates/docs.gitlab-ci.yml
```

### How to override jobs

All jobs in templates extend hidden jobs with leading `.`. When override jobs, always reference to the hidden one to avoid circular reference. 

```yaml
build:
  script:
    - echo "before"
    - !reference [.build, script]
    - echo "after"
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

## Docstring Template

Custom template file for VSCode extension [Python Docstring Generator](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring).

1. Add Custom Template Path

    <img src="https://i.imgur.com/ktMKnIC.png" alt="drawing" width="800"/>

2. Generate docstring for function

    <img src="https://i.imgur.com/ExJ9TsP.png" alt="drawing" width="800"/>

3. Result of generation

    <img src="https://i.imgur.com/MTIdFsI.png" alt="drawing" width="800"/>

4. Result of Pylance display

    <img src="https://i.imgur.com/FUgWYut.png" alt="drawing" width="800"/>
