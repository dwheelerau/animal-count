#!/bin/bash

#source ~/mambaforge/etc/profile.d/conda.sh
#conda activate labelme
#conda -V

# directories
output="video-to-proc/json"
# cleanup
rm -rf $output

# folder paths etc
vid=$(ls video-to-proc/*mp4 video-to-proc/*MP4)
vid_out_dir=${vid%.*}
#cleanup 
rm -rf $vid_out_dir

# process video catch upper and lower case
target_fps=$(cat config/target_fps.txt)
echo "target FPS used is: " $target_fps
python scripts/get_metadata.py $vid $target_fps
# per = FPS of video / desired FPS
per_param=$(cat config/rate_file.txt)
echo "Using per value of: " $per_param
video-toimg --per $per_param $vid

# label
labelme --nodata --labels config/labels.txt --output $output --autosave $vid_out_dir

# count animals
python scripts/proc-json.py $vid
