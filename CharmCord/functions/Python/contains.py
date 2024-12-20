async def contains(args: str, context):
    """
    Use. $contains[text;value;value;value;...]
    Ex. $contains[I am cool!;cool;dog;city]

    :param args:
    :param context:
    :return:
    """
    data = args.split(';')
    text = data[0]
    del data[0]
    if any(args in text for args in data):
        return True
    return False
