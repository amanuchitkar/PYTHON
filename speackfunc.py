from win32com.client import Dispatch


def Speak(a):
    speak = Dispatch("SAPI.SPVoice")
    speak.Speak(a)


Speak("""am figuring out the differences between the pickle.load() and pickle.loads(). Somebody said what kind of 
object that pickle.load() process is "file_like_object", however, pickle.loads() corresponds to "file object".""" )
