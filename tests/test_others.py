import unittest
from glueplate import config


class TestGluePlateOthers(unittest.TestCase):

    def test_parent(self):
        self.assertEqual('FROM_PARENTPACKAGE1', config.settings.from_parentpackage1)
        self.assertEqual('FROM_PARENTPACKAGE2', config.settings.from_parentpackage2)

    def test_parent_sub(self):
        self.assertEqual('FROM_CHILD_PARENTPACKAGE1', config.settings.from_child_parentpackage1)

    def test_parent_sub_parent(self):
        self.assertEqual('GRANPA!', config.settings.from_granpackage1)
