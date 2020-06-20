import os

input('\nMake Sure you are Connected with Active Hotspot and have the WiFi turned ON...\n')

show = os.popen('netsh wlan show network mode=bssid').read()
count = int(show.split('\n')[2][10])

namelist = []
for i in range(count):
    name = show.split(': ')[2+10*i].split('\n')[0]
    namelist.append(name)

while True:
    print('\n>>> ----------------(press CTRL + C to exit CMD)--------------- Menu :')

    print('\n1). Show WiFi nearby')
    print('2). Connect to WiFi')
    print('3). Disconnect to current WiFi')

    choice = input('\nEnter your Choice : ')
    if choice == '1':
        print(show)
        
    elif choice == '2':
        for j,k in enumerate(namelist):
            print(j+1, '). ',  k)
        
        try:
            index = int(input('\nEnter option : '))-1
            connect = os.popen(('netsh wlan connect name="' + namelist[index] + '"')).read()
            print(connect)
        except Exception as e:
            print(e)
    
    elif choice == '3':
        disconnect = os.popen('netsh wlan disconnect').read()
        print(disconnect)