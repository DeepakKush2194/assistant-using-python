import time
import pyttsx3
commands = ["Start music", "Open browser", "Check weather","Shutdown"]
user = input("Aapka naam kya h, sir?? ").capitalize()
print("Welcome, Mr.",user,"Main aapka personal assistant hoon.")
engine = pyttsx3.init()
engine.say("Welcome, Mr. " + user + ". Main aapka personal assistant hoon.")
engine.runAndWait()
#time.sleep(1)
print("Aap mujhe bol sakte hain:",', '.join(commands))
# for command in commands:
#     print(command)
while True:
    action = input("Command dijiye, sir: ").lower()
    if "music" in action:
        print("Music module activate ho raha hai, sir...")
    elif "browser" in action:
        print("Browser launch kar raha hoon...")
    elif "weather" in action:
        print("Fetching current weather update...")
    elif "shutdown" in action:
        print("System shutting down protocol initiate ho raha hai...")
        break
    else:
        print("Command not recognized, sir.")
        print("Aap mujhe bol sakte hain:", ', '.join(commands))