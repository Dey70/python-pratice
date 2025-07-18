logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

def find_highest_bidder(bid_record):
  highest_bid = 0
  winner = ""
  for bidder in bid_record:
    bid_amount = bid_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid:.2f}.")





bids = {}
continue_bidding = True
while continue_bidding:
  name = input("Welcome to the Blind Auction!\nWhat is your name? ")
  bid_price = float(input(f"Hello {name}, what is your bid price? $"))
  bids[name] = bid_price
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
  if other_bidders == 'no':
    continue_bidding = False
    find_highest_bidder(bids)
  elif other_bidders == 'yes':  
    print("\n"*20)


  