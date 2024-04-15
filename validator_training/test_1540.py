
import pandas as pd


# - rule 1540: If UPN (N00001) present chars 5-12 must be numeric

# def rule_1540(df):
#     # check if 'UPN' exists. if not, return empty list
#     if 'UPN' not in df.columns:
#         return []

#     # testing
#     # print("UPN not NA:", df['UPN'].notna())
#     # print("Is digit:", df['UPN'].str.slice(4, 12).str.isdigit())
#     # print("Length >= 12:", df['UPN'].str.len() >= 12)

#     # prob more readable than lambda use
#     # conditions... if UPN is present and if characters 5-12 are numeric
#     # condition = df['UPN'].notna() & \
#     #             df['UPN'].str.slice(4, 12).str.isdigit() & \
#     #             df['UPN'].str.len() >= 12

#     condition = df['UPN'].notna() & df['UPN'].apply(lambda x: x[4:12].isdigit() if len(x) >= 12 else False)

#     failing_rows = df[~condition].index

#     return list(failing_rows)

def rule_1540(df):
    if 'UPN' not in df.columns:
        return []
    
    def check_upn(upn):
        # do the rule checks
        if len(upn) >= 13:  # UPN >13
            slice_ = upn[4:13]  # slice 5th to 13th char (incl)
            is_digit = slice_.isdigit()

            # testing
            print(f"Checking UPN '{upn}': Slice is '{slice_}', Is digit: {is_digit}")

            return is_digit
        return False

    # UPN exists? perform the rule checks
    condition = df['UPN'].notna() & df['UPN'].apply(check_upn)
    failing_rows = df[~condition].index

    # testing
    print("Failing indices:", failing_rows)


    return list(failing_rows)



def test_rule_1540():


    # df with UPN, valid(from ChildIdentifiers) n invalid records

    # # use a cut-down/simplified df
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

    # Use the actual sample/fake data
    ChildIdentifiers = pd.read_csv(
        "/workspaces/validator-training/fake_cin_data/ChildIdentifiers.csv"
    )
    ChildIdentifiers["PersonBirthDate"] = pd.to_datetime(
        ChildIdentifiers["PersonBirthDate"], format="%d/%m/%Y", errors="coerce"
    )
    ChildIdentifiers["ExpectedPersonBirthDate"] = pd.to_datetime(
        ChildIdentifiers["ExpectedPersonBirthDate"], format="%d/%m/%Y", errors="coerce"
    )
    ChildIdentifiers["PersonDeathDate"] = pd.to_datetime(
        ChildIdentifiers["PersonDeathDate"], format="%d/%m/%Y", errors="coerce"
    )


    result = rule_1540(ChildIdentifiers)

    # Expect indices 4, 5, 8, 9 to fail is using the sample df
    assert result == [4, 5, 8, 9], f"Expected failing indices [4, 5, 8, 9], but got {result}"

