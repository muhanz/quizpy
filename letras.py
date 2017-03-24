# Muhan Zhang
# Letras a Flashcards
# Hecho Con Amor en Miami, FL

from quizpy import *
from translation import bing

source_lines = list(filter(bool, (open("letras/"+input("Please enter the name of the file, with the suffix: "), "r").readlines())))
scrubbed_lines = [line for line in source_lines if line!="\n"]
dest_lines = []
name = input("Give this set a name: ")

for line in scrubbed_lines:
    try:
        dest_lines.append(bing(line, dst='en'))
    except: 
        print ("Failing quietly")
    # print (line)

print (create_set(name, scrubbed_lines, "es", dest_lines, "en").text)


