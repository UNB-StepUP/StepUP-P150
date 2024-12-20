import pathlib
import numpy as np
import pandas as pd

dataset_folder = pathlib.Path('/home/shared/stepUP-P150')


participant_ids = range(1, 151)
footwears = ['BF', 'ST', 'P1', 'P2']
speeds = ['W1', 'W2', 'W3', 'W4']

standing_speeds = ['S1', 'S2', 'S3']




def load_metadata(participant_id, footwear, speed):
  f = dataset_folder / f'{participant_id:03}' / footwear / speed / 'metadata.csv'
  return pd.read_csv(f)


def load_trial(participant_id, footwear, speed):
  f = dataset_folder / f'{participant_id:03}' / footwear / speed / 'trial.npz'
  return np.load(f)['arr_0']


def load_footsteps(participant_id, footwear, speed):
  f = dataset_folder / f'{participant_id:03}' / footwear / speed / 'XXXXX.npz'
  return np.load(f)['arr_0']


def create_trial_iterator(include_standing_trials=False):
  included_speeds = speeds.copy()
  if include_standing_trials:
    included_speeds.extend(standing_speeds)
  
  for p in participant_ids:
    for f in footwears:
      for s in included_speeds:
        yield (p, f, s)

