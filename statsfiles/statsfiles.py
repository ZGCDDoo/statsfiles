# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 10:03:34 2016

@author: Charles-David Hebert
"""

import time
import os
import sys


from . import statsobs
from . import statsarrays
from . import statsparams
from . import copy_essential


def run_statsfiles(iter_start: int, yy_params) -> None:

    obs_files = yy_params["obs_files"]

    array_files = yy_params["array_files"]["names"]
    array_files_ext = yy_params["array_files"]["ext"]

    params_files = yy_params["params_files"]["names"]

    # One list per element in params_files
    params_names_l = yy_params["params_files"]["parameters"]

    starr = statsarrays.StatsArrays(array_files=array_files,
                                    end_files=array_files_ext,
                                    ext=".dat", iter_start=iter_start,
                                    ignore_col=None, in_dir=os.getcwd(),
                                    warning_only=True)

    stobs = statsobs.StatsObs(obs_files=obs_files, iter_start=iter_start, ignore_col=0, in_dir=os.getcwd(),
                              warning_only=True)

    stparams = statsparams.StatsParams(params_files=params_files, params_names_l=params_names_l,
                                       ext="", iter_start=iter_start, in_dir=os.getcwd(),
                                       warning_only=True)

    out_dir = time.strftime("Stats" + "-%Y-%m-%d--%Hh%M")
    os.mkdir(out_dir)

    stobs.mean()
    stobs.std()
    stobs.write_results(out_dir=out_dir, file_out="statsobs.json")
    starr.mean()
    starr.std()
    starr.write_results(out_dir=out_dir, file_out="statsobs.json")
    stparams.mean()
    stparams.std()
    stparams.write_results(out_dir, "statsparams.json")

    ce = copy_essential.CopyEssential(out_dir)
    ce.run()
