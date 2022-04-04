import asyncio

from telethon.events import NewMessage
from pony.orm import *
from utils.logme import logme

db = Database("sqlite", "dev.sqlite", create_db=True)


class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    userid = Required(int, size=64)
    artists_subscribed = Optional(StrArray, unique=True)
    chats_subscribed = Required(IntArray, unique=True)

    def before_insert(self):
        ...

    def after_insert(self):
        ...

    def before_delete(self):
        ...

    def after_delete(self):
        ...


@db_session
@logme
def add_user(event: NewMessage) -> bool:
    try:
        user = User(userid=event.sender.id, chats_subscribed=[event.chat.id])
        return True
    except Exception as e:
        print(e)
        return False


db.generate_mapping(create_tables=True)
