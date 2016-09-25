from glueplate import Glue as _


settings = _(
    from_child_parentpackage1 = 'FROM_CHILD_PARENTPACKAGE1',
    GLUE_PLATE_PARENT_MODULES=[
        'granpackage.granpackage_settings',
    ]
)
