#realtimefirebase_2 ver.
#
#
# UPR _ module 2
from result_class import res3
from text_detection import td_single
import os

def get_image_paths():
    folder = '/Users/bonha/realtimefirebase_easypath/image'
    files = os.listdir(folder)
    files.sort()
    files = ['{}\\{}'.format(folder, file) for file in files]
    files.remove('/Users/bonha/realtimefirebase_easypath/image/.DS_Store')
    files.remove('/Users/bonha/realtimefirebase_easypath/image/img_data.npy')
    return files

def function2():
    mod2 = 200
    X_img_paths = res3.path
#    print(X_img_paths)

    mod2 = td_single(X_img_paths) #either 1 or 5
    if(mod2 == 5):
        res3.hasFigure = True
    print("                                      2. From module 2 =>"+str(res3.hasFigure))
