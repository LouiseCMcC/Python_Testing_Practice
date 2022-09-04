# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(cc_pet_shop):
    return cc_pet_shop["name"]

def get_total_cash(cc_pet_shop):
    return cc_pet_shop["admin"]["total_cash"]

def add_or_remove_cash(cc_pet_shop, num):
    cc_pet_shop["admin"]["total_cash"] += num
    return

def get_pets_sold(cc_pet_shop):
    return cc_pet_shop["admin"]["pets_sold"]

def add_or_remove_cash(cc_pet_shop, num):
    cc_pet_shop["admin"]["total_cash"] += num
    return

def pets_sold(cc_pet_shop):
    cc_pet_shop["admin"]["pets_sold"] == 0
    return

def increase_pets_sold(cc_pet_shop, num):
    cc_pet_shop["admin"]["pets_sold"] += num
    return

def get_stock_count(cc_pet_shop):
    return len(cc_pet_shop["pets"])

def get_pets_by_breed(cc_pet_shop, pet_breed):
    pets = []
    for pet in cc_pet_shop["pets"]:
        if pet["breed"] == pet_breed:
            pets.append(pet)
    return pets

def get_pets_by_breed(cc_pet_shop, pet_breed):
    pets = []
    for pet in cc_pet_shop["pets"]:
        if pet["breed"] == pet_breed:
            pets.append(pet)
    return pets

def find_pet_by_name(cc_pet_shop, pet_name):
    for name in cc_pet_shop["pets"]:
        if name["name"] == pet_name:
            return name

def find_pet_by_name(cc_pet_shop, pet_name):
    for name in cc_pet_shop["pets"]:
        if name["name"] == pet_name:
            return name

def remove_pet_by_name(cc_pet_shop, remove_pet_name):
    for name in cc_pet_shop["pets"]:
        if name["name"] == remove_pet_name:
            cc_pet_shop["pets"].remove(name)

def add_pet_to_stock(cc_pet_shop, new_pet):
    cc_pet_shop["pets"].append(new_pet)
    return len(cc_pet_shop["pets"])

def get_customer_cash(customers):
    return(customers["cash"])

def remove_customer_cash(customers, cash_to_remove):
    customers["cash"] -= cash_to_remove

def get_customer_pet_count(customers):
    return sum(pets["pets"] for pets in customers["pets"])

def add_pet_to_customer(customers, new_pet):
    customers["pets"].append(new_pet)
    return sum(pets["pets"] for pets in customers["pets"])

 


    
        

   
    
    
  



    



    
    
    
    










