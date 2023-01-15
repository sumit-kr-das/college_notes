class Customer:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address

    def edit_info(self, new_name, new_gender, new_city, new_pin, new_state):
        self.name = new_name
        self.gender = new_gender

        self.address.change_address(new_city, new_pin, new_state)

class Address:
    def __init__(self,city,pin,state):
        self.city = city
        self.pin = pin
        self.state = state

    def change_address(self, new_city, new_pin, new_state):
        self.city = new_city
        self.pin = new_pin
        self.state = new_state

add = Address("Kalkata",700123,"WB")
cust = Customer("Nitesh","Male", add)

cust.edit_info("Sumit","Male","BDN",713128,"MP")

print(cust.address.city)