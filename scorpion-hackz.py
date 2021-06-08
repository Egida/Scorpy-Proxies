import sys
import colorama
import os
import requests
import clipboard


# <------------------------------------------------------>
# Kodlayici z3ntl3 root (efdal)                          #
# Kimse calmasin gotunuzu yerim. Split Community OZEL    #
# <------------------------------------------------------>

os.system('clear')
print("Scorpion-Hackz.com Project")
design = """
       \033[31m\033[1m╔═╗╔═╗╔═╗╦═╗╔═╗╦╔═╗╔╗╔  \033[0m\033[31m╦ ╦╔═╗╔═╗╦╔═╔═╗
       \033[31m\033[1m╚═╗║  ║ ║╠╦╝╠═╝║║ ║║║║  \033[0m\033[31m╠═╣╠═╣║  ╠╩╗╔═╝
       \033[31m\033[1m╚═╝╚═╝╚═╝╩╚═╩  ╩╚═╝╝╚╝ \033[0m\033[31m ╩ ╩╩ ╩╚═╝╩ ╩╚═╝

             \033[0m\033[31m╔══════════════════════╗\033[0m
             \033[0m\033[31m║\033[0m  \033[1m\033[96mSoft\033[0mware \033[1m\033[96mD\033[0meve\033[1m\033[96mloper\033[0m: \033[1m\033[31m║\033[0m
             \033[0m\033[31m║\033[0m  z3ntl3root (Efdal)  \033[1m\033[31m║\033[0m
             \033[0m\033[31m╚\033[1m\033[31m══════════════════════╝\033[0m
"""

design2 = """ 

      \033[96m\033[1m[\033[31mTypes\033[96m]\033[0m\033[32m#\033[0m             \033[96m\033[1m[\033[31mCountries\033[96m]\033[0m\033[32m#\033[0m
      \033[1m\033[31m>\033[0m\033[96m>\033[1m\033[32m>\033[0m \033[96mHTTP\033[0m              \033[1m\033[31m>\033[0m\033[96m>\033[1m\033[32m>\033[0m \033[96mNL: Netherland\033[0m    
      \033[31m>\033[0m\033[96m\033[1m>\033[0m\033[32m> \033[0m\033[96mHTTPS\033[0m             \033[31m>\033[0m\033[96m\033[1m>\033[0m\033[32m> \033[0m\033[96mTR: Turkey\033[0m  
      \033[31m\033[1m>\033[0m\033[96m>\033[1m\033[32m> \033[0m\033[96mSOCKS4\033[0m            \033[1m\033[31m>\033[0m\033[96m>\033[1m\033[32m>\033[0m \033[96mRU: Russia\033[0m  
      \033[31m>\033[0m\033[96m\033[1m>\033[0m\033[32m> \033[0m\033[96mSOCKS5\033[0m            \033[31m>\033[0m\033[96m\033[1m>\033[0m\033[32m> \033[0m\033[96mUS: America\033[0m
      \033[31m\033[1m>\033[0m\033[96m>\033[1m\033[32m> \033[0m\033[96mALL\033[0m               \033[1m\033[31m>\033[0m\033[96m>\033[1m\033[32m>\033[0m \033[96mAnd all other countries\033[0m  


"""


logo = (str(design+design2))
print(logo)

indicator = ("\033[0m\033[31m┌──\033[96m(\033[31m\033[1mscorpion\033[0m💀\033[31m-hackz.com\033[1m\033[96m)\033[0m-[\033[0m\033[39m\033[1mz3ntl3root\033[0m\033[96m]\n\033[31m└─\033[32m#\033[96m ")
indicatorlogo = (str(indicator))

vallensBEYINSIZDIR = input(indicatorlogo + "Proxy Type: ")
ulkesecAB = input('\n' + indicatorlogo + "Country (yes-noo): ")



