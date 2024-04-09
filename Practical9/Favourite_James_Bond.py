def get_favourite_bond_actor(birth_year):  
    bond_actors = {'Roger Moore': (1973, 1986),'Timothy Dalton': (1987, 1994),'Pierce Brosnan': (1995, 2005),'Daniel Craig': (2006, 2021)} #store the datas as a dictionary 
    watch_year = int(birth_year) + 18  
    favourite_actor = None  # Initialize the favourite actor as None  
    for actor, (start_year, end_year) in bond_actors.items():  
        if start_year <= watch_year <= end_year:  
            favourite_actor = actor  
            break  
    return favourite_actor 

# Example usage  
birth_year = 2023  
favourite_bond_actor = get_favourite_bond_actor(birth_year)  
  
if favourite_bond_actor is None:  
    print(f"No Bond actor found for someone born in {birth_year}")  
else:  
    print(f"The favourite Bond actor for someone born in {birth_year} is {favourite_bond_actor}")


birth_year = 1980
favourite_bond_actor = get_favourite_bond_actor(birth_year)  
  
if favourite_bond_actor is None:  
    print(f"No Bond actor found for someone born in {birth_year}")  
else:  
    print(f"The favourite Bond actor for someone born in {birth_year} is {favourite_bond_actor}")
