import requests
import json
import os

#cantdeusers
while True:
    n = int(input("Ingrese la cantidad de usuarios que desea obtener (entre 1 y 10): "))
    if 1 <= n <= 10:
        break
    else:
        print("Error: El número debe estar entre 1 y 10.")
        
url = f'https://jsonplaceholder.typicode.com/users?_limit={n}'
response = requests.get(url)
users =response.json
print(users)

            
#dividirusers 
usersVowels = []
usersConsonants = []
    
for user in users:
    name = user['name']
    if name[0].lower() in 'aeiou':  
        usersVowels.append(user)
    else:
        usersConsonants.append(user)

#guardarusers





def listusers (users) :
    if users['address'] == ['city'] or ['street']:
        usersfilter = filter(users)
    
    usersfilter
    
    
    
    
def busquedapost (users, word):
    num = int(input('ingres un id del 1 al 10'))
    word = input('digame una palabra clave ')
    
    url = f'https://jsonplaceholder.typicode.com/posts?userId={num}'
    response = requests.get(url)
    post =response.json
    print(users)
    