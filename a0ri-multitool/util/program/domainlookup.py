import whois
import subprocess
from util import utils
from util.program import *

async def domainlookup():
    print(utils.red + 'OUT OF SERVICE')


# A CAUSE D'UN PROBLEME AVEC LA LIB whois LE DOMAIN LOOKUP NE FONCTIONNE PLUS. JE N'AI PAS TROUVÉ D'AUTRE LIB DONC SI VOUS AVEZ DES CONSEILS : telegram : @ririmiaou1337    discord : saori.wx

######    print(utils.red + utils.domain_banner)
######    domain = input (f'{utils.red}[+] ENTER DOMAIN NAME : ') # EX : google.com
######    obj = whois.whois(domain)
######    obj2 = whois.extract_domain(domain)


######    print(f"""

######DOMAIN : {domain}

######{obj}

######REVERSE DNS : {obj2}


######""")

######    ask = input("DO YOU WANT TO PING THE IP ? [Y/N]: ")

######    if ask == 'Y':
######            command = (f'ping {domain}')
######            subprocess.run(command)
######
######    else:
######          pass
