import pandas

data = pandas.read_csv("purchases.csv")

order_sum = data[data["Purchase Order Number"] == "018H2015"]

order_sum = sum(order_sum["Total Price"])

purchased_item = data[data["Purchase Order Number"] == "3176273"]

purchased_item = purchased_item[["Item Name", "Item Description"]]

purchases_2013 = data[pandas.to_datetime(data["Creation Date"]).dt.year == 2013]

commons = data["Department Name"].value_counts()[:5]

sorted_data = data.sort_values("Department Name")