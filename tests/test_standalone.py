import os
import unittest
from glueplate import config

class TestGluePlateStandalone(unittest.TestCase):

    def test_load_basepackage_settings(self):
        self.assertEqual(config.settings.GLUE_PLATE_ENVIRONMENT_VARIABLE_KEY, 'BASEPACKAGE_SETTINGS_MODULE')
        self.assertEqual(config.settings.from_base, 'comming from base')
        self.assertEqual(config.settings.from_sub, 'comming from sub')

    def test_override_sub_settings(self):
        self.assertEqual(config.settings.to_be_override, 'I am sub.')

    def test_merge_recursive(self):
        self.assertEqual(config.settings.something.good, 'better')
        self.assertEqual(config.settings.something.bad, 'worse')
        self.assertEqual(config.settings.something.food.spam, 'spam')
        self.assertEqual(config.settings.something.food.egg, 'egg')

    def test_append_before(self):
        _list1 = config.settings.list1
        self.assertEqual(_list1[0], -3)
        self.assertEqual(_list1[1], -2)
        self.assertEqual(_list1[2], -1)
        self.assertEqual(_list1[3], 1)
        self.assertEqual(_list1[4], 2)
        self.assertEqual(_list1[5], 3)
        self.assertFalse('GLUE_PLATE_PLUS_BEFORE_list1' in config.settings)

    def test_append_after(self):
        _list2 = config.settings.list2
        self.assertEqual(_list2[0], 1)
        self.assertEqual(_list2[1], 2)
        self.assertEqual(_list2[2], 3)
        self.assertEqual(_list2[3], 4)
        self.assertEqual(_list2[4], 5)
        self.assertEqual(_list2[5], 6)
        self.assertFalse('GLUE_PLATE_PLUS_AFTER_list2' in config.settings)

    def test_assign(self):
        config.settings.new_var = 'new variable'
        self.assertTrue('new variable', config.settings.new_var)

    def test_reassign(self):
        self.assertTrue('spam' in config.settings.something.food)
        self.assertTrue('egg' in config.settings.something.food)
        config.settings.something.food = dict(ham='HAM')
        self.assertEqual(config.settings.something.food.ham, 'HAM')
        self.assertFalse('spam' in config.settings.something.food)
        self.assertFalse('egg' in config.settings.something.food)
        config.settings.to_be_override = 'from test'
        self.assertEqual(config.settings.to_be_override, 'from test')

        from othermodule import get_food
        config_food_from_othermodule = get_food()
        self.assertTrue('ham' in config_food_from_othermodule)
        self.assertFalse('spam' in config_food_from_othermodule)
        self.assertFalse('egg' in config_food_from_othermodule)
