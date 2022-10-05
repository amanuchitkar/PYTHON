from pygame import mixer

mixer.init()
mixer.music.load("Healthy_pro_life/song/2.mp3")
mixer.music.set_volume(0.8)
mixer.music.play()
while True:
    print("<Enter P for pause>")
    print("<Enter S for resume>")
    print("<Enter E for exit>")
    print("<Enter R for reload>")
    user_inp = input(": ").upper()

    if user_inp.__eq__("P"):
        print("Music pause... ")
        mixer.music.pause()
    elif user_inp.__eq__("S"):
        print("Music resume... ")
        mixer.music.unpause()
    elif user_inp.__eq__("R"):
        print("Music resume... ")
        mixer.music.rewind()

    elif user_inp == "E":
        print("Music resume... ")
        mixer.music.stop()
        break
    else:
        print("Invalid input")
