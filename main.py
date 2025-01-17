import requests
from datetime import datetime

today = datetime.now()
DATE = today.strftime("%d/%m/%Y")
TIME = today.strftime("%I:%M:%S %p")

GENDER = "gender"
WEIGHT_KG = weight
HEIGHT_CM = height
AGE = age

# can be obtained on Nutriotionix (see exercise_endpoint)
APP_ID = "your id" 
API_KEY = "your api key"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

sheet_endpoint = "https://api.sheety.co/cb5d240270de9e91d13605b022ace18c/workoutTracker/workouts" # the sheet needs to be created first on sheety then copy the url
USERNAME = "username"
PASSWORD = "password"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_text = input("Which exercises did you do today? ")

user_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=user_params, headers=headers)
result = response.json()

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": DATE,
            "time": TIME,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, auth=(USERNAME, PASSWORD))
    print(sheet_response.text) 
