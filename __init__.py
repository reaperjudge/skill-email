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
        # Sending a command to mycroft, speak Greetings Dialog
        self.send_email("I am here","it works. I am from in five minites. Don't open the next email.")
        
    def stop(self):
        pass

def create_skill():
    return HelloWorldSkill()
