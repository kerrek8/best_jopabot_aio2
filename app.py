from loader import *

import subprocess as sp
import requests
import handlers
from aiogram.utils.executor import start_webhook
from utils.set_bot_commands import set_default_commands

a = sp.Popen('C: && cd C:/Users/kerre/Desktop/ && ngrok http 8080', shell=True)

ngrok_url = 'http://localhost:4040/api/tunnels'
ngrok_response = requests.get(ngrok_url).json()
ngrok_tunnel = ngrok_response['tunnels'][0]
ngrok_address = ngrok_tunnel['public_url']


async def on_startup(dp):
    await set_default_commands(dp)
    webhook_uri = f'{ngrok_address}{webhook_path}'
    await bot.set_webhook(webhook_uri)


async def on_shutdown():
    await bot.delete_webhook()


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=webhook_path,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
    )
