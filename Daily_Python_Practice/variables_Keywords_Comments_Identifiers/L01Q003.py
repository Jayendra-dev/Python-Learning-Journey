# E1. Restaurant bill with GST and discount

price = 250
quantity = 3
gst = 5
discount = 10

# Calculate subtotal
subtotal = price * quantity

# Calculate GST
GST_AMOUNT = subtotal * gst / 100

# Calculate total cost after GST
total_cost = subtotal + GST_AMOUNT

# Calculate discount on subtotal
discount_amount = subtotal * discount / 100

# Calculate final bill
final_bill = total_cost - discount_amount

# Print final bill
print("Subtotal:", subtotal)
print("GST Amount:", GST_AMOUNT)
print("Total Cost:", total_cost)
print("Discount Amount:", discount_amount)
print("Final Bill:", final_bill)





"""Subtotal: 750
GST Amount: 37.5
Total Cost: 787.5
Discount Amount: 75.0
Final Bill: 712.5"""