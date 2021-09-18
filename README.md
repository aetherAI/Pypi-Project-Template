# Pypi Project Template

## Requirments

1. `pyproject.toml`.
2. `deploy` ci stages. (`.post` is always included)

## How to use

1. add the following to `.gitlab-ci.yml`
    ```yaml
    include:
      - project: 'DYSK_Labs/pypi-project-template'
        ref: <Ref> (e.g. branch or commit or tag)
        file: ci-template.yml

    # Optional:
    # upload_pypi:
    #    something you want to override
    # trigger_master_generate_badge:
    #    something you want to override
    # generate_badge:
    #    something you want to override
    ```

2. Add badge with image url: <https://gitlab.com/%{project_path}/-/jobs/artifacts/${default_branch}/raw/package_badge.svg?job=generate_badge>
