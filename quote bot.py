import datetime
import random
from datetime import time

now = datetime.datetime.now()

specific_time = time(12,35,00)

quotes = [
    "In the middle of difficulty lies opportunity. — Albert Einstein",
    "The best way to predict the future is to create it. — Peter Drucker",
    "Do what you can, with what you have, where you are. — Theodore Roosevelt",
    "Everything you can imagine is real. — Pablo Picasso",
    "Simplicity is the ultimate sophistication. — Leonardo da Vinci"
]

random_quote = random.choice(quotes)




def alert():
    now = datetime.datetime.now().time()
    while now == specific_time:
        print(random_quote)


alert()


        
    


    