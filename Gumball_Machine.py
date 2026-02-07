# Constant Attributes
Nickel = 5
Dime = 10
Quarter = 25
Red_Gumball_Cost = 50
Green_Gumball_Cost = 100

#Machine State
balance = 0

# =====================================================================
# CORE FUNCTIONS
# =====================================================================
def reset_machine():
    """Reset the machine to its initial state, clearing any existing balance and preparing it for new transactions."""
    global balance
    balance = 0
    print("Machine reset. Balance cleared.")

def insert_coin(coin):
    """
    Insert a coin into the machine and update the balance accordingly. The function accepts a coin value and adds it to the current balance. It also checks if the coin is valid (Nickel, Dime, or Quarter) and provides feedback on the current balance after the coin is inserted.
    """
    global balance
    if coin in [Nickel, Dime, Quarter]:
        balance += coin
        print(f"Inserted {coin} cents. Current balance: {balance} cents.")
        return True
    else:
        print("Invalid coin. Please insert a Nickel, Dime, or Quarter.")
        return False
    
def dispense_gumball(color):
        """
        Dispense a gumball of the specified color if the balance is sufficient. The function checks the cost of the requested gumball (Red or Green) and compares it to the current balance. If the balance is sufficient, it dispenses the gumball and deducts the cost from the balance. If not, it informs the user of the insufficient balance.
        """
        global balance
        if color == "Red":
            cost = Red_Gumball_Cost
        elif color == "Green":
            cost = Green_Gumball_Cost
        else:
            print("Invalid color. Please choose 'Red' or 'Green'.")
            return False
        
        if balance >= cost:
            balance -= cost
            print(f"Dispensed a {color} gumball. Remaining balance: {balance} cents.")
            return True
        else:
            print(f"Insufficient balance to dispense a {color} gumball. Current balance: {balance} cents.")
            return False

def get_balance():
    """Return the current balance in the machine."""
    global balance
    return balance

def refund_change():
    """Refund the current balance to the user and reset the machine."""
    global balance
    if balance > 0:
        print(f"Refunding {balance} cents.")
        balance = 0
    else:
        print("No balance to refund.")
        
# =====================================================================
# Test Cases
# =====================================================================
