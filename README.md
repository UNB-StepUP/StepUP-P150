# UNB StepUP P150

StepUP is a footstep database for gait analysis and recognition using underfoot pressure. The P150 dataset specifically provides underfoot pressure data for 150 participants in 16 different walking and footwear conditions.

This repository contains information and companion scripts for dataset. A comprehensive overview of the dataset and methodology is provided in [our paper](www.google.com).


# Collected Conditions

1. 150 Participants
1. Four footwear conditions per participant
  * BF - Barefoot
  * ST - Standard Shoe
  * P1 - Personal Shoe #1
  * P2 - Personal Shoe #2
1. Three 30-second stationary balance trials, while standing on:
  * S1 - both feet
  * S2 - left foot only (todo confirm)
  * S3 - right foot only (todo confirm)
1. Four 90-second walking trials, completed at the following speeds:
  * W1 - Self-Paced
  * W2 - Slow-to-Stop
  * W3 - Slow
  * W4 - Fast


# Data Format and Folder Structure

Data is provided in two formats: 

1. `.npz` - provided in the `py` folder, and intended for python users.
1. `.mat` - pprovided in the `mat` folder, and intended for matlab users. 

Both formats of the dataset follow the same uniform folder structre. Data is organized into heirarchical folders by experiment trial as follows:

```
stepUP-P150/py/<participant-id>/<footwear-condition>/<walking-speed>/
```

# Data Files

** For simplicity, this section references datafile extensions using the `.npz` file extension. Replace this with the `.mat` extension when working in matlab.

## Standing Balance Trials
Two files are provided for each 30-second standing balance trial:

1. `trial.npz` - The full tile-grid recording (i.e., 30-seconds x 720px x 240px)
1. `preprocessed.npz` - A cropped recording, with all activity centered in a 180x180px region (i.e., 30-seconds x 180px x 180px)

## Walking Trials
Four files are provided for each 90-second walking trial:

1. `metadata.csv` -
1. `trial.npz` -
1. `pipeline_1.npz` -
1. `pipeline_2.npz` -  


# Downloading and Extracting the Dataset

The P150 dataset can be downloaded from [figshare](www.google.com).

To reduce total dataset size, each participant folder is provided as a compresed zipfile. These folders can be extracted separately using the standard zipfile tools built into Windows, Linux, and OsX. For convenience, the following code snippets can be used to extract them all at once. Run the following commands in a terminal window from the `steUP-P150/py` or `stepUP-P150/mat` folders to extract the `numpy` and `matlab` records respectively.

## Linux and OsX
```bash
for f in `ls`; do unzip -v $f; done
```

## Windows (todo, confirm that this actually works)
```powershell
Get-ChildItem | ForEach-Object { 
    if ($_ -is [System.IO.FileInfo]) {
        & "unzip" "-v" $_.Name
    }
}
```

# Using the Code Provided in the Repository

This repository provides utilities and examples for working with the python version of the dataset.


## Install Dependencies

After cloning the repository, run the following command from the top-level project folder:

```bash
pip install -r './requirements.txt'
```

## Example Usage

Examples of loading, manipulating, and working with the dataset are provided in `Examples.ipynb`. For convenience and use in your own code, common operations are provided in the `utils.py` file.

