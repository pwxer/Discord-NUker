import configparser
import io
from concurrent.futures import ThreadPoolExecutor
from pystyle import Center, Colorate, Colors
import os
import time
import requests
import random

config = configparser.ConfigParser()
config.read('config.txt')

prefix = variable_value = config.get('config', 'prefix')

def spam(msg, webhook):
    print(Colorate.Vertical(Colors.cyan_to_blue, '-> Use proxies from proxies.txt? [Y/n] '))
    pc = input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
    def spam_msg():
        nonlocal pc
        i = 0
        proxy = None
        if pc == 'Y':
            with open('proxies.txt', 'r') as f:
                proxies = f.read().splitlines()
                i = len(proxies)
                if i == 0:
                    print(Colorate.Vertical(Colors.cyan_to_blue, f'No proxies found in proxies.txt, running without proxies.'))
                    pc = 'n'
                else:
                    # Create headers with Content-Type set to application/json
                    headers = {'Content-Type': 'application/json'}
                    proxy = {'https://': random.choice(proxies)}
        try:
            if pc == 'Y':
                response = requests.post(webhook, headers=headers, json={'content': msg}, proxies=proxy)
            else:
                response = requests.post(webhook, json={'content': msg})
            if response.status_code == 204:
                print(Colorate.Vertical(Colors.cyan_to_blue, f"Sent message {msg}"))
            elif response.status_code == 429:
                print(Colorate.Vertical(Colors.cyan_to_blue, f"You Are Being Rate Limited ({response.json()['retry_after']}ms)"))
                time.sleep(response.json()["retry_after"] / 1000)
            spam_msg()
        except Exception as e:
            print(str(e))
            input()
    spam_msg()

def send_msg():
    os.system('cls')
    print(Colorate.Vertical(Colors.cyan_to_blue, '-> Enter your webhooks complete link ( Enter 0 to go back to main menu ) '))
    webhook = input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
    if webhook == '0':
         webhook_menu()
    print(
        Center.XCenter(
            Colorate.Vertical(
                Colors.cyan_to_blue,   
                f"""
             ██████╗██╗      ██████╗ ██╗   ██╗██████╗ ███████╗    ██████╗  █████╗ ██╗   ██╗███╗   ███╗
            ██╔════╝██║     ██╔═══██╗██║   ██║██╔══██╗██╔════╝    ██╔══██╗██╔══██╗╚██╗ ██╔╝████╗ ████║
            ██║     ██║     ██║   ██║██║   ██║██║  ██║███████╗    ██║  ██║███████║ ╚████╔╝ ██╔████╔██║
            ██║     ██║     ██║   ██║██║   ██║██║  ██║╚════██║    ██║  ██║██╔══██║  ╚██╔╝  ██║╚██╔╝██║
            ╚██████╗███████╗╚██████╔╝╚██████╔╝██████╔╝███████║    ██████╔╝██║  ██║   ██║   ██║ ╚═╝ ██║
             ╚═════╝╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝
        """,
                1,
            )
        )
    )
    print((Colorate.Vertical(Colors.cyan_to_blue,f"""x,.-> Clouds Nuker v6.9
x,.-> made by r3xvert#0855

Prefix - "{prefix}"
Discord - https://discord.gg/WJGNdeQTCq
Note - Thanks for using my program
        """,1,)))
    print(Colorate.Vertical(Colors.cyan_to_blue, '-> Enter your message ( Enter 0 to go back )'))
    def choice1():
        choice = input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
        if choice == '0':
             webhook_menu()
        else:
            try:
                data = requests.post(webhook, json={'content': choice})
                if data.status_code == 204:
                    print(Colorate.Vertical(Colors.cyan_to_blue, f"Sent message {choice}"))
                choice1()
            except:
                print(Colorate.Vertical(Colors.cyan_to_blue, f'-> Could not send message {choice}'))
                choice1()

    choice1()

def webhook_menu():
    os.system('cls')
    print(
        Center.XCenter(
            Colorate.Vertical(
                Colors.cyan_to_blue,   
                f"""
             ██████╗██╗      ██████╗ ██╗   ██╗██████╗ ███████╗    ██████╗  █████╗ ██╗   ██╗███╗   ███╗
            ██╔════╝██║     ██╔═══██╗██║   ██║██╔══██╗██╔════╝    ██╔══██╗██╔══██╗╚██╗ ██╔╝████╗ ████║
            ██║     ██║     ██║   ██║██║   ██║██║  ██║███████╗    ██║  ██║███████║ ╚████╔╝ ██╔████╔██║
            ██║     ██║     ██║   ██║██║   ██║██║  ██║╚════██║    ██║  ██║██╔══██║  ╚██╔╝  ██║╚██╔╝██║
            ╚██████╗███████╗╚██████╔╝╚██████╔╝██████╔╝███████║    ██████╔╝██║  ██║   ██║   ██║ ╚═╝ ██║
             ╚═════╝╚══════╝ ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝     ╚═╝
        """,
                1,
            )
        )
    )
    print((Colorate.Vertical(Colors.cyan_to_blue,f"""x,.-> Clouds Nuker v6.9
x,.-> made by r3xvert#0855

Prefix - "{prefix}"
Discord - https://discord.gg/WJGNdeQTCq
Note - Thanks for using my program
        """,1,)))
    print((Colorate.Vertical(Colors.cyan_to_blue,f"""[ Webhook Nuker / Select a 0ption ]
---------------------------------------------------------

-> 0 - Go back to main menu
-> 1 - Send a message
-> 2 - Spam webhook
-> 3 - Delete webhook
-> 4 - Check if webhook is valid

---------------------------------------------------------
        """,1,)))
    def choice1():
        choice = input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
        if choice == '0':
            os.system('python launcher.py')
        if choice == '1':
             send_msg()
        if choice == '2':
            print(Colorate.Vertical(Colors.cyan_to_blue, '-> Enter your webhooks complete link ( Enter 0 to go back to main menu ) '))
            webhook = input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
            if webhook == '0':
                 webhook_menu()
            print(Colorate.Vertical(Colors.cyan_to_blue, '-> Enter the message to spam (Enter 0 to go back)'))
            message = input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
            if message == '0':
                 webhook_menu()
            spam(message, webhook)
        if choice == '3':
            # Set up the webhook URL and headers
            print(Colorate.Vertical(Colors.cyan_to_blue, '-> Enter your webhooks complete link ( Enter 0 to go back to main menu ) '))
            webhook_url = input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
            headers = {'Content-type': 'application/json'}

            # Send the DELETE request to delete the webhook
            response = requests.delete(webhook_url, headers=headers)

            # Check the response status code to ensure the webhook was deleted successfully
            if response.status_code == 204:
                print(Colorate.Vertical(Colors.cyan_to_blue, "Webhook deleted successfully!"))
                choice1()
            else:
                print(Colorate.Vertical(Colors.cyan_to_blue, f"Failed to delete webhook with status code {response.status_code}"))
                choice1()
        if choice  == '4':
            print(Colorate.Vertical(Colors.cyan_to_blue, '-> Enter your webhooks complete link ( Enter 0 to go back to main menu ) '))
            webhook_url = input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
            response = requests.get(webhook_url)
            if response.status_code == 200:
                print(Colorate.Vertical(Colors.cyan_to_blue, 'Webhook URL is valid'))
                input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
                webhook_menu()
            else:
                print(Colorate.Vertical(Colors.cyan_to_blue, 'Webhook URL is not valid'))
                input(Colorate.Vertical(Colors.cyan_to_blue, 'x,.->'))
                webhook_menu()
        else:
            choice1()

    choice1()

def webhook_start():
    webhook_menu()
