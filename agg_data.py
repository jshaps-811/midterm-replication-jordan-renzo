#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 10:42:09 2025

@author: jordanshaps
"""

import os
import csv
import pandas as pd

def output_agg_data(in_directory: str, out_fpath: str):
    
    
    def summarize(fname: str, aggregate_type: str, aggregate_col: str, groupby_cols: list, delimiter='\t'):
        """
        Args:
            fname: path to tsv/csv file
            aggregate_type: mean or sum
            aggregate_col: the column with values to aggregate
            groupby_cols: list of columns to group by

        Returns:
            Pandas DataFrame aggregated by the specified columns
        """
        dat = pd.read_csv(fname, sep=delimiter)
        summ = dat.groupby(groupby_cols).agg({aggregate_col: aggregate_type}).reset_index()
        return summ


    with open(out_fpath, "w", newline='', encoding='utf-8') as out_file:
        writer = csv.writer(out_file, delimiter='\t')
        writer.writerow(["model", "type", "mean_acc"])

        for fname in os.listdir(in_directory):
            fpath = os.path.join(in_directory, fname)
            if not os.path.isfile(fpath):
                continue  # skip non-files
            if not (fname.endswith(".tsv")):
                continue  # skip non-data files

            try:
                summ_df = summarize(fpath, "mean", "acc", ["model"])

                for _, row in summ_df.iterrows():
                    ling_type = " ".join(fname.strip().split("_"))
                    ling_type = ling_type.split(".")[0]
                    writer.writerow([row["model"], ling_type, row["acc"]])

            except Exception as e:
                print(f"Error processing {fname}: {e}")


in_directory = "./results/mbert_russian"
out_fpath = "./agg_results/mbert_russian_summary.tsv"

output_agg_data(in_directory, out_fpath)






