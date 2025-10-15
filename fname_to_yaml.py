#!/usr/bin/env python3
# -*- coding: utf-8 -*-
\
import os

def fname_to_yaml(in_folder, out_folder, base_yaml):
    if not os.path.exists(out_folder):
        os.makedirs(out_folder)

    for fname in os.listdir(in_folder):
        if fname.endswith(".tsv"):
            tsv_fpath = os.path.join(in_folder, fname)
            yaml_fname = os.path.splitext(fname)[0] + ".yaml"
            yaml_fpath = os.path.join(out_folder, yaml_fname)

            try:
                with open(base_yaml, 'r', encoding='utf-8') as in_file:
                    lines = in_file.readlines()

                with open(yaml_fpath, 'w', newline='', encoding='utf-8') as out_file:
                    for line in lines:
                        if "fpath" in line:
                            sent = line.strip().split('/')
                            if "datafpath:" in line:
                                
                                print(sent[-1])
                                sent[-1] = tsv_fpath
                                print(sent)
                            elif "resultsfpath:" in line:
                                print(sent[-1])
                                sent[-1] = "results_" + tsv_fpath
                                print(sent)
                            elif "predfpath:" in line:
                                print(sent[-1])
                                sent[-1] = "pred_" + tsv_fpath
                                print(sent)
                            out_file.write("/".join(sent))
                        else:
                            out_file.write(line)

            except Exception as e:
                print(f"Error processing '{fname}': {e}")


in_directory = "./test_cases/eval_tsv_files/french"  
out_directory = "./configs/french" 
base_yaml = "./base_config.yaml"

fname_to_yaml(in_directory, out_directory, base_yaml)