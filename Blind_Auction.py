from os import system
system("cls")
dict = {}
while(True):
    print("Welcome to Blind Auction.\nPlease enter your name and bid\n\n")
    name = input("Name: ")
    bid = int(input("Bid: "))
    dict[name] = bid
    call = input("\nAny more bidders: ").lower()
    system('cls')
    if(call == "n"):
        break
    

bidder = max(dict.values())
print("Highest bidder is:")
for i in dict:
    if(dict[i] == bidder):
        print(f"{i} with amount {dict[i]}")