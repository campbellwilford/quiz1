# Read the file VendorList.csv into this program and create a dictionary of the customer's
# full name, email address and phone number where the key is the full name of the customer
# and the value is a dictionary where the keys are 'email' and 'phone' and the values
# are the corresponding email address and phone number of the customer. 

# Once the dictionary has been completed print it out. It shoud resemble what is shown
# below (first 2 and last 2 elements shown only):

#{'Tommie Goody': {'email': 'tgoody0@weather.com', 'phone': '809-992-7298'}, 
# 'Obadiah Godfery': {'email': 'ogodfery1@a8.net', 'phone': '560-745-9361'}......
# ..........'Kessiah Tynemouth': {'email': 'ktynemouthdu@ning.com', 'phone': '690-215-8097'}, 
# 'Carmela Kaubisch': {'email': 'ckaubischdv@wikia.com', 'phone': '307-726-6526'}}


# Using the dictionary, write the contents to a csv file. The output file shoud be exactly as
# what is shown in the file - marketinglist.csv.
# Name your file - marketinglistFINAL.csv


# Note: you can use the comments below to guide you through the logic of the code. You are not
# required to follow it. ALSO NOT ALL STEPS HAVE BEEN COMMENTED. You may have additional steps.


import csv

# open the vendorlist file
VendorList = open("VendorList.csv", "r")
print(VendorList.read())

# create a csv object from the file object
writer = csv.writer(VendorList)


# create an output file

with open('outputfile', 'w') as outputfile:
    outputfile.writelines('VendorList')

# create an empty dictionary

empty_dictionary = dict()

# iterate through the csv object

from csv import reader

with open('VendorList.csv', 'r') as readlist:

    readlist = reader(readlist)

    for row in readlist:
    
        print(row)



    # add the key-value pair to the dictionary

VendorList = {'id:50001, first_name:Tommy, last_name:Goody, gender:Male, email: tgoody0@weather.com, phone: 809-992-7298'}

# print the dictionary after the loop is finished

print(VendorList)

# iternate through the dictionary and write to the output file

for id, first_name, last_name, gender, email, phone in VendorList():
    print ('This is the full Vendor List')
    outputfile=open('VendorList.csv','w')
    outputfile.write(id)
    outputfile.write(first_name)
    outputfile.write(last_name)
    outputfile.write(gender)
    outputfile.write(email)
    outputfile.write(phone)

outputfile.close()

# close your output file

