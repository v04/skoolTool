def data():
    import mysql.connector as sql
    conn = sql.connect(host="localhost", user="root", passwd="meme", database="skooltool")
    # asking for there data
    cur = conn.cursor()
    name = input("your good name please: ")
    grade = int(input("i assume you are in class(integer): "))
    school = input("you are student of school: ")
    q = "insert into info values('{}', {}, '{}')".format(name, grade, school)
    cur.execute(q)
    # collecting in database
    conn.commit()
    print("done")
    #calling name
    print("hello", name)

    from gtts import gTTS
    from playsound import playsound
    #this will convert my text into audio
    def convert(text):
        myaudio = gTTS(text)
        myaudio.save("hello name.mp3")
        myaudio1 = gTTS("hello")
        myaudio1.save("hello.mp3")
    convert(name)
    #volume up
    playsound("hello.mp3")
    playsound("hello name.mp3")

data()





