from . import actions

def dispatch(action, callback=None):
    if action is None:
        return

    """Invoke the right callback for the given action"""
    if callback is None:
        module = getattr(actions, action.command)
        callback = getattr(module, 'dispatch', lambda action: False)

    return callback(action)

