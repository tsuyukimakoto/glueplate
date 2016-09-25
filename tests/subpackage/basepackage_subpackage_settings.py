from glueplate import Glue as _


settings = _(
    from_sub='comming from sub',
    to_be_override = 'I am sub.',
    something = _(
        bad = 'worse',
        food = _(
            egg = 'egg',
        )
    ),
    GLUE_PLATE_PLUS_BEFORE_list1 = [-3, -2, -1],
    GLUE_PLATE_PLUS_AFTER_list2 = [4, 5, 6],
)
