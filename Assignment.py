import requests
import json

option = int(0)
url = ""
headers = ""
res = ""
data = ""
i = int(0)

accessToken = input("Please input the access token:")

while option != 5:
        print("=" * 128)
        print("Test connection to Webex Server (0)")
        print("User Information (1)")
        print("List room (2)")
        print("Create room (3)")
        print("Send Message (4)")
        print("Exit (5)")
        option = int(input("Please choose option from above using the number given:"))
        print("=" * 128)
        
        if option == 0:
            url = 'https://webexapis.com/v1/people/me'

            headers = {
            'Authorization': 'Bearer {}'.format(accessToken)
            }

            res = requests.get(url, headers=headers)

            if res.status_code == 200:
                print("Connection to the webex server is success")
            
            else:
                 print("Connection error. Please use a correct access token or use a new access token")
                 accessToken = input("Please input the access token:")
        
        elif option == 1:
            url = 'https://webexapis.com/v1/people/me'

            headers = {
            'Authorization': 'Bearer {}'.format(accessToken)
            }

            res = requests.get(url, headers=headers)

            if res.status_code == 200:
                data = res.json()
                print("=" * 128)
                
                if 'id' in data:
                    userId = data.get('id', '')
                    email = data.get('emails', [''])[0]
                    displayed_name = data.get('displayName', '')

                    print('User ID:', userId)
                    print('Email:', email)
                    print('Displayed Name:', displayed_name)
             
        elif option == 2:
            url = 'https://webexapis.com/v1/rooms'

            headers = {
            'Authorization': 'Bearer {}'.format(accessToken),
            'Content-Type': 'application/json'
            }

            params={'max': '5'}

            res = requests.get(url, headers=headers, params=params)

            if res.status_code == 200:

                data = res.json()
                
                print('_' * 120)
                if 'items' in data:
                    for item in data['items']:
                        id = item.get('id', '')
                        title = item.get('title', '')
                        lastAct = item.get('lastActivity', '')
                        dateCreate = item.get('created', '')
            
                        print('id:', id)
                        print('Title:', title)
                        print('Last Activity:', lastAct)
                        print('Date Created:', dateCreate)
                        print('_' * 120)
            
        elif option == 3:
            NewRoom = input("Please insert the name for the new room:")
            
            url = 'https://webexapis.com/v1/rooms'
            
            headers = {
            'Authorization': 'Bearer {}'.format(accessToken),
            'Content-Type': 'application/json'
            }

            params={'title': NewRoom}
            
            res = requests.post(url, headers=headers, json=params)
            
            if res.status_code == 200:
                print("New room has been created")
            
            else:
                 print("Error in creating a room")
        
        elif option == 4:
            url = 'https://webexapis.com/v1/rooms'

            headers = {
            'Authorization': 'Bearer {}'.format(accessToken),
            'Content-Type': 'application/json'
            }

            params={'max': '5'}

            res = requests.get(url, headers=headers, params=params)

            if res.status_code == 200:

                data = res.json()
                
                if 'items' in data:
                    selectedRoom = []
                    for item in data['items']:
                        id = item.get('id', '')
                        title = item.get('title', '')

                        i += 1
                        selectedRoom.append(id)
                        print(title, "(", i, ")")
                        
                    ChooseRoom = int(input("Please choose the room to send a message using the number given:"))
                    if 1 <= ChooseRoom <= 5:
                        IdSelectRoom = selectedRoom[ChooseRoom - 1]
                        message = input("Enter the message to send to the selected room: ")
                        
                        url = 'https://webexapis.com/v1/messages'

                        params = {'roomId': IdSelectRoom, 'markdown': message}

                        res = requests.post(url, headers=headers, json=params)
                        
                        print("Message has been send")
                    else:
                        print("Invalid room")      
            else:
                print ("No room has been found")        