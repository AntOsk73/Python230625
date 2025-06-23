def check_weather():
    while True:
        weather = input("How's the weather today? (hot/cold/rainy): ").lower()

        if weather == "hot":
            print("Don't forget to drink some water, and hydrate yourself.")
        elif weather == "cold":
            print("Stay warm and cozy!")
        elif weather == "rainy":
            print("Take an umbrella with you—stay dry!")
        else:
            print("Sorry, didn’t get your answer. Please try again.")

# Start the app
check_weather()
