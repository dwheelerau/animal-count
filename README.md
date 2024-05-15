# Animal counter app for the VPRU  

## Introduction  
Simple animal counter app based on the
open source package [labelme](https://github.com/labelmeai/labelme.git).  

The program splits a MP4 video into individual frames and allows the user
to annoate animals with labels. After the program closes a CSV file is created
that contains the counts of each animal type.  

This should work pre/post SOE on windows systems. The individual bash scripts should work on POSIX,
with minor modification. A conda env file is provided for easy clonning using conda.    

## Running the software  
1. Copy the video you wish to process into the `video-to-proc` folder (make sure only
   one video is found in this folder).  
2. Double click on the `duck-counter.bat` file (several terminal windows will open)
3. The GUI should open, select menu option [Edit]->[Create rectangle]
4. Draw a box around the object using the mouse and add the label
5. Use the back and forward buttons to move through frames
6. When you are finished annotating, just close the program
7. A CSV file named after the video file will contain a summary of the counts.

## Troubleshooting  
- Dont include spaces in filenames, use underscores instead "_"!
- The video needs to have the file extension .MP4 or .mp4

## install
1. Install Anaconda through the MS software center, **ignore the 'install failed message'** \-:
    
Check that there is a new "start menu" folder called the `Anaconda`.   
    - if you are using a non-soe computer use this link [Anaconda](https://www.anaconda.com/download)  

2. Install `git` through the software center (this will add the required bash tools)  
3. Open a `Anaconda powershell terminal` avaiable through `Anaconda` folder shortcut in the start menu   
4. Run the following code (copy line by line and press ENTER after each line),
   this will create a new isolated python environment to install all dependencies.   

```
conda create --name=labelme python=3
conda activate labelme
pip install labelme
pip install video-cli
pip install imageio-ffmpeg
```
5. Download the scripts from this repo (ie this webpage) by clicking the green `code` button and selecting 'zip' file
6. Unzip the folder to your desktop
7. Open this new directory, and copy the MP4 video to the `video-to-proc` folder.
8. Follow the instructions above to run the software  

## Outputs  
A single spreadsheet containing the list of animals and there counts will be saved to the
base directory, with the filename being the video name + a time stamp.  

## Customisation  
### Modifying the number of individual image frames generated from a single video
Modify the number in the file `config/target_fps.txt`. For 1 frame per second just add the number
1 to this file. For 2 frames per second add 2, etc. To reduce the temnporal resolution you can
use 0.5, which will create 1 framer per 2 seconds of video.  

### Custom animal labels
One off custom labels can be added via the GUI (draw the polygon and add it to the free form text window),
or for persistant labels add the name to the bottom of the `config/labels.txt` file (on its own line). Save
the file and this label will appear as an option when the program is started.  

## Using miniconda instead of Anaconda (more advanced)  
For a minimal install you could use 
[miniconda](https://docs.anaconda.com/free/miniconda/miniconda-install/),
which can be installed anywhere where you have non-admin write access (ie 
Documents/programs or where ever you like). 

There is a hard coded path in `animal-counter.bat`, these may need to be modified. 
If using anaconda from the software center, the required path (FYI) is
`C:\ProgramData\Anaconda3\Scripts\activate.bat`. If using miniconda install script,
the path will be: `<where_you_installed/Scripts/activate.bat`.
or call the `conda.exe` directly from
the `Scripts` directory where you installed `miniconda`. The following commands
are required to install the env (called `labelme`). Use this latter command
to install the environment from a terminal window using the following code.     

```
conda create --name=labelme python=3
conda activate labelme
pip install labelme
```

## The files  
A description of the files is below.

| filename  | Desc.  |
|---|---|
| `scripts/animal-counter.bat`  | a batch file that executes the shell and python code in windows  |
| `scripts/animal-counter-win.sh`  | bash script that executes `video-toimg`  |
| `scripts/proc-json.py`  | python script that converts json annotation files to animal counts in CSV format |
| `scripts/get_metadata.py`  | python script that calculates the parameters required for 1 FPS |
| `config/labels.txt`  | Optional duck labels that can be imported at app startup  |
| `env/labelme-env-win64.yml`  | a conda env file that can be used to clone this environment  |

The default video splitting is 1 FPS, if this is too little or too much, see the comment in the
`scripts/get_metadata.py` file to adjust. A smaller FPS results in less images to annotate, but may
leed to missed animals that fall between frames.   

## Historical notes about the per value (ignore as not used)  
The number of single frame images that 
are created can be adjusted by modifying the number in the file `config/rate_file.txt`. This number
is called the `per` value. To adjust this value you need to know the FPS (Frames per second) of your 
video. To find this information right click on the file, click [properties] and [details]. Once you know
the FPS value, the equation to set the per value is = FPS/(required frames per scond). So if the
FPS value is listed as 29, then setting the number in `config/rate_file.txt` to 29 will create  1 frame
per second of video footage. For more temporal resolution, you may want (for example) 2 frames 
per second. For 2 frames per second set the `config/rate_file.txt` number to 29/2=14. Note 
increasing the number of frames will make require more processing time. Likewise to get 1 frame per 2 second
of video, the formulia would be 29/0.5=58, so use 58 in the `config/rate_file.txt` file.  

## options  
- `FPS` split can be adjusted as described above
- `config/labels.txt` allows custom labels at startup (optional)  

