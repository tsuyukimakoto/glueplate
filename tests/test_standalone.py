import pytest

from glueplate import Glue, config


def test_loads_and_overrides_settings() -> None:
    assert config.settings.GLUE_PLATE_ENVIRONMENT_VARIABLE_KEY == "BASEPACKAGE_SETTINGS_MODULE"
    assert config.settings.from_base == "comming from base"
    assert config.settings.from_sub == "comming from sub"
    assert config.settings.to_be_override == "I am sub."


def test_merges_nested_settings() -> None:
    assert config.settings.something.good == "better"
    assert config.settings.something.bad == "worse"
    assert config.settings.something.food.spam == "spam"
    assert config.settings.something.food.egg == "egg"


def test_appends_to_lists() -> None:
    assert config.settings.list1 == [-3, -2, -1, 1, 2, 3]
    assert config.settings.list2 == [1, 2, 3, 4, 5, 6]
    assert "GLUE_PLATE_PLUS_BEFORE_list1" not in config.settings
    assert "GLUE_PLATE_PLUS_AFTER_list2" not in config.settings


def test_glue_supports_attribute_access_and_assignment() -> None:
    settings = Glue(spam="spam", nested={"answer": 42})

    settings.ham = "ham"

    assert settings.spam == "spam"
    assert settings.ham == "ham"
    assert settings.nested.answer == 42


def test_missing_attribute_uses_normal_attribute_semantics() -> None:
    settings = Glue()

    assert getattr(settings, "missing", "default") == "default"
    assert not hasattr(settings, "missing")
    with pytest.raises(AttributeError, match="missing"):
        _ = settings.missing


def test_update_merges_nested_mappings() -> None:
    settings = Glue({"food": {"spam": "spam"}})

    settings.update({"food": {"egg": "egg"}})

    assert settings.food == {"spam": "spam", "egg": "egg"}


def test_list_extension_requires_an_existing_list() -> None:
    settings = Glue(value="not a list")

    with pytest.raises(TypeError, match="must be a list"):
        settings.update({"GLUE_PLATE_PLUS_AFTER_value": [1]})


def test_load_settings_requires_base_module() -> None:
    with pytest.raises(ValueError, match="GLUE_PLATE_BASE_MODULE is not set"):
        config.load_settings({})


def test_load_settings_requires_environment_variable_key() -> None:
    environ = {"GLUE_PLATE_BASE_MODULE": "granpackage.granpackage_settings"}

    with pytest.raises(ValueError, match="must define GLUE_PLATE_ENVIRONMENT_VARIABLE_KEY"):
        config.load_settings(environ)


def test_load_settings_requires_child_module() -> None:
    environ = {"GLUE_PLATE_BASE_MODULE": "basepackage.basepackage_settings"}

    with pytest.raises(ValueError, match="BASEPACKAGE_SETTINGS_MODULE is not set"):
        config.load_settings(environ)


def test_load_settings_requires_mapping() -> None:
    environ = {"GLUE_PLATE_BASE_MODULE": "othermodule"}

    with pytest.raises(TypeError, match="must define a mapping named 'settings'"):
        config.load_settings(environ)
