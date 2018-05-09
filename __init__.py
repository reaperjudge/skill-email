# Importing IntentBuilder
from adapt.intent import IntentBuilder
# Importing MycroftSkill class
from mycroft.skills.core import MycroftSkill

__author__ = 'reaperjudge'

# Creating HelloWorldSKill extending MycroftSkill
class HelloWorldSkill(MycroftSkill):
    def __init__(self):
        super(HelloWorldSkill, self).__init__(name="EmailSkill")

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
        self.send_email("Message From Your Picroft", dialog + <img width="400" height="400" data="putinmeme02.jpg"></img>)
        self.speak(dialog)
    def stop(self):
        pass

def create_skill():
    return HelloWorldSkill()
