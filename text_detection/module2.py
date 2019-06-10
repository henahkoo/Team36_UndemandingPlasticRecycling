from text_detection import td_single
import os

def get_image_paths():
    folder = '/Users/bonha/realtimefirebase/images/bottle/notext'
    files = os.listdir(folder)
    files.sort()
    files = ['{}/{}'.format(folder, file) for file in files]
    files.remove('/Users/bonha/realtimefirebase/images/bottle/notext/.DS_Store')
    return files

X_img_paths = get_image_paths()
print(X_img_paths)

for filename in X_img_paths:
    print(filename)
    result = td_single(filename) #either 1 or 5

print("detection finished")


