
def my_data(name):
    return {"name": name,
            "age": "31",
            "marital_status": True,
            "hobby" : "lol",
            "personality": "habby"}


def all_data(func):
    return func(name="james")


def get_name_data(func):
    return func(name="james").get("name")



print(get_name_data(my_data))
print(all_data(my_data))