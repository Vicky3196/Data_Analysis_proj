Mobile Tracking

#  Mobile phone tracking is a process for identifying the location of a mobile phone, 
   whether stationary or moving.
#  Phone numbers is one of the modules that provides numerous Features like providing 
   basic information about a phone number, validation of a phone number, etc.
#  The phone number is entered and a library is used to turn the country calling code. For 
   example numbers starting with +91 becomes India, +880 is Bangladesh, +34 is Spain, 
   etc.


import phonenumbers 
from phonenumbers import timezone,geocoder,carrier
number = input("Enter your no. with +__: ")
phone = phonenumbers.parse(number)
time=timezone.time_zone_for_number(phone)
car=carrier.name_for_number(phone,"en")
reg =geocoder.description_for_number(phone,"en")
print(phone)
print(time)
print(car)
print(reg)
