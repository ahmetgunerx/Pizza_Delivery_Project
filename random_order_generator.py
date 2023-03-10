import pandas as pd
import random
from randomtimestamp import randomtimestamp
from tqdm import tqdm


# username,address,ordered_pizza,ordered_sauce,total_amount,order_datetime,order_note
customersdf = pd.read_csv("customers.csv")
ordersdf = pd.read_csv("orders.csv")


pizza_prices = {"classic":30, "margherita":40, "turkish":50, "simple":20}
sauce_prices = {"olive":4, "mushroom":10, "goat cheese":7, "meat":15, "onion":4, "corn":6}

ord_notes = ["no extra sauce please.", "don't put tomatoes on pizza.", "don't ring the bell.", "extra sauce please.", 
                          "please hurry! I'm hungry.", "I want more mushrooms than the previous order"]



howmany = int(input("how many order data you want to create? --> "))


for i in tqdm(range(howmany)):
     ind = random.choice(range(1000))
     ordersdf.loc[i,"username"] = customersdf.loc[ind, "username"]
     ordersdf.loc[i,"address"] = customersdf.loc[ind,"address"]
     ordersdf.loc[i,"ordered_pizza"] = random.choice(list(pizza_prices.keys()))
     ordersdf.loc[i, "ordered_sauce"] = random.choice(list(sauce_prices.keys()))
     ordersdf.loc[i, "total_amount"] = str(pizza_prices[ordersdf.loc[i,"ordered_pizza"]] + 
                                                  sauce_prices[ordersdf.loc[i, "ordered_sauce"]]) + "₺"
     random_time = randomtimestamp(2023,2023)
     random_time = random_time.strftime("%d/%m/%Y %H:%M:%S")
     ordersdf.loc[i, "order_datetime"] = random_time
     ordersdf.loc[i, "order_note"] = random.choice(ord_notes)
  
print(ordersdf)

ordersdf.to_csv("orders.csv", index=False)