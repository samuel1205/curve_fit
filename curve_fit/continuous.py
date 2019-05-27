# -*- coding: utf-8 -*-
# @Project : curve_fit
# @Time    : 2019-05-27 14:51
# @Author  : Samuel Chan
# @Email   : samuelchan1205@gmail.com
# @File    : continuous.py


import numpy as np
from patsy import dmatrix
import statsmodels.api as sm


class Continuous:
    def __init__(self, k=3):
        self.x = None
        self.model = None
        self.all = None
        self.k = k

    def transform(self, x):
        x = np.array(x)
        assert x.ndim == 1
        n = x.shape[0]
        if self.all is None:
            self.all = np.array(x)
        else:
            self.all = np.concatenate([self.x, x])
        transformed_x = dmatrix("cr(x,df={})".format(self.k), {"x": self.all}, return_type='dataframe')[-n:]
        return transformed_x

    def fit(self, x, y):
        self.model = sm.GLM(y, x).fit()
        return self.model

    def predict(self, x):
        pred = self.model.predict(x)
        return pred
