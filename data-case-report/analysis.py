import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("injuries.csv")

# Cleaning up data
data = data.drop("business.second name", axis=1)
data = data.drop("address.street", axis=1)
data = data.drop("address.zip", axis=1)
industry_sorted_data = data["industry.division"].value_counts(ascending=False).reset_index()
industry_sorted_data.columns = ["Industry Name", "Report Count"]
state_industry_sort = data[["address.state", "industry.division"]]
state_industry_sort.columns = ["State", "Industry"]

# plt.clf()
print("Most represented states:")
print(data["address.state"].value_counts().nlargest(5))
print("Most represented cities:")
print(data["address.city"].value_counts().nlargest(5))
# sns.histplot(data["year"])
# plt.figure()
plt.clf()
state_plot = sns.countplot(x="State",
              hue="Industry",
              data=state_industry_sort,
              order=state_industry_sort.State.value_counts().iloc[:5].index)
plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
plt.figure()

print("Mean days away:")
print(data["statistics.days away"].mean())

companies = data["business.name"].value_counts(ascending=False).reset_index()
worst_companies = companies[:10]
worst_companies.columns = ["Business Name", "Reports"]