import yt_dlp
url = input()
ydl_opts = \
    {
    'format': 'bestaudio',
    'writethumbnail':1,
    'outtmpl': '%(title)s.%(ext)s',
    'postprocessors':
    [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        },
        {
            "key": "EmbedThumbnail",
        }
    ],
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
    print("done!")