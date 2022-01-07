import os

four_emotion=['Happy','Angry','Neutral','Sad']
file_name='./data/txt/afew_eval'
f = open(file_name+'.txt')
content = []
for line in f.readlines():
    content.append(line)
f.close()

print('content len',len(content))
print(content)
four_emo_content = []
for c in content:
    for emo in four_emotion:
        if emo in c:
            four_emo_content.append(c)
print('four emo content len',len(four_emo_content))
# save
with open(file_name+"_4emo.txt", "w") as output:
    for i in four_emo_content:
        output.write(i)
