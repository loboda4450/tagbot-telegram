import asyncio
import logging

import yaml

from telethon import TelegramClient
from telethon.events import NewMessage

from utils.chat_aux import has_file
from utils.user import add_user
from utils.artist import add_artist


async def main(config):
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=config['log_level'])
    logger = logging.getLogger(__name__)
    client = TelegramClient(**config['telethon_settings'])
    print("Starting")
    await client.start(bot_token=config['bot_token'])
    print("Started")

    @client.on(NewMessage(pattern='/subscribe'))
    async def subscribe(event):
        if event.is_group:
            add_user(event)

    @client.on(NewMessage(func=has_file))
    async def file(event):
        add_artist(event)

    async with client:
        print("Good morning!")
        await client.run_until_disconnected()


if __name__ == '__main__':
    with open("config.yml", 'r') as f:
        config = yaml.safe_load(f)
        asyncio.get_event_loop().run_until_complete(main(config=config))
