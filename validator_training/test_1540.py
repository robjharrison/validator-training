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



# - rule 1540: If UPN (N00001) present chars 5-12 must be numeric

def rule_1540(df):
    if 'UPN' not in df.columns:
        return []
    
    def check_upn(upn):
        # only arrive here if not na
        # do the rule checks
        if len(upn) >= 13:              # rule #1 if exists & valid size
            slice_ = upn[4:13]          
            is_digit = slice_.isdigit() # rule #2 numeric on 5th to 13th char (incl)

            # testing
            print(f"UPN chk'{upn}': slice is '{slice_}', is digit/num: {is_digit}")

            return is_digit
        return False

    # UPN exists? perform the rule checks
    condition = df['UPN'].notna() & df['UPN'].apply(check_upn)
    failing_rows = df[~condition].index

    # testing
    print("Failing indices:", failing_rows)


    return list(failing_rows)



def test_rule_1540():

    # opt1
    # file path and get sample data file
    directory_path = "/workspaces/validator-training/fake_cin_data"
    data_dfs_dict = load_data_files(directory_path)

    # opt2
    #    # use simplified df
    # ChildIdentifiers = pd.DataFrame({
    #     "UPN": [
    #         "A850728973744",  # 0 - valid
    #         "A141396438491",  # 1 - valid
    #         "A929946861554",  # 2 - valid
    #         "A612330267292",  # 3 - valid
    #         "not real eth",   # 4 - Invalid, non-numeric characters
    #         "A1234X67890123", # 5 - Invalid, non-numeric at critical position
    #         "A512600833840",  # 6 - valid
    #         "A223285848317",  # 7 - valid
    #         "A12345D6789",    # 8 - Invalid, too short
    #         "A12345678901X3", # 9 - Invalid, non-numeric in requ slice
    #     ]
    # })

    
    # load data df
    result = rule_1540(data_dfs_dict.get('ChildIdentifiers'))

    # Expect indices 4, 5, 8, 9 to fail is using the sample df
    assert result == [4, 5, 8, 9], f"Expected failing indices [4, 5, 8, 9], but got {result}"

