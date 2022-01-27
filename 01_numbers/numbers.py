la_shipment = 11_754
ncy_shipment = 6_903
houston_shipment = 2_897
leftover = 297

total = la_shipment + ncy_shipment + houston_shipment + leftover

cars_needed = total/330
leftover = total%330


print(cars_needed)
print(leftover)
