import sys
import os


def get_image_paths():
    folder = '/Users/bonha/realtimefirebase/images/white'
    files = os.listdir(folder)
    files.sort()
    files = ['{}/{}'.format(folder, file) for file in files]
#    files.remove('/Users/bonha/realtimefirebase/images/white_test/.DS_Store')
#    files.remove('/Users/bonha/realtimefirebase/images/0512test/test2/img_data.npy')
    return files

X_img_paths = get_image_paths()

for filename in X_img_paths:
    os.system('python3 test_white.py -i '+str(filename))
