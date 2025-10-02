import phonenumbers
from phonenumbers import geocoder

phone_number1=phonenumbers.parse("+998907095756")
phone_number2=phonenumbers.parse("+14158586273")

print("\nPhone Numbers location")
print(geocoder.description_for_number(phone_number1,"en"))
print(geocoder.description_for_number(phone_number2,"en"))
