import pandas
import scipy
data = pandas.read_csv("data_salaries_india.csv")

# helper function for pandas to convert all salaries
# into yearly integer salaries
def yearly_wage(row):
    # the last two characters determine if it's yearly, monthly, hourly
    period = row["Salary"][-2:]
    
    # remove all commas and combine all numbers
    number = int("".join(filter(str.isdigit, row["Salary"])))
    
    # if it's hourly, the average work hours per year in India is
    # approximately 2117.01 (might change in future)
    if period == "hr":
        number = int(number * 2117.01)
    elif period == "mo":
        # months to year
        number = int(number * 12)
    
    # return the yearly salary in integer format
    return number


data["Annual Salary"] = data.apply(yearly_wage, axis=1)
=======
# Converted annual salary, in indian rupees
data["Annual Salary"] = data.apply(yearly_wage, axis=1)

# Most common company names
common_company = data["Company Name"].value_counts().nlargest(5)

# Most common job locations, seems to be an emphasis in Bangalore
common_location = data["Location"].value_counts().nlargest(5)

# Most common job titles
common_titles = data["Job Title"].value_counts().nlargest(5)

# Seeing if the salary mean is skewed by the 2 highest earners, whose salaries are almost twofold
# Compared to the one behind them
mean_salary = data["Annual Salary"].mean()
# vesas, as in Vesa Keskinen(s)
annual = data["Annual Salary"]
no_vesas = annual.drop(index=annual.nlargest(2, keep="all").index)
mean_salary_no_vesas = no_vesas.mean()
# This alone drops the mean by ~20k rupees, not much probably but still good to know

# Specialist = 0, manager = 1
label1, unique1 = pandas.factorize(data["Role"], sort=False)
label2, unique2 = pandas.factorize(data["Location"], sort=False)
label3, unique3 = pandas.factorize(data["Company Name"], sort=False)
data["Role Binary"] = label1
data["Location Binary"] = label2
data["Company binary"] = label3

# As the number is close enough to zero, we can say that location has no correlance to salary
location_to_salary = data["Location"].corr(data["Annual Salary"], method="spearman")

# Now the number is -0.4, close to zero but not that close.
# Some correlation is possible, but not enough to be confidently sure.
# PS. I delved into a rabbit hole of the spearman rank correlation coefficient,
# And the finnish wikipedia page uses an example chart of fish sizes while
# The english page uses an example chart of hours of TV watched to IQ,
# Cultural difference? Maybe.
role_to_salary = data["Role"].corr(data["Annual Salary"], method="spearman")

# Really close to zero, no correlation, so no companies have significantly higher salaries
company_to_salary = data["Company Name"].corr(data["Annual Salary"], method="spearman")

# Not many correlations, but there might be some errors in my way of trying to
# Look for them, maybe need a different mindset of thinking
