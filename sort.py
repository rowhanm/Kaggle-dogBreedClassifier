import os
from shutil import copy
from random import shuffle

input_directory = './Data/Input/'
raw_directory = input_directory + 'Raw/'
training_data_directory = input_directory + 'Train/'
validation_data_directory = input_directory + 'Validate/'

with open('./labels.csv') as f:
    for line in f:
        lineData = line.strip().split(',')
        if lineData[0] != 'id' and lineData[1] != 'breed':  # It was late at night when I came up with this bad code
            filePath = './Data/train/' + lineData[0] + '.jpg' # Thankfully all files are .jpg
            label = lineData[1]
            if not os.path.exists(input_directory + 'Raw/' + label):
                os.makedirs(input_directory + 'Raw/' + label)
            if not os.path.exists(training_data_directory + label):
                os.makedirs(training_data_directory + label)
            if not os.path.exists(validation_data_directory + label):
                os.makedirs(validation_data_directory + label)
            copy(filePath, raw_directory + label)



labels = os.listdir(input_directory + 'Train/')


for i in labels:
    print 'Processing ' + raw_directory + i + '...'
    data = os.listdir(raw_directory + i)
    shuffle(data)
    datalen = len(data)
    split_point = int(0.8*datalen)
    train = data[:split_point]
    validation = data[split_point:]
    print str(len(train)) + ' training samples.'
    print str(len(validation)) + ' validation samples.'
    for j in train:
        copy(raw_directory + i + '/' + j, training_data_directory + i)
    for j in validation:
        copy(raw_directory + i + '/' + j, validation_data_directory + i)
    print 'Done!'
