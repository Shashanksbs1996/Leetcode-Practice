print("Welcome to the tip calculator.")
bill= float(input("What is the total bill? $" ))
tip=int(input("What percentage tip would you like to give? 10,12,or 15?"))
total=(bill+(bill*(tip/100)))
final=round(float(total/7),2)

print(f"Each person should pay: ${final}")