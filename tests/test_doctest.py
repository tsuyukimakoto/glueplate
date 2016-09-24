import doctest
import os


def load_tests(loader, tests, ignore):
    import glueplate
    tests.addTests(doctest.DocTestSuite(glueplate))
    return tests
