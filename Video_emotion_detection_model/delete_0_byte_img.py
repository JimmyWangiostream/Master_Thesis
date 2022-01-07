import os


res  = []
root_path = './matched_face/'
for f in os.listdir(root_path):
    print(f ,'enter')
    if not os.listdir(root_path + f):
        #print(f,'is null')
        continue
    for img in os.listdir(root_path + f):
        if not os.path.getsize(root_path + f+'/'+img):
            print(img,'is 0 size')
            os.remove(root_path + f+'/'+img)