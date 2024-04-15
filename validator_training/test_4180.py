import pandas as pd


def rule_4180(df):
    valid_gender_codes = ["1", "2", "0", "9"]

    failing_rows = df[~df["GenderCurrent"].isin(valid_gender_codes)].index

    return list(failing_rows)


def test_rule_4180():

    ChildIdentifiers = pd.DataFrame(
        {
            "GenderCurrent": [
                "1",
                "2",
                "0",
                "9",
                "4",  # 4, fail
                1,  # 5, fail
                "just a word",  # 6, fail
            ]
        }
    )

    result = rule_4180(ChildIdentifiers)

    assert result == [4, 5, 6]
