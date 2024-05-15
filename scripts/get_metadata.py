import imageio
import sys
import time

video_file = sys.argv[1] 
reader = imageio.get_reader(video_file)
fps=reader.get_meta_data()['fps']

# target fps 
target_fps=sys.argv[2]
if len(target_fps) < 1:
    target_fps = 1
target_fps = float(target_fps) 
per=str(int(fps/target_fps))

with open('config/rate_file.txt', 'w') as wf:
    wf.write(per)
