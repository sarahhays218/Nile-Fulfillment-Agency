from nile import get_distance, format_price, SHIPPING_PRICES
from test import test_function

# Define calculate_shipping_cost() here:
def calculate_shipping_cost(from_coords, to_coords, shipping_type='Overnight'):
  distance = get_distance(*from_coords, *to_coords)
  shipping_type2 = SHIPPING_PRICES[shipping_type]
  price = (distance * shipping_type2)
  return format_price(price)

# Test the function by calling 
test_function(calculate_shipping_cost)

# Define calculate_driver_cost() here
def calculate_driver_cost(distance, *drivers):
  cheapest_driver = None
  cheapest_driver_price = None
  for driver in drivers:
    driver_time = driver.speed * distance
    price_for_driver = str(driver.salary * driver_time)
    if driver is None or price_for_driver < cheapest_driver_price:
      cheapest_driver = driver
      cheapest_driver_price = price_for_driver
    elif price_for_driver < cheapest_driver_price:
      cheapest_driver.update(driver)
      cheapest_driver_price.update(price_for_driver)
  return cheapest_driver, cheapest_driver_price

# Test the function by calling 
test_function(calculate_driver_cost)