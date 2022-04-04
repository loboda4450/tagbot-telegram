from pony.orm import *
from telethon.events import NewMessage

from utils.logme import logme

db = Database("sqlite", "dev.sqlite", create_db=True)


class Album(db.Entity):
    id = PrimaryKey(int, auto=True)
    artist = Required(str)
    title = Required(str)

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
def album_exists(event: NewMessage):
    return Album.exists(artist=event.message.media.document.attributes[0].performer,
                        title=event.message.media.document.attributes[0].title)


@db_session
@logme
def add_album(event: NewMessage):
    try:
        track = Album(name=event.message.media.document.attributes[0].performer)
        return True
    except Exception as e:
        print(e)
        return False


db.generate_mapping(create_tables=True)
