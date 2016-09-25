from glueplate import Glue as _


settings = _(
    GLUE_PLATE_ENVIRONMENT_VARIABLE_KEY = 'BASEPACKAGE_SETTINGS_MODULE',
    from_base = 'comming from base',
    to_be_override = 'I am base.',
    something = _(
        good = 'better',
        food = _(
            spam = 'spam',
        )
    ),
    list1 = [1,2,3],
    list2 = [1,2,3],
)
