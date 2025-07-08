from munch import DefaultMunch


def handler(event, context):
    _event = DefaultMunch.fromDict(event)
    print(_event)
