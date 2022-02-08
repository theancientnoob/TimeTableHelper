from datetime import date

Monday = ["Acp, Maths, Chemistry, Hindi"]
Tuesday = ["Physics, Hindi, Maths, AI"]
Wednesday = ["Social, Maths, English, Science(Rotation)"]
Thursday = ["Biology, AI, English, Social"]
Friday = ["Hindi, Lib/WE/PT, Social, English"]
Saturday = ["Maths, Social, Hindi, English"]

today = date.today()
d1 = today.strftime("%A")

if d1 == "Monday":
    print(Monday)

if d1 == "Tuesday":
    print(Tuesday)

if d1 == "Wednesday":
    print(Wednesday)

if d1 == "Thursday":
    print(Thursday)

if d1 == "Friday":
    print(Friday)

if d1 == "Saturday":
    print(Saturday)

if d1 == "Sunday":
    print("Its sunday tf you doin")

