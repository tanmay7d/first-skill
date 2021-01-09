from mycroft import MycroftSkill, intent_file_handler


class First(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('first.intent')
    def handle_first(self, message):
        self.speak_dialog('first')


def create_skill():
    return First()

