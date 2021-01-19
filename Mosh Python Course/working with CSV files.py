import csv

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(['transaction_ID', "product_ID", "price_ID"])
    writer.writerow([1000, 1, 5])
    writer.writerow([1001, 2, 15])