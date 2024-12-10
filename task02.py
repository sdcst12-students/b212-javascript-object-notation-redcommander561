#!python3
import requests
import json

# we can use requests to retrieve json encoded data from the internet
# there are different methods that we can retrieve the data with: POST and GET
# You can google the difference between POST and GET requests

req = requests.get('http://sdcaf.hungrybeagle.com/menu.php')
#print(req.status_code)
#print(req.connection)
#print(req.apparent_encoding)
#print(req.elapsed)
#print(req.text)

data = req.text
#print(data)
#print( type(data) )

# Use the json encoded data that is retrieved from this website and print out the weekly menu
# You will need to decipher the json decoded data to determine what information the 
# dictionary object contains

x = json.loads(data)
for i in x:
    print(i)

print(f"the menu is {x['menu']}")

