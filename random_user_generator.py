import pandas as pd
import random
from faker import Faker
import names
from tqdm import tqdm


df = pd.read_csv("customers.csv")




howmany = int(input("how many user data you want to create? --> "))


for i in tqdm(range(howmany)):
     df.loc[i,"username"] = names.get_first_name()
     df.loc[i,"password"] = df.loc[i,"username"]+"123"
     df.loc[i,"user_Id"] = random.randrange(100000, 999999)
     df.loc[i, "credit_card_number"] = Faker().credit_card_number(card_type='visa16')
     df.loc[i, "credit_card_security_code"] = random.randrange(100,1000)
     df.loc[i, "credit_card_expire"] = Faker().credit_card_expire()
     df.loc[i, "address"] = Faker().address()
  
     # remove decimal parts of user_Id's and credit_card_security_code's
     df.loc[i,"user_Id"] = str(df.loc[i,"user_Id"]).split('.')[0]
     df.loc[i,"credit_card_security_code"] = str(df.loc[i,"credit_card_security_code"]).split('.')[0]

print(df)

df.to_csv("customers.csv", index=False)