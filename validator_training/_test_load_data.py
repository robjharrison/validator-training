import pandas as pd
import os

def load_data_files(directory_path):
    data_dict = {}
    
    # find all the csvs in path
    for file in os.listdir(directory_path):
        if file.endswith('.csv'):
            file_path = os.path.join(directory_path, file)
            # load each csv
            df = pd.read_csv(file_path)
            
            # ensure data cols are consistent
            for col in df.columns:
                if 'Date' in col:   # look for col substring to id date cols
                                    # and enforce format/consistency
                    df[col] = pd.to_datetime(df[col], format="%d/%m/%Y", errors="coerce")
            
            # add df to dict
            data_dict[file.replace('.csv', '')] = df
    
    return data_dict

# file path and run
directory_path = "/workspaces/validator-training/fake_cin_data"
data_dfs_dict = load_data_files(directory_path)
