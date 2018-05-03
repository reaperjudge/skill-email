# Importing IntentBuilder
from adapt.intent import IntentBuilder
# Importing MycroftSkill class
from mycroft.skills.core import MycroftSkill

__author__ = 'reaperjudge'

# Creating HelloWorldSKill extending MycroftSkill
class HelloWorldSkill(MycroftSkill):
    def __init__(self):
        super(HelloWorldSkill, self).__init__(name="HelloWorldSkill")

    def initialize(self):
        # Creating GreetingsIntent requiring Greetings vocab
        greetings = IntentBuilder("GreetingsIntent"). \
            require("greetings").build()
        # Associating a callback with the Intent
        self.register_intent(greetings,
                             self.handle_greetings)
        
    def handle_greetings(self, message):
        dialog = self.dialog_renderer.render("greetings", None)
        # Sending a command to mycroft, speak Greetings Dialog
        self.send_email(dialog)
        self.speak(dialog)
        
    def stop(self):
        pass

def create_skill():
    return HelloWorldSkill()
