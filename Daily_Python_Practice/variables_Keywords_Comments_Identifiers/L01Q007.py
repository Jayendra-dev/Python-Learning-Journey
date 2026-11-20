"""E5. Cab fare
Base fare 50, 12 per km, 18 km, waiting 10 minutes at 2 per minute.
"""

base_fare = 50
rate_per_km = 12
distance_km = 18
waiting_minutes = 10
waiting_rate = 2
total_fare = (base_fare + (rate_per_km * distance_km)+ (waiting_minutes * waiting_rate))
print("Total fare:", total_fare) # 286
