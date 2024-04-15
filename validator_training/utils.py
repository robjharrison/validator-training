import pandas as pd


def read_cin_data():
    ChildCharacteristics = pd.read_csv(
        "/workspaces/validator-training/fake_cin_data/ChildCharacteristics.csv"
    )

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

    ChildProtectionPlans = pd.read_csv(
        "/workspaces/validator-training/fake_cin_data/ChildProtectionPlans.csv"
    )

    CINdetails = pd.read_csv(
        "/workspaces/validator-training/fake_cin_data/CINdetails.csv"
    )
    CINdetails["CINreferralDate"] = pd.to_datetime(
        CINdetails["CINreferralDate"], format="%d/%m/%Y", errors="coerce"
    )
    CINdetails["CINclosureDate"] = pd.to_datetime(
        CINdetails["CINclosureDate"], format="%d/%m/%Y", errors="coerce"
    )
    CINdetails["DateOfInitialCPC"] = pd.to_datetime(
        CINdetails["DateOfInitialCPC"], format="%d/%m/%Y", errors="coerce"
    )

    CINplanDates = pd.read_csv(
        "/workspaces/validator-training/fake_cin_data/CINplanDates.csv"
    )
    Header = pd.read_csv("/workspaces/validator-training/fake_cin_data/Header.csv")
    Header["ReferenceDate"] = pd.to_datetime(
        Header["ReferenceDate"], format="%d/%m/%Y", errors="coerce"
    )

    Reviews = pd.read_csv("/workspaces/validator-training/fake_cin_data/Reviews.csv")
    Section47 = pd.read_csv(
        "/workspaces/validator-training/fake_cin_data/Section47.csv"
    )

    return (
        ChildCharacteristics,
        ChildIdentifiers,
        ChildProtectionPlans,
        CINdetails,
        CINplanDates,
        Header,
        Reviews,
        Section47,
    )


# (
#     ChildCharacteristics,
#     ChildIdentifiers,
#     ChildProtectionPlans,
#     CINdetails,
#     CINplanDates,
#     Header,
#     Reviews,
#     Section47,
# ) = read_cin_data()
