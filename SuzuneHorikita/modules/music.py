import datetime
import os
from asyncio import get_running_loop
from functools import partial
from io import BytesIO

from pyrogram import filters
from pytube import YouTube
from requests import get

from SuzuneHorikita import aiohttpsession as session
from SuzuneHorikita import pbot as pgram
from SuzuneHorikita import arq
from SuzuneHorikita.core.decorators.errors import capture_err
from SuzuneHorikita.utils.pastebin import paste

is_downloading = False


def download_youtube_audio(arq_resp):
    r = arq_resp.result[0]

    title = r.title
    performer = r.channel

    m, s = r.duration.split(":")
    duration = int(
        datetime.timedelta(minutes=int(m), seconds=int(s)).total_seconds()
    )

    if duration > 1800:
        return

    thumb = get(r.thumbnails[0]).content
    with open("thumbnail.png", "wb") as f:
        f.write(thumb)
    thumbnail_file = "thumbnail.png"

    url = f"https://youtube.com{r.url_suffix}"
    yt = YouTube(url)
    audio = yt.streams.filter(only_audio=True).get_audio_only()

    out_file = audio.download()
    base, _ = os.path.splitext(out_file)
    audio_file = base + ".mp3"
    os.rename(out_file, audio_file)

    return [title, performer, duration, audio_file, thumbnail_file]


@pgram.on_message(filters.command("ytmusic") & ~filters.edited)
@capture_err
async def music(_, message):
    global is_downloading
    if len(message.command) < 2:
        return await message.reply_text("/ytmusic needs a query as argument")

    url = message.text.split(None, 1)[1]
    if is_downloading:
        return await message.reply_text(
            "Another download is in progress, try again after sometime."
        )
    is_downloading = True
    m = await message.reply_text(
        f"Downloading {url}", disable_web_page_preview=True
    )
    try:
        loop = get_running_loop()
        arq_resp = await arq.youtube(url)
        music = await loop.run_in_executor(
            None, partial(download_youtube_audio, arq_resp)
        )

        if not music:
            return await message.reply_text("[ERROR]: MUSIC TOO LONG")
        (
            title,
            performer,
            duration,
            audio_file,
            thumbnail_file,
        ) = music
    except Exception as e:
        is_downloading = False
        return await m.edit(str(e))
    await message.reply_audio(
        audio_file,
        duration=duration,
        performer=performer,
        title=title,
        thumb=thumbnail_file,
    )
    await m.delete()
    os.remove(audio_file)
    os.remove(thumbnail_file)
    is_downloading = False


# Funtion To Download Song
async def download_song(url):
    async with session.get(url) as resp:
        song = await resp.read()
    song = BytesIO(song)
    song.name = "a.mp3"
    return song


# Jiosaavn Music


@pgram.on_message(filters.command("song") & ~filters.edited)
@capture_err
async def jssong(_, message):
    global is_downloading
    if len(message.command) < 2:
        return await message.reply_text("/song requires an argument.")
    if is_downloading:
        return await message.reply_text(
            "Another download is in progress, try again after sometime."
        )
    is_downloading = True
    text = message.text.split(None, 1)[1]
    m = await message.reply_text("Searching...")
    try:
        songs = await arq.saavn(text)
        if not songs.ok:
            await m.edit(songs.result)
            is_downloading = False
            return
        sname = songs.result[0].song
        slink = songs.result[0].media_url
        ssingers = songs.result[0].singers
        sduration = songs.result[0].duration
        await m.edit("Downloading")
        song = await download_song(slink)
        await m.edit("Uploading")
        await message.reply_audio(
            audio=song,
            title=sname,
            performer=ssingers,
            duration=sduration,
        )
        await m.delete()
    except Exception as e:
        is_downloading = False
        return await m.edit(str(e))
    is_downloading = False
    song.close()


# Lyrics


@pgram.on_message(filters.command("lyrics") & ~filters.edited)
async def lyrics_func(_, message):
    if len(message.command) < 2:
        return await message.reply_text("**Usage:**\n/lyrics [QUERY]")
    m = await message.reply_text("**Searching**")
    query = message.text.strip().split(None, 1)[1]

    resp = await arq.lyrics(query)

    if not (resp.ok and resp.result):
        return await m.edit("No lyrics found.")

    song = resp.result[0]
    song_name = song['song']
    artist = song['artist']
    lyrics = song['lyrics']
    msg = f"**{song_name}** | **{artist}**\n\n__{lyrics}__"
          
    if len(msg) > 4095:
        msg = await paste(msg)
        msg = f"**LYRICS_TOO_LONG:** [URL]({msg})"
    return await m.edit(msg)
