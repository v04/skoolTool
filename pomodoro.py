import time
from playsound import playsound
print("********************************Q. WHAT IS THE POMODORO TECHNIQUE?******************************** ")
print("$ A time management method developed by franceso cirillo in late 1980s,\n"
      "uses a timer to break down work into intervals traditionally 25minutes in length separated by short breaks")
print("lets see what are the steps: \n"
      "step 1 - choose the task \n"
      "step 2 - set a timer for 25 mins or maybe 50 mins if you want \n"
      "step 3 - work on the task until timer BEEPS* \n"
      "step 4 - take a short break of 5mins for 25mins and 10mins break for 50mins \n"
      "step 5 - repeat the cycle 4times take a longer break after 4 sissions")


start = input("start timer? y/n ")
#a intro audio will be played before timer starts
playsound("pomo intro.mp3")

if start == "y":
    from turtle import *
    setup()
    t1 = Turtle()
    tr = Turtle()
    wn = Screen()

    for i in range(4):
        t = 4
        t1.clear()
        while t:
            t1.clear()
            wn.bgpic("Pomodoro-Technique-for-Studying.gif")
            mins, secs = divmod(t, 60)
            t1.write(str(mins).zfill(2) + ":" + str(secs).zfill(2), font=("sans", 40, "bold"), align="center")
            t -= 1
            time.sleep(1)
        print("BREAK")
        print("starting timer for 5 min break ")
#audio will be played before timer goes off
        playsound("break-start sound.mp3")
        t = 5
        while t:
            t1.clear()
            wn.bgpic("pomodorobreak.gif")
            mins, secs = divmod(t, 60)
            t1.write(str(mins).zfill(2) + ":" + str(secs).zfill(2), font=("", 50, "normal"), align="center")
            t -= 1
            time.sleep(1)
        print("next session")
        print("START")
        playsound("break-start sound.mp3")
print("looks like someone made it!!")
#goodnight



























