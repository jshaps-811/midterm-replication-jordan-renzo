#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 27 15:55:27 2025

@author: jordanshaps
"""

import os
import csv

def txt_to_tsv(in_folder, out_folder):
    if not os.path.exists(out_folder):
        os.makedirs(out_folder)

    for fname in os.listdir(in_folder):
        if fname.endswith(".txt"):
            txt_fpath = os.path.join(in_folder, fname)
            tsv_fname = os.path.splitext(fname)[0] + ".tsv"
            tsv_fpath = os.path.join(out_folder, tsv_fname)

            try:
                with open(txt_fpath, 'r', encoding='utf-8') as in_file:
                    lines = in_file.readlines()

                with open(tsv_fpath, 'w', newline='', encoding='utf-8') as out_file:
                    tsv_writer = csv.writer(out_file, delimiter='\t')
                    header = ["sentid", "pairid", "expected", "sentence"]
                    tsv_writer.writerow(header)
                    sentid = 1
                    pairid = 1
                    for line in lines:
                        sent = line.strip().split()
                        to_write = [sentid, pairid, sent[0], " ".join(sent[1:])]
                        tsv_writer.writerow(to_write)
                        sentid += 1
                        if sentid % 2 == 1:
                            pairid += 1

            except Exception as e:
                print(f"Error processing '{fname}': {e}")


in_directory = "./test_cases/source_txt_files"  
out_directory = "./test_cases/eval_tsv_files" 

txt_to_tsv(in_directory, out_directory)