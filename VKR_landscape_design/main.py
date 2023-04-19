import sqlite3
import numpy as np
import pandas as pd
from models.animals_model import *
from models.grounds_model import *
from models.plants_model import *
from models.soils_model import *
from models.territories_model import *
from models.users_model import *
pd.options.display.max_rows = 100
pd.options.display.max_columns = 100

# PRAGMA FOREIGN_KEYS = on;

con = sqlite3.connect("VKR.sqlite")

con.executescript('''

 ''')



con.commit()

cursor = con.cursor()

print(get_animals(con))
print(get_grounds(con))
print(get_plants(con))
print(get_soils(con))
print(get_territories(con))
print(get_users(con))
print()
print()
print()


print()