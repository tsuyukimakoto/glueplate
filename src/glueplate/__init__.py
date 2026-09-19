"""Composable settings with attribute-style access."""

from collections.abc import Iterable, Mapping
from typing import Any

GLUE_PLATE_ENVIRONMENT_VARIABLE_KEY = 'GLUE_PLATE_ENVIRONMENT_VARIABLE_KEY'
GLUE_PLATE_PLUS_BEFORE = 'GLUE_PLATE_PLUS_BEFORE_'
GLUE_PLATE_PLUS_AFTER = 'GLUE_PLATE_PLUS_AFTER_'
GLUE_PLATE_PARENT_MODULES = 'GLUE_PLATE_PARENT_MODULES'


def _updated_list(
    original: 'Glue',
    key: str,
    values: list[Any],
    *,
    before: bool,
) -> list[Any]:
    target_key = key.removeprefix(
        GLUE_PLATE_PLUS_BEFORE if before else GLUE_PLATE_PLUS_AFTER,
    )
    current = original[target_key]
    if not isinstance(current, list):
        raise TypeError(f'{target_key!r} must be a list')
    return values + current if before else current + values


def _update(
    original: 'Glue',
    updates: Mapping[str, Any],
) -> None:
    for key, value in updates.items():
        if key.startswith(GLUE_PLATE_PLUS_BEFORE) and isinstance(value, list):
            target_key = key.removeprefix(GLUE_PLATE_PLUS_BEFORE)
            original[target_key] = _updated_list(original, key, value, before=True)
        elif key.startswith(GLUE_PLATE_PLUS_AFTER) and isinstance(value, list):
            target_key = key.removeprefix(GLUE_PLATE_PLUS_AFTER)
            original[target_key] = _updated_list(original, key, value, before=False)
        elif isinstance(value, Mapping):
            current = original.get(key)
            nested = Glue(current) if isinstance(current, Mapping) else Glue()
            _update(nested, value)
            original[key] = nested
        else:
            original[key] = value


class Glue(dict[str, Any]):
    """A recursively mergeable dictionary with attribute-style access."""

    def __init__(
        self,
        *args: Mapping[str, Any] | Iterable[tuple[str, Any]],
        **kwargs: Any,
    ) -> None:
        super().__init__()
        for values in args:
            for key, value in dict(values).items():
                self[key] = value
        for key, value in kwargs.items():
            self[key] = value

    def __getattr__(self, key: str) -> Any:
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key) from None

    def __setattr__(
        self,
        key: str,
        value: Any,
    ) -> None:
        self[key] = value

    def __setitem__(
        self,
        key: str,
        value: Any,
    ) -> None:
        nested_value = (
            Glue(value) if isinstance(value, Mapping) and not isinstance(value, Glue) else value
        )
        super().__setitem__(key, nested_value)

    def update(
        self,
        other: Any = (),
        /,
        **kwargs: Any,
    ) -> None:
        values = dict(other)
        values.update(kwargs)
        _update(self, values)
