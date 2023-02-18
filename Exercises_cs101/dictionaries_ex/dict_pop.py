available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

#pop key and return value of key and increment health_points
#"stamina grains" being the key, 0 is default if key has no value.
health_points += available_items.pop("stamina grains",0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread",0)

print(available_items)
print(health_points)

                    