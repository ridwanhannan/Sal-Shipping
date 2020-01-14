def ground_shipping(weight):
  flat_charge = 20.00
  price = 0 
  if weight <= 2:
    price = weight * 1.50 + flat_charge
    return price
  elif weight > 2 and weight <= 6:
    price = weight * 3.00 + flat_charge
    return price
  elif weight > 6 and weight <= 10:
    price = weight * 4.00 + flat_charge
    return price
  else:
    price = weight * 4.75 + flat_charge
    return price 


cost_of_premium_ground_shipping = 125.00

def drone_shipping(weight):
  price = 0
  if weight <= 2:
    price = weight * 4.50
    return price
  elif weight > 2 and weight <= 6:
    price = weight * 9.00
    return price
  elif weight > 6 and weight <= 10:
    price = weight * 12.00
    return price
  else:
    price = weight * 14.25
    return price
  
def cheapest_shipping_cost(weight):
  ground = ground_shipping(weight)
  premium = cost_of_premium_ground_shipping 
  drone = drone_shipping(weight)
  
  if ground < premium and ground < drone:
    method = "standard ground"
    cost = ground 
  elif premium < ground and premium < drone: 
    method = "premium"
    cost = premium
  else:
    method = "drone"
    cost = drone
    
  return("The cheapest option is $%.2f with %s shipping.") % (cost, method)
    

    
print(cheapest_shipping_cost(4.8))
print(cheapest_shipping_cost(41.5))
  