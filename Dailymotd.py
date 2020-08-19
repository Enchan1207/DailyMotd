#
# /etc/motdの中身を日替わりで書き換える
#

def main():
    writeMotd(getMessage())

def getMessage():
    return "SSHログインユーザやったら、ちゃんとメモ取ってな画面の前でお前、俺喋ってることを！\nいいか?\n\nマ ン ダ の り ゅ う せ い ぐ ん は つ よ い"

def writeMotd(message = ""):
    with open("/etc/motd", mode = 'w') as f:
        f.write("\n" + message + "\n\n")

main()

