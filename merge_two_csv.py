import sys
from StringIO import StringIO
import pandas as pd

list1 = pd.read_csv(TESTDATA, sep=";")

list2 = pd.read_csv(TESTDATA, sep=";")

common = pd.merge(list1, list2, how='left', left_on=['name', 'class'], right_on=['name', 'class']).dropna()

