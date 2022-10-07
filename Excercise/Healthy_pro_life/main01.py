import time
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

from pygame import mixer as m


def display(title, songName, mode, inp=None):
    print(title)
    m.init()
    m.music.load(songName)

    m.music.play()
    while True:
        if mode == "Eye" or mode == "Physical":
            inp = input(f"Have you done {mode} Exersice(Y or N): ").upper()
        elif mode == "Water":
            inp = input(f"Did you drink 250ml water(Y or N): ").upper()
        if inp == "Y" or inp == "YES":
            m.music.stop()
            f1 = open("log.txt", "a")
            f1.write(f"{title.replace('Do', 'Done')} at: {time.asctime()}\n")

            f1.close()
            break
        elif inp == "N" or inp == "NO":
            m.music.play()
            print(title)
            continue
        else:
            print("invalid input..!!")


# Do some physical Exersice
# print(display("Drink water", "song/water.mp3", "Water"))
time1 = time.strftime("%H:%M")
# print(time1)
try:
    eye_time = time.time()
    water_time = time.time()
    physical_time = time.time()
    while True:
        if "09:00" <= time1 <= "21:00":
            # print(time.asctime())
            time1 = time.strftime("%H:%M")
            if time.time() - eye_time >= 3600:
                title = "Do any eye Exersice"
                display(title, "song/eyes.mp3", "Eye")
                eye_time = time.time()

            elif time.time() - water_time >= 2400:
                title = "Drink water"
                display(title, "song/water.mp3", "Water")
                water_time = time.time()
            elif time.time() - physical_time >= 9000:
                title = "Do some physical exersice"
                display(title, "song/physical.mp3", "Physical")
                physical_time = time.time()
        else:
            print("You had a good day..")
            break
except KeyboardInterrupt:
    print("\nProgram stopped by user..!!")
