class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        
    def deposit(self, amt, desc=""):
        self.ledger.append({"amount": amt, "description": desc})
        
    def withdraw(self, amt, desc=""):
        if self.check_funds(amt):
            self.ledger.append({"amount": -amt, "description": desc})
            return True
        return False
        
    def get_balance(self):
        bal = 0
        for x in self.ledger:
            bal += x["amount"]
        return bal
        
    def check_funds(self, amt):
        if amt > self.get_balance():
            return False
        return True
        
    def transfer(self, amt, other):
        if self.check_funds(amt):
            self.withdraw(amt, f"Transfer to {other.name}")
            other.deposit(amt, f"Transfer from {self.name}")
            return True
        return False
        
    def __str__(self):
        out = self.name.center(30, "*") + "\n"
        for item in self.ledger:
            d = item["description"][:23]
            a = f"{item['amount']:.2f}"
            out += f"{d:<23}{a:>7}\n"
        out += f"Total: {self.get_balance():.2f}"
        return out


def create_spend_chart(categories):
    spent_list = []
    for c in categories:
        s = 0
        for item in c.ledger:
            if item["amount"] < 0:
                s += abs(item["amount"])
        spent_list.append(s)
        
    tot = sum(spent_list)
    
    percents = []
    for s in spent_list:
        if tot == 0:
            percents.append(0)
        else:
            percents.append(int((s / tot) * 100) // 10 * 10)
            
    res = "Percentage spent by category\n"
    
    for i in range(100, -1, -10):
        res += f"{i:3}| "
        for p in percents:
            if p >= i:
                res += "o  "
            else:
                res += "   "
        res += "\n"
        
    res += "    " + "-" * (3 * len(categories) + 1)
    
    m = 0
    for c in categories:
        if len(c.name) > m:
            m = len(c.name)
            
    names = [c.name.ljust(m) for c in categories]
    
    for i in range(m):
        res += "\n     "
        for n in names:
            res += f"{n[i]}  "
            
    return res