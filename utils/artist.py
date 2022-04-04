from pony.orm import *
from telethon.events import NewMessage

from utils.logme import logme

db = Database("sqlite", "dev.sqlite", create_db=True)


class Artist(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)

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
def artist_exists(file_attrs: NewMessage) -> bool:
    return Artist.exists(name=file_attrs.performer)


@db_session
@logme
def add_artist(event: NewMessage) -> bool:
    try:
        artist = Artist(name=event.message.media.document.attributes[0].performer)
        return True
    except Exception as e:
        print(e)
        return False


db.generate_mapping(create_tables=True)
