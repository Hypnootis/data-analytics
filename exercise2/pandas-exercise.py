import pandas

data = pandas.read_csv("loans.csv")

data = data.drop("Customer ID", axis=1) # Remove customer IDs

print(data.head()) # Head of data

data = data[data["Current Loan Amount"] < 99999999] # Remove loans that are too big

# Replace NaN values in annual income with the mean
data["Annual Income"].fillna((data["Annual Income"].mean()), inplace=True)

average_loan = data["Current Loan Amount"].mean() # Mean/average

lowest_income = data["Annual Income"].min()

highest_income = data["Annual Income"].max()

ownership_value_id = data[data["Loan ID"] == "bbf87a87-22cd-4d10-bd9b-7a9cc1b6e59d"]
ownership_value_id = ownership_value_id["Home Ownership"]

data["Real Annual Income"] = data["Annual Income"] - 12 * data["Monthly Debt"]

income_id = data[data["Loan ID"] == "76fa89b9-e6a8-49af-afa1-8151315aba8e"]

income_id = income_id["Real Annual Income"]

lowest_income = data["Real Annual Income"].min()

# Since the lowest actual income is negative, this is for the positive...
lowest_positive_income = min([smallest for smallest in data["Real Annual Income"] if smallest > 0])

long_terms = data[data["Term"] == "Long Term"]

long_terms_count = len(long_terms.index)

bankrupters = data[data["Bankruptcies"] > 0]

bankrupters_count = len(bankrupters.index)

short_terms = data[data["Term"] == "Short Term"]

home_improvers = short_terms[short_terms["Purpose"] == "Home Improvements"]

uniques = data["Purpose"].nunique()

commons = data["Purpose"].value_counts()[:3].index.tolist()

correlations1 = data["Annual Income"].corr(data["Number of Open Accounts"])

correlations2 = data["Number of Credit Problems"].corr(data["Bankruptcies"])

print(f"Annual income correlates with open accounts: {correlations1 > 0.7}")

print(f"Credit problems correlates with bankruptcies: {correlations2 > 0.7}")