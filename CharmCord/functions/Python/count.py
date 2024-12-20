async def count(code, context):
    """
    Use. $count[text or list]
    Ex. $count[Hi]

    :param code:
    :param context:
    :return:
    """
    if isinstance(code, list):
        try:
            return len(code)
        except:
            return
    else:
        try:
            return len([i for i in code.split(" ") if len(i) > 0])
        except:
            return 0
