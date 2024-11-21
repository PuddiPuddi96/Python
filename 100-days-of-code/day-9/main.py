from art import logo

def get_winner(bidders):
    highest_bid = 0
    winner = ""
    for bidder in bidders:
        if bidders[bidder] > highest_bid:
            winner = bidder
            highest_bid = bidders[bidder]
    return winner


bids = {}
continue_bidding = True

print(logo)

while continue_bidding:
    name = input("What's your name? ")
    bid = float(input("What's your bid? $"))

    bids[name] = bid

    response = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if response == "no":
        continue_bidding = False
    else:
        print("\n" * 20)

bidder_winner = get_winner(bids)
#bidder_winner = max(bids, key=bids.get)

print(f"The winner is {bidder_winner} with a bid of ${bids[bidder_winner]}")
