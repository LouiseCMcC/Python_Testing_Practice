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
    
ef get_pets_by_breed(cc_pet_shop, pet_breed):
    pets = []
    for pet in cc_pet_shop["pets"]:
        if pet["breed"] == pet_breed:
            pets.append(pet)
    return pets
    
    
    
    # for breed in cc_pet_shop["pets"]:
    #     if breed["breed"] == pet_breed:
    #         return type




# def find_pet_by_name(cc_pet_shop, pet_name):
#     for pet in cc_pet_shop["pets"]["breed"]:
#         if pet["name"][""] == pet_name:
#             return pet_name



# def find_user_by_id(list, user_id):
#     for user in list:
#         if user["user_id"] == user_id:
#             return user
#     return None










