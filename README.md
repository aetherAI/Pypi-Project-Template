# Pypi Project Template


## Pypi Jobs Template

Template of `gitlab.ci.yml` for pypi package CI/CD.

### Requirments

1. `pyproject.toml`.
2. `test`, `deploy` ci stages. (included by default)
3. `python >= 3.7` pre-installed in `image`

### How to use

1. add the following to `.gitlab-ci.yml`

    ```yaml
    include:
      - project: 'DYSK_Labs/pypi-project-template'
        ref: <Ref> (e.g. branch or commit or tag)
        file:
          - ci-templates/test.gitlab-ci.yml
          - ci-templates/deploy.gitlab-ci.yml

    build:
      extends: .build_template
      # override example
      before_script:
        - !reference [default, before_script]
        - some new stuff
    test:
      extends: .test_template

    lint:
      extends: .lint_template

    publish:
      extends: .publish_template

    ```

## Shared Configuration

[nitpick](https://nitpick.readthedocs.io/en/latest/index.html)

```bash
$ pip install nitpick
```

add the following section to your `.nitpick.toml` or `pyproject.toml` ([detail](https://nitpick.readthedocs.io/en/latest/configuration.html#configuration))

```toml
[tool.nitpick]
style = [
    "https://github.com/aetherAI/Pypi-Project-Template/blob/<ref>/nitpick-style/lint.toml",
    # ...,  optional, will override the former
    "https://github.com/aetherAI/Pypi-Project-Template/blob/<ref>/nitpick-style/coverage.toml",
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
