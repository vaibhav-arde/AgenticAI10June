from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str = 'Male'
    age: int
    address: Address

address_dict = {'city': 'Kolhapur', 'state': 'Maharashtra', 'pin': '416007'}

address1 = Address(**address_dict)

patient_dict = {'name': 'Vaibhav', 'age': 35, 'address': address1}

patient1 = Patient(**patient_dict)

temp1 = patient1.model_dump()
print(type(temp1))
print(patient1)

temp2 = patient1.model_dump_json()
print(type(temp2))
print(patient1)

temp3 = patient1.model_dump(exclude=['name', 'age'])
print(temp3)
print(type(temp3))
