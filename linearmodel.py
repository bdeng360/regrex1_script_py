#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import sys
import matplotlib.pyplot as plt
import scipy as sci
import os.path
from scipy import stats

regrex = pd.read_csv(sys.argv[1])
print("loading {}".format(sys.argv[1]))

basename = os.path.splitext(sys.argv[1])
print(basename)

x = regrex.x
y = regrex.y

plt.plot(x, y, 'o')
plt.savefig("{}_scatter.png".format(basename[0]))
print("saving {}_scatter.png".format(basename[0]))

reg = stats.linregress(x, y)

plt.plot(x, y, 'o', label='scatter')
plt.plot(x, reg.intercept + reg.slope*x, 'b', label='lin fit')
plt.legend()
plt.savefig("{}_scatter_lin.png".format(basename[0]))
print("saving {}_scatter_lin.png".format(basename[0]))

print("done")