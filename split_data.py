# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 14:49:41 2021

@author: Aisling
"""

import pandas as pd
#import numpy as np
from sklearn.model_selection import train_test_split
import os
import shutil

# Read csv content into dataframe
df = pd.read_csv('train.csv')

# Split into training and test data 85/15
train_df, test_df = train_test_split(df, test_size=0.15, random_state=0)

# Get relevant columns
relevant_train = train_df[['image_name', 'benign_malignant', 'target']]
relevant_test = test_df[['image_name', 'benign_malignant', 'target']]

if os.path.exists('training.csv'):
    os.remove('training.csv')
if os.path.exists('testing.csv'):
    os.remove('testing.csv')

# Write to training and test csvs
relevant_train.to_csv('training.csv')
relevant_test.to_csv('testing.csv')

# Get images in testing csv file 
test_images = test_df['image_name'].tolist() 

input_directory = "lesion_images/"
train_output_directory = "training/"
test_output_directory = "testing/"

# Get list of images in source directory
file_names = os.listdir(input_directory)

# If output directories already exist, remove them
if os.path.exists(train_output_directory):
    shutil.rmtree(train_output_directory)
    
if os.path.exists(test_output_directory):
    shutil.rmtree(test_output_directory)

# Create them again
os.makedirs(train_output_directory)
os.makedirs(test_output_directory)
             
for file in file_names:
     # Remove .jpeg extension from image name
     file = file.replace('.jpg', '')
     
     found = False
     x = 0;
     
     while(not found and x < len(test_images)):
         test_images[x] = str(test_images[x])

         if(file == test_images[x]):
             shutil.move(input_directory + file + ".jpg", test_output_directory + file + ".jpg")
             found = True
         x+=1
             
         
training_file_names = os.listdir(input_directory)
for file in training_file_names:
    shutil.move(input_directory + file, train_output_directory + file)



