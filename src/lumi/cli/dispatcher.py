from lumi.cli import actions


def dispatch(action, callback=None):
    if action is None:
        return

    """Invoke the right callback for the given action"""
    if callback is None:
        try:
            module = getattr(actions, action.command)
        except:
            print("Type -h to see the commands available")
            return

        callback = getattr(module, "dispatch", lambda action: False)

    return callback(action)
