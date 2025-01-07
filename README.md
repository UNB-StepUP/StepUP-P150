# UNB StepUP P150

StepUP is a footstep database for gait analysis and recognition using underfoot pressure. The P150 dataset specifically provides underfoot pressure data for 150 participants in 16 different walking and footwear conditions.

This repository contains python code to support dataset use. The repository is designed for python version 3. A comprehensive overview of the dataset and methodology is provided in [our paper](www.google.com).


# Downloading the Dataset

The P150 dataset can be downloaded from [figshare](www.figshare.com). Although the dataset is provided in both `.npz` (i.e., python) and `.mat` (i.e., matlab) file formats, this repository documents python usage only. Therefore, ensure you download the "Python Dataset" from FigShare.

To reduce download size, the dataset is compressed in `.tar.xz` format with a separate compressed folder containing data for each participant. The full dataset can be downloaded by clicking the "Download All" button in FigShare (see below). The dataset can be extracted manually, or using the automated script provided in this repository (see "Unzip the Downloaded Dataset", below).


# Using the Repository

This repository provides python source code for working with the dataset. For example, basic functions for loading dataset records are provided in `utils.py`. Further, example usage is documented in the `Examples.ipynb` notebook.

**Importantly, you _must_ complete the following three (3) steps** for the code in this repository to function correctly.


## Step 1: Install Software Dependencies

Dependencies are documented in the `requirements.txt` file. Install them with the following command:

```bash
pip install -r requirements.txt
```

## Unzip the Downloaded Dataset

To minimize download requirements, the dataset has been compressed in `.tar.xz` format. The `extract_dataset.py` automates the dataset extraction process. Run the following command to extract the dataset:

```bash
python extract_dataset.py path/to/downloaded/dataset
```


## Configure the `DATASET_PATH` variable

This repository contains python functions for loading data records. To function correctly, the `DATASET_PATH` variable on line X of `utils.py` must be updated to reflect the file system location of the dataset in your development environment.

```python
# Update for your local environment
DATASET_PATH = '/path/to/dataset/root/folder'
```


# Data Records

## Walking Trials

Each participant completed a series of sixteen 90-second walking trials (i.e., 4 footwear conditions X 4 walking behaviors). The following data files are provided for each walking trial. Example python code for loading data files is provided in `utils.py`

1. `metadata.csv` - information about each footstep that occurred in the 90-second trial. A full description of metadata fields is provided in Table X of [our paper](www.google.com).

1. `trial.npz` -  a numpy array of the full trial recording with shape: (90,000 frames X 720px X 240px)

1. `pipeline_1.npz` - a numpy array of extracted footsteps preprocessed using *pipeline #1* (documented in [our paper](www.google.com)) with shape: (n_footsteps X 101 frames X 75px X 40px)

1. `pipeline_2.npz` - a numpy array of extracted footsteps preprocessed using *pipeline #2* (documented in [our paper](www.google.com)) with shape: (n_footsteps X 101 frames X 75px X 40px)


## Standing Balance Trials

Additionally, participants completed twelve 30-second standing balance trials (i.e., left-, right-, and two-foot balance; performed with each of the 4 footwear conditions). The following data files are provided for each standing trial. Example python code for loading data files is provided in `utils.py`

1. `trial.npz` - a numpy array of the full trial recording, with shape: (30,000 frames X 720px X 240px)
1. `preprocessed.npz` - a numpy array spatially cropped around the participant, with shape: (30,000 frames X 180px X 180px)




# Example Usage

Although the dataset was collected through the lens of gait biometrics, we anticipate that it will be valuable for a wide range of research topics. Usage examples are provided in the `Examples.ipynb` jupyter notebook.


# Citing this Dataset

```bibtex
TODO: Codeblock for citation
```
