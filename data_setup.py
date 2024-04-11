import numpy as np
import matplotlib.pyplot as plt
import csv
import PIL
import os
from DetectFace import DetectFace

path_gender_csv = None
with open('merged_data.csv') as file:
    reader = csv.reader(file)
    path_gender_csv = list(reader)

print(path_gender_csv[:10])

train_data = []
test_data = []

unvalid_paths = []

for file_path, gender in path_gender_csv:
    if gender == 'NaN':
        continue
    # merge directory
    file_path = os.path.join('wiki_crop', file_path)

    # replace slash with os specific separator
    file_path = file_path.replace('/', os.sep)

    # print(file_path)

    if os.path.exists(file_path):
        # open as grayscale
        img = PIL.Image.open(file_path)

        if not DetectFace(img):
            unvalid_paths.append(file_path)
            continue

        img = img.convert('L')

        # if pixel size is 1x1, skip
        if img.size[0] == 1 and img.size[1] == 1:
            continue

        # resize to 128x128
        img = img.resize((128, 128))

        # convert to numpy array
        img = np.array(img)

        # plot image with gender
        # plt.imshow(img, cmap='gray')
        # gender_title = "female" if gender == '0' else "male"
        # plt.title(gender_title)
        # plt.show()

        # append to list
        train_data.append(img)
        test_data.append(0 if gender == '0' else 1)

# convert to numpy array
train_data = np.array(train_data)
test_data = np.array(test_data)

# save to file
np.save('train_data.npy', train_data)
np.save('test_data.npy', test_data)

# save unvalid paths to file
print("found", len(unvalid_paths), "unvalid images")
with open('unvalid_paths.txt', 'w') as file:
    for path in unvalid_paths:
        file.write(path + '\n')
