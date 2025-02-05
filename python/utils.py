import pathlib
import numpy as np
import pandas as pd

dataset_folder = pathlib.Path('/home/shared/stepUP-P150/py') # path to local data folder


def load_metadata(participant_id, footwear, speed):
  f = dataset_folder / f'{participant_id:03}' / footwear / speed / 'metadata.csv'
  return pd.read_csv(f)


def load_trial(participant_id, footwear, speed):
  f = dataset_folder / f'{participant_id:03}' / footwear / speed / 'trial.npz'        
  return np.load(f)['arr_0']


def load_footsteps(participant_id, footwear, speed, pipeline = 1):
  f = dataset_folder / f'{participant_id:03}' / footwear / speed / f'pipeline_{pipeline}.npz'
  return np.load(f)['arr_0']

def load_processed_standing(participant_id, footwear, trial):
  f = dataset_folder / f'{participant_id:03}' / footwear / trial / 'preprocessed.npz'
  return np.load(f)['arr_0']
