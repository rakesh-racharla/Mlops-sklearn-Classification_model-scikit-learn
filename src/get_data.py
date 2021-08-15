## read params
## process
## return dataframe
import os
import yaml
import pandas as pd
import argparse
from read_parameters import read_params

def get_data(config_path):
    config = read_params(config_path)
    # print(config)
    data_path = config["data_source"]["Git"]
    print(data_path)
    try:
        df = pd.read_table(data_path)
    except:
        print("Data loading Failed")
    return df



if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    data = get_data(config_path=parsed_args.config)

