from app.models.point import PointRuleModel


def add_point_rules():
    good_point_rule = PointRuleModel(
        name='상점 규칙',
        point_type=True,
        min_point=1,
        max_point=3
    ).save()

    bad_point_rule = PointRuleModel(
        name='벌점 규칙',
        point_type=False,
        min_point=1,
        max_point=5
    ).save()

    return good_point_rule, bad_point_rule
