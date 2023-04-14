# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Optional

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
)
from rasa_sdk.types import DomainDict

import json
import requests
import re
import jsonpath


class ValidateFormEnforceYesOrNo(FormValidationAction):
    def name(self) -> Text:
        return "validate_form_enforce_yes_or_no"

    # async def extract_is_someone(
    #     self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    # ) -> Dict[Text, Any]:
    #     is_someone = tracker.get_slot('is_someone')
    #     # 此处很重要，在Rasa3.x里面，Rasa不能够循环问槽，此处必须返回，才能循环问，但是引入的另一个问题是无法打断form
    #     return  {"is_someone": is_someone}

class ActionAskIsSomeone(Action):
    def name(self) -> Text:
        return "action_ask_is_someone"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:

        requested_slot = tracker.get_slot("requested_slot")
        print(f'requested_slot: {requested_slot}')

        dispatcher.utter_message(text="请问您是XX先生/女士么？")

        return []


class PrintSlot(Action):
    def name(self) -> Text:
        return "print_slot"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        # print (tracker.latest_message["entities"])
        # print (tracker.get_slot("is_someone"))
        print (tracker.slots)
        return []
