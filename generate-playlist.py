import spotipy
import spotipy.util as util
import datetime
from peewee import *

scope = 'playlist-modify-public'
token = util.prompt_for_user_token('121540093', scope)

db = SqliteDatabase('grovedb')

class Link(Model):
    user = CharField()
    message = TextField()
    time = DateTimeField()
    link = TextField()

    class Meta:
        database = db

db.connect()

if token:
    sp = spotipy.Spotify(auth=token)

    links = Link.select().where(Link.time >= datetime.date(2018, 3, 1))
    for link in links:
        if "spotify.com/track/" in link.link:
            track_id = link.link.split('/')[-1].split('?')[0]
            sp.user_playlist_add_tracks('121540093', '1gzUmIft7Az7RnoOT4AMEV', [track_id])
else:
    print("Can't get token for", '121540093')
