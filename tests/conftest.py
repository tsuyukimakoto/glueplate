import os

os.environ.setdefault('GLUE_PLATE_BASE_MODULE', 'basepackage.basepackage_settings')
os.environ.setdefault('BASEPACKAGE_SETTINGS_MODULE', 'subpackage.basepackage_subpackage_settings')
os.environ.setdefault(
    'PARENTPACKAGE_SETTINGS_MODULE',
    'parentpackage1.child_parentpackage1_settings',
)
