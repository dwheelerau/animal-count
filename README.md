# Animal counter

## Introduction  
Simple animal counter app based on the
open source package [labelme](https://github.com/labelmeai/labelme.git).  

This should work pre/post SOE on windows systems. The individual bash scripts should work on POX
  

Splits a MP4 video into frames and allows users to draw boundary boxes around 
animals and apply a species label. On program close a CSV file of species counts is provided. 

## install
1. Install Anaconda through the MS software center
    - uncheck any options for a desktop icon, but accept options for a shortcut in the menu   
    - Note: The software center will report that the install failed, ignore this message,
instead check for the `Anaconda` shortcut options in the menu.   
    - if you are using a non-soe computer used this link [Anaconda](https://www.anaconda.com/download)  
    - If the above failed see the section on using Miniconda  

2. Install `git` through teh software center (this will add bash tools)  
3. Activate conda via a `conda powershell terminal` avaiable through `Anaconda navigator shortcut`)
4. Run the following code (copy line by line) that will create a new environment to install dependencies.  

```
conda create --name=labelme python=3
conda activate labelme
pip install labelme
```

5. Download the scripts directory from the [repo]()

6. Open this new directory, and copy the MP4 video to the `video-to-proc` folder.  
    - Custom labels can be added via creating a text file called `labels.txt`
in the `config` directory. This file should consist of one species per row. These
can also be added latter manually using the labelme GUI.    


## Outputs  
A single spreadsheet containing the list of animals and there counts will be saved to the
base directory, with the filename being the video name + a time stamp.  

## Using miniconda instead of Anaconda  
 For a minimal install you could use 
[miniconda](https://docs.anaconda.com/free/miniconda/miniconda-install/),
which can be installed anywhere where you have non-admin write access (ie 
Documents/programs or where ever you like). 

There is a hard coded path in `duck-counter.bat`, this may need to be modified. 
If using anaconda from the software center, the required path (FYI) is
`C:\ProgramData\Anaconda3\Scripts\activate.bat`. If using miniconda install script,
the path will be: `<where_you_installed/Scripts/activate.bat`.
or call the `conda.exe` directly from
the `Scripts` directory where you installed `miniconda`. The following commands
are required to install the env (called `labelme`).  

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
`scripts/get_metadata.py` file to adjust.  

## options  
- `FPS` split can be adjusted as described above
- `config/labels.txt` allows custom labels at startup (optional)  

