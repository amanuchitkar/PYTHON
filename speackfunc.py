from win32com.client import Dispatch


def Speak(a):
    speak = Dispatch("SAPI.SPVoice")
    speak.Speak(a)


Speak(
    """Raised when the interpreter finds an internal error, but the situation does not look so serious to cause it to abandon all hope. The associated value is a string indicating what went wrong (in low-level terms).

You should report this to the author or maintainer of your Python interpreter. Be sure to report the version of the Python interpreter (sys.version; it is also printed at the start of an interactive Python session), the exact error message (the exception’s associated value) and if possible the source of the program that triggered the error."""
)
