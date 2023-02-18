pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}


#get both key and value from dictionary
for occupation, pct in pct_women_in_occupation.items():
  print("Women make up {} percent of {}".format(pct,occupation))

