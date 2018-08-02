from . import actions

def dispatch(action, callback=None):
    """Invoke the right callback for the given action"""
    if callback is None:
        module_name = action.command.replace('-', '_')
        module = getattr(actions, module_name)

        callback = getattr(module, 'dispatch', lambda action: False)
    return callback(action)