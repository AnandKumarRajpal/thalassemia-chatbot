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
        {"name": "Fatimid Foundation Karachi", "address": "Head Office 393, Britto Road, Garden East, Karachi",
            "contact": "+92-21-2225284", "website": "https://www.fatimid.org", "city": "Karachi"},
        {"name": "PWA Patients Welfare Association Karachi", "address": "Dr Ruth K.M. Pfau Civil Hospital Karachi",
            "contact": "+92-21-32735214", "website": "", "city": "Karachi"},
        {"name": "Afzaal Memorial Thalassemia Foundation", "address": "1/C Shahrah-e-Jahangir, Block 10 Gulberg Town, Karachi",
            "contact": "+92-21-36366452", "website": "https://afzaalfoundation.org/", "city": "Karachi"},
        {"name": "Kashif Iqbal Thalassemia Care Center", "address": "A-19, Street 1, Mujahid Colony, Dalmia Cement Factory Road Gulshan e Iqbal, Karachi",
            "contact": "+92-21-34981190", "website": "https://www.kashifiqbal.com/", "city": "Karachi"},
        {"name": "National Institute of Blood Disease(NIBD)", "address": "ST 2/A Block 17 Gulshan-e-Iqbal KDA Scheme 24 Karachi",
            "contact": "+92-21-34824250-3", "website": "https://www.nibd.edu.pk/", "city": "Karachi"},
        {"name": "Omair Sana Foundation", "address": "R212, BLOCK 8, CORPORATE HOUSING SOCITY, SHAHRAH-E-JAHANGIR RD KARACHI",
                 "contact": "+92-21-36330094", "website": "http://omairsana.com/", "city": "Karachi"},
        {"name": "Ali-Zaib Blood Transfusion Centre Faisalabad", "address": "Inside General Hospital, Ghulam Muhammad Abad, Faisalabad",
            "contact": "+92-41-8722090", "website": "https://www.alizaibfoundation.org", "city": "Faisalabad"},
        {"name": "Fatimid Foundation Hyderabad Centre", "address": "Red Cresent B meeran Shah Road Near Dialdas Club Hyderabad",
            "contact": "+92-22-2728241", "website": "", "city": "Hyderabad"},
        {"name": "Pakistan Thalassemia Center Islamabad", "address": "F-9 Park, Islamabad",
            "contact": "+92-51-2324241", "website": "", "city": "Islamabad"},
        {"name": "Ali-Zaib Blood Transfusion Centre Faisalabad", "address": "G-8 Markaz, Islamabad",
            "contact": "+92-310-0002273", "website": "http://www.pims.gov.pk/", "city": "Islamabad"},
        {"name": "Fatimid Foundation Lahore Center", "address": "72-A, Blok D-II, Johar Town, Lahore",
            "contact": "+92-42-35210834-6", "website": "https://www.fatimid.org", "city": "Lahore"},
        {"name": "Thalassaemia Center, Safe Blood Bank & Hematological Services Multan", "address": "1967 Aqsa Street HazoorBagh Road, Multan",
            "contact": "+92-300-6301473", "website": "", "city": "Multan"},
        {"name": "Ahsas Welfare Organization Peshawar", "address": "House# 1653 Mohalla Mulan Majeed, 1/S Hushtnagri Peshawar City",
            "contact": "+92-91-2565094", "website": "", "city": "Peshawar"},
        {"name": "Hepatitis & Thalassemi Care Organization", "address": "Bugti Bazar Rd, Sui, Dera Bugti, Balochistan",
            "contact": "+92-835-421095", "website": "", "city": "Dera Bugti"},
        {"name": "Sukkur Blood Bank & Hospital SBDDS", "address": "Eidgah Road, Near DIG Office, Sukkur",
                 "contact": "+92-71-5615375", "website": "", "city": "Sukkur"},
        {"name": "CMH Combined Military Hospital", "address": "CMH Rd, Rawalpindi",
                 "contact": "+92-51-9273426", "website": "", "city": "Rawalpindi"},
        {"name": "Thalassaemia Care Center BMCH Quetta", "address": "Bolan Medical Complex Hospital, Quetta",
                 "contact": "", "website": "https://www.facebook.com/Thalassaemia-Care-Center-BMCH-Quetta-1478540029045683/", "city": "Quetta"},


    ]
    if city:
        return [
            center for center in centers if center["city"].lower() == city.lower()
        ], "Here are some of the available centers in {}:".format(city)
    else:
        return [], "No available centers found in {}:".format(city)


class ActionQueryDatabase(Action):
    def name(self):
        return "action_query_database"

    def run(self, dispatcher, tracker, domain):
        city = tracker.get_slot("city") if tracker.get_slot(
            "city") else tracker.get_slot("GPE")
        results, message = get_centers(city=city)
        dispatcher.utter_message(message)
        for i, obj in enumerate(results):
            dispatcher.utter_message(str(
                i + 1) + " - " + obj["name"] + "\n" + "Address: " + obj["address"] + "\n" + "Contact: " + obj["contact"] + "\n" + "Website:" + obj["website"])
        return []
