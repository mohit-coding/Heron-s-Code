import math
import subprocess
import random
import pyttsx3
# import PyInstaller
import os
import wikipedia
import webbrowser
import pywintypes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# engine.setProperty('voices' ,voices[0].id)
engine.setProperty('rate', 135)
speak = engine.say


print("Here we will find the area of triangle using heron's formula")
speak("Here we will find the area of triangle using heron's formula")
engine.runAndWait()
speak("Input side a")
engine.runAndWait()
a = int(input("Input Side a => " ))
speak("Input side b")
engine.runAndWait()
b = int(input("Input side b => " ))
speak("Input side c")
engine.runAndWait()
c = int(input("Input side c => " ))
engine.runAndWait()
print("Now finding Semi Perimeter of the triangle")
speak("Now finding Semi perimeter of the triangle")
engine.runAndWait()

print("S = (a + b + c) / 2")
print("S = ")
S = (a + b + c) // 2
print(S)

print("Now, apply heron's Formula")
speak("Now, apply Heron's Formula")
engine.runAndWait()
print("Area of triangle = √(S(S-a)(S-b)(S-c))")
t = ((S-a)*(S-b)*(S-c))
total = (t * S)
print(math.sqrt(total))