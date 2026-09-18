"""Load and merge Glueplate settings from modules named by environment variables."""

import os
from collections.abc import Mapping
from importlib import import_module
from typing import Any

from glueplate import (
    GLUE_PLATE_ENVIRONMENT_VARIABLE_KEY,
    GLUE_PLATE_PARENT_MODULES,
    Glue,
)


def _module_settings(module_name: str) -> Glue:
    module = import_module(module_name)
    module_settings: Any = getattr(module, "settings", None)
    if not isinstance(module_settings, Mapping):
        raise TypeError(f"{module_name!r} must define a mapping named 'settings'")
    return Glue(module_settings)


def _merge_parents(
    settings: Glue,
    environ: Mapping[str, str],
) -> Glue:
    for parent_module_name in settings.get(GLUE_PLATE_PARENT_MODULES, []):
        parent_settings = _module_settings(parent_module_name)
        environment_key = parent_settings.get(GLUE_PLATE_ENVIRONMENT_VARIABLE_KEY)
        if isinstance(environment_key, str) and environment_key in environ:
            parent_settings.update(_module_settings(environ[environment_key]))
            parent_settings = _merge_parents(parent_settings, environ)
        parent_settings.update(settings)
        settings = parent_settings
    return settings


def load_settings(environ: Mapping[str, str] = os.environ) -> Glue:
    """Load the configured base module and merge user and parent settings."""
    try:
        base_module_name = environ["GLUE_PLATE_BASE_MODULE"]
    except KeyError:
        raise ValueError("GLUE_PLATE_BASE_MODULE is not set") from None

    loaded_settings = _module_settings(base_module_name)
    environment_key = loaded_settings.get(GLUE_PLATE_ENVIRONMENT_VARIABLE_KEY)
    if not isinstance(environment_key, str):
        raise ValueError(
            f"{base_module_name!r} must define {GLUE_PLATE_ENVIRONMENT_VARIABLE_KEY}",
        )
    try:
        child_module_name = environ[environment_key]
    except KeyError:
        raise ValueError(f"{environment_key} is not set") from None

    loaded_settings = _merge_parents(loaded_settings, environ)
    loaded_settings.update(_module_settings(child_module_name))
    return loaded_settings


settings = load_settings()
