from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated
from datetime import date

class Patient(BaseModel):

    name: Annotated[str, Field(max_length=10, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Nitish', 'Amit'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]
    joining_date: date = Field(description="Employee joining date", examples=["2026-07-01"])


# def update_patient_data(patient: Patient):

    # print(patient.name)
    # print(patient.age)
    # print(patient.allergies)
    # print(patient.married)
    # print('updated')

patient_info = {'name':'Vaibhav', 'email':'abc@gmail.com', 'linkedin_url':'http://linkedin.com/1322', 'age': '30', 'weight': 75.2,'contact_details':{'phone':'2353462'}, 'joining_date':'2026-12-01'}

patient = Patient(**patient_info)
print(patient.name)
print(patient.age)
print(patient.weight)
print(patient.married)
print(patient.joining_date)
# print('updated')

# update_patient_data(patient1)
