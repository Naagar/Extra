import os
import os
import random
from shutil import copyfile
import pandas as pd
import numpy as np
import csv

# specify the img directory path
path = "images"

# list files in img directory
files = os.listdir(path)
df_test= pd.DataFrame(columns=['name', 'class'])
img_count = 0
counter = 0
class_name = 1
for file in files:
    # make sure file is an image
    if file.endswith('.png'):
    	image_name = file 
    	counter += 1
    	df_test.loc[img_count] = file, class_name
    	img_count += 1
        


df_test.to_csv('images_data.csv') 

print('this much ' + str(counter) + ' added to list ' )
print('done')


# df_test.loc[img_count] = file, class_name
        # img_count += 1