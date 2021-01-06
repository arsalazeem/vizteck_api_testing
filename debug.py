import inspect

def last_call():
    curframe = inspect.currentframe()
    calframe = inspect.getouterframes(curframe, 2)
    print('caller name:')
    return calframe[1][5]