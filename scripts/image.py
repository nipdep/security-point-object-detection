
import os
import cv2
import numpy

point = 300

def img_resize(current_dir,save_dir,cat,size_x=413,size_y=413):
    img_list = os.listdir(current_dir)

    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    #os.chdir(save_dir)

    for name in img_list:
        print(name)
        img = cv2.imread(os.path.join(current_dir,name),1)
        #cv2.imshow('',img)
        res = cv2.resize(img, dsize=(size_x, size_y), interpolation=cv2.INTER_CUBIC)
        global point
        point+=1
        name = cat+str(point)+'.jpg'

        cv2.imwrite(os.path.join(save_dir,name),res)

    return res


res = img_resize("./last/common", "./new/common", "common")
