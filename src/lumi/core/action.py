class CommandAction:
    def __init__(self,
                 name,
                 running_command,
                 buf,
                 pre_message='',
                 post_message=''):
        self.name = name
        self.running_command = running_command
        self.buf = buf
        self.pre_message = pre_message
        self.post_message = post_message

    def buf():
        return self.buf

    def output():
        running_command.wait()
        return self.output

    def done(cmd, success, exit_code):
        self.success = success
        self.exit_code = exit_code

        self.output = self.buf.read()

        # Add call to notify status handler

