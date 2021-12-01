# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from rasa_sdk import Action


def get_centers(city=None):
    centers = [
        {"name": "Test", "city": "Karachi"},
        {"name": "Test1", "city": "Rawalpindi"},
        {"name": "Test3", "city": "Faisalabad"},
        {"name": "Test2", "city": "Lahore"},
    ]
    if city:
        return [
            center for center in centers if center["city"] == city
        ], "Here are some of the available centers in {}:".format(city)
    else:
        return [], "No available centers found in {}:".format(city)


class ActionQueryDatabase(Action):
    def name(self):
        return "action_query_database"

    def run(self, dispatcher, tracker, domain):
        city = tracker.get_slot("city")
        # hotel = tracker.get_slot("hotel")
        # cuisine = tracker.get_slot("cuisine")
        # results = [{"name": "دی لکھنوی"}]
        # message = ""

        results, message = get_centers(city=city)
        # else:
        # results, message = get_centers()
        dispatcher.utter_message(message)
        # limit to top 5 queries
        for i, obj in enumerate(results):
            dispatcher.utter_message(str(i + 1) + " - " + obj["name"])

        return []
