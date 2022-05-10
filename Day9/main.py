#HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)

def highest_bid(bidding_records):
  high_bid=0
  winner =""
  for bidder in bidding_records:
    bid_amount=bidding_records[bidder]
    if bid_amount >high_bid:
      high_bid= bid_amount
      winner=bidder
  print(f"The winner is the {winner} The highest amount is ${high_bid}")
  
bid_details = {}
switch= False
while not switch:
  
  name = input("Enter the name:")
  bid= int(input("Enter the bid amount ? $"))
  bid_details[name]= bid
  a_bid=input("Is there another bid : say yes or no : ")
  if a_bid =="no":
    switch = True
    highest_bid(bidding_records=bid_details)
  elif a_bid =="yes":
    print('''**********************''')

