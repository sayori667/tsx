import platform
import os


os_name = platform.system()

if os_name == "Linux":
    distro = ' '.join(platform.linux_distribution())
else:
    distro = "Non Linux"


def requirements():

    if os_name == 'Windows':
        os.system('python -m pip install colorama')
        os.system('python -m pip install whois')
        os.system('python -m pip install requests')
        os.system('python -m pip install datetime')
        os.system('python -m pip install bs4')
        os.system('python -m pip install discord')
        os.system('python -m pip install discord.py')
        os.system('python -m pip install googlesearch-python')
        os.system('python -m pip install tls-client')

    elif distro == 'Arch Linux' and 'Manjaro Linux'  and 'Antergos' and 'Endeavour OS':
        os.system('pacman -S python-colorama')
        os.system('pacman -S python-whois')
        os.system('pacman -S python-requests')
        os.system('pacman -S python-datetime')
        os.system('pacman -S python-bs4')
        os.system('pacman -S python-discord')
        os.system('pacman -S python-discord.py')
        os.system('pacman -S python-googlesearch-python')
        os.system('pacman -S python-tls-client')
        
    else :
        os.system('sudo python3 -m pip install colorama')
        os.system('sudo python3 -m pip install whois')
        os.system('sudo python3 -m pip install requests')
        os.system('sudo python3 -m pip install datetime')
        os.system('sudo python3 -m pip install bs4')
        os.system('sudo python3 -m pip install discord')
        os.system('sudo python3 -m pip install discord.py')
        os.system('sudo python3 -m pip install googlesearch-python')
        os.system('sudo python3 -m pip install tls-client')