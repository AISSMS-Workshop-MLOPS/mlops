import os
import yaml
import pandas as pd
import numpy as np
import argparse
from pkgutil import get_data

def get_data(congfig_path):
    congfig = read_param(congfig_path)
    #print(congfig)
    data_path = congfig["load_data"]["clean_data"]
    df = pd.read_csv(data_path, sep=',', encoding="utf-8")
    # print(df)
    return df

def read_param(congfig_path):
    with open(congfig_path) as ymal_file:
        config = yaml.safe_load(ymal_file)
        return config

if __name__ == "__name__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yml")
    parsed_args = args.parse_args()
    data = get_data(congfig_path = parsed_args.config)