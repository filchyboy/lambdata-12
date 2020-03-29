#lambdata-12/my_script.py

import pandas
from my_lambdata.my_mod import enlarge


print("Hello world!")

df = pandas.DataFrame({"state": ["CT", "CO", "CA", "TX"]})
print(df.head)

print("__________________")

x=5
print("Number", x)
print("Enlarged Number", enlarge(x))