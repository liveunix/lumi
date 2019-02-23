from lumi.cli import actions

def dispatch(action):
    if action is None:
        return

    """Invoke the right callback for the given action"""
    try:
        module = getattr(actions, action.command)
    except:
        return

    callback = getattr(module, "dispatch", lambda action: False)
    callback(action)
