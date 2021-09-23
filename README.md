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
        file: pypi_jobs.gitlab-ci.yml

    # Optional:
    # upload_pypi:
    #   extends: .upload_pypi_template

    # trigger_master_generate_badge:
    #   extends: .trigger_master_generate_badge_template

    # generate_badge:
    #   extends: .generate_badge_template
    ```

2. Add badge with image url: <https://gitlab.com/%{project_path}/-/jobs/artifacts/${default_branch}/raw/package_badge.svg?job=generate_badge>
