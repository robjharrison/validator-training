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
            ]
        }
    )

    result = rule_4220(ChildCharacteristics)

    # Check if result is as expected
    assert len(result) == 1, "expecting only 1 invalid ethnicity"
    assert result == [4], "invalid ethnicity index should be [4]"