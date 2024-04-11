import imageio
import sys
import time

video_file = sys.argv[1]
reader = imageio.get_reader(video_file)
fps=reader.get_meta_data()['fps']

# target fps 
target_fps=1
per=str(int(target_fps*fps))

with open('config/rate_file.txt', 'w') as wf:
    wf.write(per)