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


def iter_trials():
  for p in range(1, 151):
    for f in 'BF ST P1 P2'.split():
      for s in 'W1 W2 W3 W4'.split():
        yield p, f, s



cache_root = pathlib.Path('/home/aaron/stepUP-150-cache')

def generate_p100_cache():
  for p, f, s in iter_trials():
    for pipeline in [1, 2]:

      print(p, f, s, pipeline)

      footsteps = load_footsteps(p, f, s, pipeline)
      p100s = footsteps.sum(axis=1)

      dest = cache_root / f'p100/{p}/{f}/{s}/pipeline_{pipeline}.npz'
      dest.parent.mkdir(parents=True, exist_ok=True)

      np.savez(dest, arr_0=p100s)

def load_cached_p100s(participant_id, footwear, speed, pipeline=1):
  f = cache_root / f'p100/{participant_id}/{footwear}/{speed}/pipeline_{pipeline}.npz'        
  return np.load(f)['arr_0']


def generate_grf_cache():
  for p, f, s in iter_trials():
    for pipeline in [1, 2]:

      print(p, f, s, pipeline)

      footsteps = load_footsteps(p, f, s, pipeline)
      grfs = footsteps.sum(axis=(2,3))

      dest = cache_root / f'grf/{p}/{f}/{s}/pipeline_{pipeline}.npz'
      dest.parent.mkdir(parents=True, exist_ok=True)

      np.savez(dest, arr_0=grfs)


def load_cached_grfs(participant_id, footwear, speed, pipeline=1):
  f = cache_root / f'grf/{participant_id}/{footwear}/{speed}/pipeline_{pipeline}.npz'        
  return np.load(f)['arr_0']

