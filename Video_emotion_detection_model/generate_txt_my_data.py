import os


res  = []

for f in os.listdir('./matched_face'):
    print(f)
    res.append(f+' Angry')
textfile = open("./txt/matched_face_inf.txt", "w")
for element in res:
    textfile. write(element + "\n")
textfile. close()