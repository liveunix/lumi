class change_description:
    def __init__(self, application):
        self.application = application

    @classmethod
    def init(cls, application):
        istance = cls(application)

        return istance.main

    def main(self):
        print(self.application.sender().text())
        self.application.distro_description_textBrowser.setText("TEXT")
