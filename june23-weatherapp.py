# Weather check app

# Ask the user about the weather
weather = input("How's the weather today? (hot/cold/rainy): ").lower()

# Respond based on the input
if weather == "hot":
    print("Don't forget to drink some water, and hydrate yourself.")
elif weather == "cold":
    print("Stay warm and cozy!")
elif weather == "rainy":
    print("Take an umbrella with you—stay dry!")
else:
    print("Sorry, didn’t get your answer, please try again.")
