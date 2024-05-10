# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []


class ActionPrintPattern(Action):

    def name(self) -> Text:
        return "action_print_pattern"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        pattern=""
        for i in range(1,6):
            pattern+="*"*i+"\n"
        print(pattern)

        dispatcher.utter_message(text=pattern)

        return []
    
class ActionTestButtons(Action):

    def name(self) -> Text:
        return "action_send_buttons"
    
    def run(self, dispatcher: CollectingDispatcher, tracker:Tracker, domain: Dict[Text,Any]) -> List[Dict[Text,Any]]:

        buttons=[
            {
                "title":"Say Hi",
                "payload":"Hi"
            },
            {
                "title":"Bot Challange",
                "payload":"Are you a bot?"
            },
            {
                "title":"Say Bye",
                "payload":"bye"
            },
            {
                "title":"Memes?",
                "payload":"/send_carousel"
            },
        ]

        dispatcher.utter_message(
            text="Here are some buttons to test things",
            buttons = buttons
        )

        return []
    
class ActionSendCarousel(Action):

    def name(self) -> Text:
        return "action_send_carousel"
    
    def run(self, dispatcher: CollectingDispatcher, tracker:Tracker, domain: Dict[Text,Any]) -> List[Dict[Text,Any]]:

        test_carousel = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "Card 1",
                        "subtitle": "This is subtitle",
                        "image_url": "https://cdn4.sharechat.com/MEEMSOFWORLD_2564253c_1625799332793_sc_cmprsd_40.jpg?tenant=sc&referrer=tag-service&f=rsd_40.jpg",
                        "buttons": [
                            {
                                "title": "Bigger Image",
                                "url": "https://cdn4.sharechat.com/MEEMSOFWORLD_2564253c_1625799332793_sc_cmprsd_40.jpg?tenant=sc&referrer=tag-service&f=rsd_40.jpg",
                                "type": "web_url"
                            },
                            {
                                "title": "See Dev",
                                "url": "https://github.com/Kldpsh7",
                                "type": "web_url"
                            },
                            {
                                "title": "Say Hi",
                                "type": "postback",
                                "payload": "/greet"
                            }
                        ]
                    },
                    {
                        "title": "Second Card",
                        "subtitle": "This is subtitle",
                        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlMHXnQMrq5sxFH-NP-umKcb-rseVn_6lmUQ&usqp=CAU",
                        "buttons": [
                            {
                                "title": "Bigger Image",
                                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlMHXnQMrq5sxFH-NP-umKcb-rseVn_6lmUQ&usqp=CAU",
                                "type": "web_url"
                            },
                            {
                                "title": "See Dev",
                                "url": "https://github.com/Kldpsh7",
                                "type": "web_url"
                            },
                            {
                                "title": "Send buttons",
                                "type": "postback",
                                "payload": "send buttons"
                            }
                        ]
                    },
                    {
                        "title": "Third Card",
                        "subtitle": "This is subtitle",
                        "image_url": "https://static.wikia.nocookie.net/f033fd90-2c9c-4a98-a05b-d99bf915344b/scale-to-width/755",
                        "buttons": [
                            {
                                "title": "Bigger Image",
                                "url": "https://static.wikia.nocookie.net/f033fd90-2c9c-4a98-a05b-d99bf915344b/scale-to-width/755",
                                "type": "web_url"
                            },
                            {
                                "title": "See Dev",
                                "url": "https://github.com/Kldpsh7",
                                "type": "web_url"
                            },
                            {
                                "title": "Bot challange",
                                "type": "postback",
                                "payload": "are you a bot?"
                            }
                        ]
                    }
                ]
            }
        }

        dispatcher.utter_message(attachment=test_carousel)

        return []