import pandas as pd


def rule_4220(df):
    # Ethnicity (N00177) must be present and a valid code

    eth_list = ["ABAN","AIND","AOTH","APKN","BAFR","BCRB","BOTH","CHNE","MOTH","MWAS","MWBA","MWBC","NOBT","OOTH","REFU","WBRI","WIRI","WIRT","WOTH","WROM"]

    failing_indices = df[~df["Ethnicity"].isin(eth_list)].index

    print(failing_indices)

    return list(failing_indices)


def test_rule_4220():
    # Ethnicity (N00177) must be present and a valid code

    ChildCharacteristics = pd.DataFrame(
        {
            "Ethnicity": [
                "WIRI", # 0
                "WBRI", # 1
                "BOTH", # 2
                "MWBC", # 3
                "not real eth", # 4, fail
                1,              # 5, fail
            ]
        }
    )

    result = rule_4220(ChildCharacteristics)

    expected_fail_indices = [4,5]

    assert result == expected_fail_indices


    # # Check if result(s) is as expected
    # assert len(result) == len(expected_fail_indices),   f"There should be {len(expected_fail_indices)} invalid vals, but found {len(result)}"
    # assert result == expected_fail_indices,             f"The index of the invalid vals should be ...{result} "




