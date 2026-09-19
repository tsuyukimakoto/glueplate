# glueplate

Glueplate provides composable settings for Python frameworks and libraries. Settings are dictionaries that support attribute access, recursive merging, list extension, and inheritance from other Glueplate configurations.

## Installation

```console
python -m pip install glueplate
```

Glueplate requires Python 3.11 or later.

## Define base settings

Create a module that exports a `settings` value. `GLUE_PLATE_ENVIRONMENT_VARIABLE_KEY` names the environment variable that points to the user's settings module.

```python
from glueplate import Glue

settings = Glue(
    GLUE_PLATE_ENVIRONMENT_VARIABLE_KEY='MY_APP_SETTINGS_MODULE',
    debug=False,
    paths=['base'],
    database={'host': 'localhost', 'port': 5432},
)
```

Set `GLUE_PLATE_BASE_MODULE` to that module and the configured environment variable to the user's module.

```console
export GLUE_PLATE_BASE_MODULE=my_app.default_settings
export MY_APP_SETTINGS_MODULE=my_project.settings
```

The user's module only needs to contain overrides.

```python
from glueplate import Glue

settings = Glue(
    debug=True,
    database={'host': 'database.example.com'},
)
```

Load the merged settings through `glueplate.config`.

```python
from glueplate import config

assert config.settings.debug is True
assert config.settings.database.host == 'database.example.com'
assert config.settings.database.port == 5432
```

## Extend lists

Use `GLUE_PLATE_PLUS_BEFORE_` or `GLUE_PLATE_PLUS_AFTER_` followed by the target setting name.

```python
from glueplate import Glue

settings = Glue(
    GLUE_PLATE_PLUS_BEFORE_paths=['project-first'],
    GLUE_PLATE_PLUS_AFTER_paths=['project-last'],
)
```

The merged value is `['project-first', 'base', 'project-last']`.

## Inherit settings

A base settings module can include other Glueplate settings modules.

```python
from glueplate import Glue

settings = Glue(
    GLUE_PLATE_ENVIRONMENT_VARIABLE_KEY='MY_APP_SETTINGS_MODULE',
    GLUE_PLATE_PARENT_MODULES=[
        'another_library.default_settings',
    ],
)
```

## Development

The development environment is managed with [uv](https://docs.astral.sh/uv/).

```console
uv sync --locked
uv run pytest
uv run ruff check .
uv run pyrefly check
uv build
uv run twine check dist/*
```

## License

Glueplate is distributed under the MIT License.
