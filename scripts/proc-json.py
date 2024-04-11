#!/usr/bin/env python
import csv
from datetime import datetime
import json

from os import listdir, getcwd
from os.path import isfile, join, basename
import sys

def cal_timestamp(pathstring):
    # use filename string to calculate timestamp based on 100ms
    #todo
    #00000000.jpg
    #00000100.jpg
    #00000200.jpg
    return ""

video_file = sys.argv[1]

mywd = getcwd()
json_path = join(mywd, "video-to-proc", "json")

# get a list of files from the json directory
onlyfiles = [f for f in listdir(json_path) 
             if isfile(join(json_path, f))]

animal_count = {}

for fname in onlyfiles:
    fname_path = join(json_path, fname)
    with open(fname_path, 'r') as rf:
        data = json.load(rf)
        samples = data['shapes']
        for sample in samples:
            animal = sample['label']
            # could save filepaths here as well for time-stamp-ish obj
            if animal in animal_count:
                animal_count[animal][0]+=1
                if fname not in animal_count[animal][1]:
                    animal_count[animal][1].append(fname)
            else:
                animal_count[animal] = [1, [fname]]

timestr = datetime.now().strftime("%Y_%m_%d-%H_%M")
outfile = "%s.%s.csv"%(video_file, timestr)
outfile_h = basename(outfile)

with open(outfile_h, 'w', newline='') as wf:
    csv_writer = csv.writer(wf)
    csv_writer.writerow(['animal','count'])
    for animal in animal_count:
        count = animal_count[animal][0]
        csv_writer.writerow([animal, count])
print('wrote final counts to the directory %s with the filename %s' % ("video-to-proc",outfile))
print('program will now close!')