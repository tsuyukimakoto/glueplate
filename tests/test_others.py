from glueplate import config


def test_merges_parent_settings() -> None:
    assert config.settings.from_parentpackage1 == 'FROM_PARENTPACKAGE1'
    assert config.settings.from_parentpackage2 == 'FROM_PARENTPACKAGE2'


def test_merges_customized_parent_settings() -> None:
    assert config.settings.from_child_parentpackage1 == 'FROM_CHILD_PARENTPACKAGE1'


def test_merges_grandparent_settings() -> None:
    assert config.settings.from_granpackage1 == 'GRANPA!'
