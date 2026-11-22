# 4. Naming Audit – E-commerce Application
# E-commerce Application

# 1. Variables (PEP 8)

customer_name = "Rahul"
customer_id = 101

product_name = "Laptop"
product_price = 50000

cart_items = 2
total_amount = product_price * cart_items

discount_percentage = 10
shipping_address = "Puducherry"

payment_method = "UPI"
order_status = "Confirmed"


# 2. Constants (UPPERCASE)

GST_RATE = 18
FREE_SHIPPING_LIMIT = 1000
MAX_CART_ITEMS = 50


# 3. Calculations

discount_amount = total_amount * discount_percentage / 100

amount_after_discount = total_amount - discount_amount

gst_amount = amount_after_discount * GST_RATE / 100

final_amount = amount_after_discount + gst_amount


# 4. Display order details

print("CUSTOMER DETAILS")
print("Customer:", customer_name)
print("Customer ID:", customer_id)

print("\nORDER DETAILS")
print("Product:", product_name)
print("Quantity:", cart_items)
print("Payment:", payment_method)
print("Order Status:", order_status)

print("\nBILL DETAILS")
print("Original Amount:", total_amount)
print("Discount:", discount_amount)
print("GST:", gst_amount)
print("Final Amount:", final_amount)