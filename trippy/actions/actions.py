# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import mysql.connector
from mysql.connector import Error

class ActionHelloWorld(Action):

    """def create_connection(host_name, user_name, user_password, db_name):
        connection = None
        try:
            connection = mysql.connector.connect(
				host=host_name,
				user=user_name,
				passwd=user_password,
				database=db_name
			)
            print("Connection to MySQL DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")
        return connection"""    
    
    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #connection = create_connection("localhost", "root", "", "bits")
        connection = mysql.connector.connect(
				host="localhost",
				user="root",
				passwd="",
				database="bits"
			)
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM resturant")
            name = cursor.fetchall()
            print("exceuted successfully")
            msg = 'Hello {}!'.format(name)
            dispatcher.utter_message(msg)
        except Error as e:
            print(f"The error '{e}' occurred")

        return []



