import os
import logging
from importlib import import_module
from .. import GLUE_PLATE_ENVIRONMENT_VARIABLE_KEY


logger = logging.getLogger(__name__)

ENVIRONMENT_VARIABLE = 'GLUE_PLATE_MODULE'

if __name__ == 'glueplate.config':
    if not os.environ['GLUE_PLATE_BASE_MODULE']:
        raise ValueError("need glueplate's GLUE_PLATE_ENVIRONMENT_VARIABLE_BASE_KEY in environment.")
    base_module_name = os.environ['GLUE_PLATE_BASE_MODULE']
    logger.info('Load base glueplate config: {0}'.format(base_module_name))
    settings = import_module(base_module_name).settings
    if GLUE_PLATE_ENVIRONMENT_VARIABLE_KEY not in settings:
        raise ValueError("neet GLUE_PLATE_ENVIRONMENT_VARIABLE_KEY in base config settings.")
    modified_module_name = os.environ[settings.GLUE_PLATE_ENVIRONMENT_VARIABLE_KEY]
    _settings = import_module(modified_module_name).settings
    settings.update(_settings)
