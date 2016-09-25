#import doctest
#import os
import glueplate
from nose.plugins.doctests import Doctest


gluedoctest = Doctest()
gluedoctest.loadTestsFromModule(glueplate)
