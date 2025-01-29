import matplotlib.pyplot as plt
import math


# Plot a grid of P100 images, row-major ordering.
# Plot height and width are assigned reasonable defaults when left unspecified
# Individual plot titles can be created by specifying a metadata df and title string template (passed to str.format)

def plot_p100s(p100s, n_cols=15, width=None, height=None, metadata=None, title_str='{ParticipantID} {Footwear} {Speed} {FootstepID} {RScore:.2}'):

  n_rows = math.ceil(p100s.shape[0]/n_cols)

  if not width:
    width = 2.5 * n_cols

  if not height:
    height = 4 * n_rows

  fig, axes = plt.subplots(ncols=n_cols, nrows=n_rows, figsize=(width, height))

  for i, p100 in enumerate(p100s):
    r = i % n_cols
    c = i // n_cols

    axes[c, r].imshow(p100, norm='log')

    if metadata is not None:
      kw_args = metadata.iloc[i].to_dict()
      axes[c, r].set_title(title_str.format(**kw_args))

  return fig, axes