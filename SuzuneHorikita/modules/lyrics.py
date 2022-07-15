import os

from youtubesearchpython import VideosSearch

from pytube import YouTube

from lyricsgenius import genius

from pyrogram import filters

from pyrogram.types import Message

from pyrogram.errors.exceptions import MessageNotModified

from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong

from SuzuneHorikita import GENIUS_API_TOKEN as GENIUS_API, pbot as pgram

  

  ### LYRICS ###

api = genius.Genius(GENIUS_API,verbose=False)

@pgram.on_message(filters.command(['lyrics','lyric'],prefixes=['/','!']) 

    & (filters.group | filters.private))

async def lyrics(client:pgram, msg: Message):

    if len(msg.command) == 1:

        return await msg.reply(

            text='heh still noob?', 

        )

    r_text = await msg.reply("mf c'mon waito for some real time bish..")

    song_name = msg.text.split(None, 1)[1]

    lyric = api.search_song(song_name)

    if lyric is None:return await r_text.edit('no lyrics?')

    lyric_title = lyric.title

    lyric_artist = lyric.artist

    lyrics_text = lyric.lyrics

    try:

        await r_text.edit_text(f'__--**{lyric_title}**--__\n__{lyric_artist}\n__\n\n__{lyrics_text}__')

    except MessageTooLong:

        with open(f'downloads/{lyric_title}.txt','w') as f:

            f.write(f'{lyric_title}\n{lyric_artist}\n\n\n{lyrics_text}')

        await r_text.edit_text('ayo wtf')

        await msg.reply_chat_action(

            action='upload_document'

        )

        await msg.reply_document(

            document=f'downloads/{lyric_title}.txt',

            thumb='src/d.jpg',

            caption=f'\n__--{lyric_title}--__\n__{lyric_artist}__'

        )

        await r_text.delete()

        

        

        os.remove(f'downloads/{lyric_title}.txt')
