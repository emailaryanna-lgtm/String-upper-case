# Write a program to create a class IOString which consists of a constructor that
#  gives a default value to variable str1. Next up create a method that gets a 
# string as input from the user. Create another method that will print the string 
# in the upper case. Next up create an object and call methods to get everything 
# implemented.
class Word:
    def __init__(self,word):
        self.word=word
    def display(self):
        print (self.word.upper())
w=Word("hello")
w.display()