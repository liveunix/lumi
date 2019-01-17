class it_works:
    def __init__(self, application):
        self.application = application

    @classmethod
    def init(cls, application):
        istance = cls(application)

        return istance.main

    def main(self):
        print("It Works")
