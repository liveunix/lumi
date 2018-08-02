VERSION = '0.1.0'

def dispatch(action):
    """Callback for the version command"""
    print('LUMI ver%s | Licensed under GNU/GPL v3' % VERSION)
    return VERSION