while True:
    if ulkesecAB == "yes":
        
        z3ntl3rootULKE = input('\n' + indicatorlogo + "Choose a country (Example: America is US): ")
        # kac tane proxy cektik?:
        APIulkeproxySAYISI = requests.get("https://api.proxyscrape.com?request=amountproxies&proxytype=" + vallensBEYINSIZDIR + "&timeout=7000&country=" + z3ntl3rootULKE)
        toplamPROXYv = (APIulkeproxySAYISI.text)
        print(str('\n' + indicatorlogo + 'Amount of the grabbed proxies: ' + toplamPROXYv))
        
        # proxy ne zaman guncellendi?:
        guncellenme = requests.get("https://api.proxyscrape.com?request=lastupdated&proxytype=" + vallensBEYINSIZDIR)
        guncellenmetext = (guncellenme.text)
        print(str('\n' + indicatorlogo + vallensBEYINSIZDIR + 'Last time when it was updated: ' + toplamPROXYv))

        # proxy leri cekmek:
        # APIurl :  https://api.proxyscrape.com?request=getproxies&proxytype=http&timeout=5000&country=US&anonymity=elite&ssl=yes

        proxycek1 = requests.get("https://api.proxyscrape.com?request=displayproxies&proxytype=" + vallensBEYINSIZDIR + "&timeout=7000&country=" + z3ntl3rootULKE)

        # printle

        proxyPRINT = (proxycek1.text)
        print(str('\n' + indicatorlogo + vallensBEYINSIZDIR + 'Succesful grabbed proxies:'))
        print(str('\n' + proxyPRINT))

        # klavyeye kopyala hepsini      
        clipboard.copy(proxyPRINT)
        print(str('\n' + indicatorlogo + 'Proxies copied!'))

        # ana menuye git
        menudon1 = input('\n' + indicatorlogo + 'Type something to go back to main-men (exit for exiting) ')
        if menudon1 == "exit":
            os.system('clear')
            print(logo)
            print("\n" + indicatorlogo + 'Your chosen option: ' + menudon1)
            os.system('python3 zentleroot.proxies.py')
    else:
        break


        

        # kac tane proxy cektik?:
APIulkeproxySAYISI1 = requests.get("https://api.proxyscrape.com?request=amountproxies&proxytype=" + vallensBEYINSIZDIR + "&timeout=7000")
toplamPROXYv1= (APIulkeproxySAYISI1.text)
print(str('\n' + indicatorlogo + 'Amount of grabbed proxies: ' + toplamPROXYv1))
        
        # proxy ne zaman guncellendi?:
guncellenme1 = requests.get("https://api.proxyscrape.com?request=lastupdated&proxytype=" + vallensBEYINSIZDIR)
guncellenmetext1 = (guncellenme1.text)
print(str('\n' + indicatorlogo + vallensBEYINSIZDIR + 'Proxies lastly updated: ' + toplamPROXYv1))

        # proxy leri cekmek:
        # APIurl :  https://api.proxyscrape.com?request=getproxies&proxytype=http&timeout=5000&country=US&anonymity=elite&ssl=yes

proxycek11 = requests.get("https://api.proxyscrape.com?request=displayproxies&proxytype=" + vallensBEYINSIZDIR + "&timeout=7000")

        # printle

proxyPRINT1 = (proxycek11.text)
print(str('\n' + indicatorlogo + vallensBEYINSIZDIR + 'Grabbed Proxies Succesful:'))
print(str('\n' + proxyPRINT1))

        # klavyeye kopyala hepsini
clipboard.copy(proxyPRINT1)
print(str('\n' + indicatorlogo + 'Copied the proxies!'))

        # ana menuye git
menudon1 = input('\n' + indicatorlogo + 'Go back to menu by typing something (to exit type = exit): ')

if menudon1 == "exit":
    os.system('clear')
    print(logo)
    print("\n" + indicatorlogo + 'Your chosen option: ' + menudon1)
    sys.exit()
else:
        os.system('python3 scorpion-hackz.py')





    
