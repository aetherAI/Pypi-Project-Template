# Pypi Project Template


## Pypi Jobs Template

Template of `gitlab.ci.yml` for pypi package CI/CD.

### Requirments

1. `pyproject.toml`.
2. `deploy` ci stages. (`.post` is always included)
3. `python` & `pip` pre-installed in ci `image` or via `before_script`

### How to use

1. add the following to `.gitlab-ci.yml`

    ```yaml
    include:
      - project: 'DYSK_Labs/pypi-project-template'
        ref: <Ref> (e.g. branch or commit or tag)
        file: pypi_jobs.gitlab-ci.yml

    # Optional
    upload_pypi:
      extends: .upload_pypi_template
      # override setings

    test_upload_pypi:
      extends: .test_upload_pypi_template
      # override setings

    trigger_master_generate_badge:
      extends: .trigger_master_generate_badge_template
      # override setings

    generate_badge:
      extends: .generate_badge_template
      # override setings
    ```

2. Add badge with image url: <https://gitlab.com/%{project_path}/-/jobs/artifacts/${default_branch}/raw/package_badge.svg?job=generate_badge>

## Shared Configuration

[nitpick](https://nitpick.readthedocs.io/en/latest/index.html)

```bash
$ poetry add -D nitpick
```

add the following section to your `.nitpick.toml` or `pyproject.toml` ([detail](https://nitpick.readthedocs.io/en/latest/configuration.html#configuration))

```toml
[tool.nitpick]
style = "<path-to-style-file>"
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
