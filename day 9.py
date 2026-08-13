import art
print(art.logo2)
bids={}
def highest_bidder(bidding_dictionary):
    highest_bid=0
    winner = ""
    max(bidding_dictionary)
    for bidder in bidding_dictionary:
        max_bid=bidding_dictionary[bidder]
        if max_bid>highest_bid:
            highest_bid=max_bid
            winner=bidder
        print(f"the winner is {winner} with {highest_bid} amount bid")
should_continue= True
while should_continue:
    name=input("what is your name?\n")
    bid=int(input("what is your bid? : "))
    bids[name]=bid
    more_bidders= input("Are there any new bids?type yes or no\n")
    if more_bidders=="no":
        should_continue=False
        highest_bidder(bids)
    else:
        print("\n"*50)
        should_continue=True




