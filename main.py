#
# /etc/motdの中身を日替わりで書き換える
#
import random

def main():
    writeMotd(getMessage("motds.txt"))

def getMessage(filepath):
    motds = ["Hello! Sorry, you set invalid filepath parameter or no content in %s."%filepath, ]
    with open(filepath, mode = 'r') as f:
        lines = f.readlines()
        if(len(lines)>0):
            motds = lines

    return random.choice(motds)

def writeMotd(message = ""):
    with open("/etc/motd", mode = 'w') as f:
        f.write("\n" + message + "\n\n")

main()

