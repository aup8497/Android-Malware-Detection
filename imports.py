import gzip
import pandas as pd
import scipy as sp
from numpy.random import seed
import numpy as np
import pickle
from sklearn.feature_selection import mutual_info_classif as mic
import glob
from androguard.misc import *
from datetime import datetime as dt
import h5py
import math


LOAD_DATA = True       # Bool to decide whether to load data dictionaries previously pickled.
MAKE_DICT = False        # Bool to decide whether to pre process the whole raw data and create the data dicts
LOAD_FEATS = True      # Bool to decide whether to load previously calculated feature set.
LOAD_MODEL = False     # Bool to decide whether to train the model again or not.

###########################################################################################################

MAX_DATA = 1000         # The total count of APKs to be processed to extract feature space. Basically no. of
                        # datapoints to be considered.

DATASET_PATH = "Dataset/"
TEST_DATASET_PATH = "testAPKs/testAPK-1/"

##########################################################################################################
