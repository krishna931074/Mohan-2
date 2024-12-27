import os
import re
import sys
import json
import time
import asyncio
import requests
import subprocess
import urllib.parse
import yt_dlp
import cloudscraper

import core as helper
from utils import progress_bar
from vars import API_ID, API_HASH, BOT_TOKEN
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput
from pytube import YouTube
from aiohttp import web

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Initialize the bot
bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

cookies_file_path = os.getenv("COOKIES_FILE_PATH", "youtube_cookies.txt")

# Define aiohttp routes
routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("https://text-leech-bot-for-render.onrender.com/")

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

async def start_bot():
    await bot.start()
    print("Bot is up and running")

async def stop_bot():
    await bot.stop()

async def main():
    if WEBHOOK:
        # Start the web server
        app_runner = web.AppRunner(await web_server())
        await app_runner.setup()
        site = web.TCPSite(app_runner, "0.0.0.0", PORT)
        await site.start()
        print(f"Web server started on port {PORT}")

    # Start the bot
    await start_bot()

    # Keep the program running
    try:
        while True:
            await bot.polling()  # Run forever, or until interrupted
    except (KeyboardInterrupt, SystemExit):
        await stop_bot()
    
@bot.on_message(filters.command(["start"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text(
       "饾悋饾悶饾惀饾惀饾惃 鉂わ笍\n\n鈼嗐�撯梿 鉂� (炉`路.赂赂.-> 掳潞   馃巰  饾挮饾挾饾搰饾捁饾憭饾憭饾搮馃挐饾挗饾挾饾搳饾搰饾捑馃挃饾憛馃挒饾捊饾捑饾搲  馃巰   潞掳 >-.赂赂.路`炉( 鉂� 鈩� 鈼嗐�撯梿\n\n鉂� I Am A Bot For Download Links From Your **.TXT** File And Then Upload That File Om Telegram So Basically If You Want To Use Me First Send Me 鉄� /GAURI Command And Then Follow Few Steps..", reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("鉁� 饾悏饾惃饾悽饾惂 饾悢饾惄饾悆饾悮饾惌饾悶 饾悅饾悺饾悮饾惂饾惂饾悶饾惀 鉁�" ,url=f"https://t.me/+gnmRbwms4jg0MDg1") ],
                    [
                    InlineKeyboardButton("鉁� Pradeep1804馃┓ 鉁�" ,url="https://t.me/Pradeep1804") ],
                    [
                    InlineKeyboardButton("馃 饾悈饾惃饾惀饾惀饾惃饾惏 饾悓饾悶 馃" ,url="https://t.me/+XJFAdIa3Vw5iN2M9") ]                               
            ]))

@bot.on_message(filters.command(["stop"]))
async def restart_handler(_, m):
    await m.reply_text("鈾� 饾悞饾惌饾惃饾惄饾惄饾悶饾惌 鈾�", True)
    os.execl(sys.executable, sys.executable, *sys.argv)



@bot.on_message(filters.command(["GAURI"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text('stranger 馃グ饾悡饾惃 饾悆饾惃饾惏饾惂饾惀饾惃饾悮饾悵 饾悁 饾悡饾惐饾惌 饾悈饾悽饾惀饾悶 饾悞饾悶饾惂饾悵 饾悋饾悶饾惈饾悶 鈴�')
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"
    file_name = os.path.splitext(os.path.basename(x))[0]

    try:
       with open(x, "r") as f:
           content = f.read().strip()
    
       lines = content.splitlines()
       links = []
    
       for line in lines:
           line = line.strip()
           if line:
               link = line.split("://", 1)
               if len(link) > 1:
                   links.append(link)
    
       os.remove(x)
       print(len(links))
    
    except:
           await m.reply_text("鈭� 饾悎饾惂饾惎饾悮饾惀饾悽饾悵 饾悷饾悽饾惀饾悶 饾悽饾惂饾惄饾惍饾惌.")
           os.remove(x)
           return
   
    await editable.edit(f"鈭� 饾悡饾惃饾惌饾悮饾惀 饾悑饾悽饾惂饾悿 饾悈饾惃饾惍饾惂饾悵 饾悁饾惈饾悶 馃敆** **{len(links)}**\n\n Stranger馃グ饾悞饾悶饾惂饾悵 饾悈饾惈饾惃饾惁 饾悥饾悺饾悶饾惈饾悶 饾悩饾惃饾惍 饾悥饾悮饾惂饾惌 饾悡饾惃 饾悆饾惃饾惏饾惂饾惀饾惃饾悮饾悵 饾悎饾惂饾悽饾惌饾悮饾惀 饾悽饾惉 **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)
    
    await editable.edit("**Enter Batch Name or send d for grabing from text filename.**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    if raw_text0 == 'd':
        b_name = file_name
    else:
        b_name = raw_text0
     
    await editable.edit("鈭� 饾悇饾惂饾惌饾悶饾惈 饾悇饾悶饾惉饾惃饾惀饾惍饾惌饾悽饾惃饾惂 馃幀\n鈽濸ardeep馃挐Gauri馃挃Rohit馃槜144,240,360,480,720,1080\nPlease Choose Quality")
    input2: Message = await bot.listen(editable.chat.id) 
    raw_text2 = input2.text
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080" 
        else: 
            res = "UN"
    except Exception:
            res = "UN"
    
    

    await editable.edit("**stranger馃挃Enter Your Name or send `de` for use default**")

    # Listen for the user's response
    input3: Message = await bot.listen(editable.chat.id)

    # Get the raw text from the user's message
    raw_text3 = input3.text

    # Delete the user's message after reading it
    await input3.delete(True)

    # Default credit message
    credit = "锔� 鈦伂鈦伄鈦�"
    if raw_text3 == 'de':
        CR = '@Pradeep1804馃┓ Strangerboy27_botstrangerboy'
    elif raw_text3:
        CR = raw_text3
    else:
        CR = credit
     
    await editable.edit("馃寗Crush馃槑 Now send the Thumb url if don't want thumbnail send no https://envs.sh/JLq.jpg")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)

    try:
        # Assuming links is a list of lists and you want to process the second element of each sublist
        for i in range(len(links)):
            original_url = links[i][1]

            # Replace parts of the URL as needed
            V = links[i][1].replace("file/d/","uc?export=download&id=")\
               .replace("www.youtube-nocookie.com/embed", "youtu.be")\
               .replace("?modestbranding=1", "")\
               .replace("/view?usp=sharing","")\
               .replace("youtube.com/embed/", "youtube.com/watch?v=")
            
            url = "https://" + V

            if "acecwply" in url:
                cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={raw_text2}]+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv --no-warning "{url}"'
                

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif 'videos.classplusapp' in url or "tencdn.classplusapp" in url or "webvideos.classplusapp.com" in url or "media-cdn-alisg.classplusapp.com" in url or "videos.classplusapp" in url or "videos.classplusapp.com" in url or "media-cdn-a.classplusapp" in url or "media-cdn.classplusapp" in url:
             url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MzgzNjkyMTIsIm9yZ0lkIjoyNjA1LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTcwODI3NzQyODkiLCJuYW1lIjoiQWNlIiwiZW1haWwiOm51bGwsImlzRmlyc3RMb2dpbiI6dHJ1ZSwiZGVmYXVsdExhbmd1YWdlIjpudWxsLCJjb3VudHJ5Q29kZSI6IklOIiwiaXNJbnRlcm5hdGlvbmFsIjowLCJpYXQiOjE2NDMyODE4NzcsImV4cCI6MTY0Mzg4NjY3N30.hM33P2ai6ivdzxPPfm01LAd4JWv-vnrSxGXqvCirCSpUfhhofpeqyeHPxtstXwe0'}).json()['url']

            elif '/master.mpd' in url:
             id =  url.split("/")[-2]
             url =  "https://d26g5bnklkwsh4.cloudfront.net/" + id + "/master.m3u8"

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]}'
                      
            if "/master.mpd" in url :
                if "https://sec1.pw.live/" in url:
                    url = url.replace("https://sec1.pw.live/","https://d1d34p8vz63oiq.cloudfront.net/")
                    print(url)
                else: 
                    url = url    

                print("mpd check")
                key = await helper.get_drm_keys(url)
                print(key)
                await m.reply_text(f"got keys form api : \n`{key}`")
          
            if "/master.mpd" in url:
                cmd= f" yt-dlp -k --allow-unplayable-formats -f bestvideo.{quality} --fixup never {url} "
                print("counted")

            

            if "edge.api.brightcove.com" in url:
                bcov = 'bcov_auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MjQyMzg3OTEsImNvbiI6eyJpc0FkbWluIjpmYWxzZSwiYXVzZXIiOiJVMFZ6TkdGU2NuQlZjR3h5TkZwV09FYzBURGxOZHowOSIsImlkIjoiZEUxbmNuZFBNblJqVEROVmFWTlFWbXhRTkhoS2R6MDkiLCJmaXJzdF9uYW1lIjoiYVcxV05ITjVSemR6Vm10ak1WUlBSRkF5ZVNzM1VUMDkiLCJlbWFpbCI6Ik5Ga3hNVWhxUXpRNFJ6VlhiR0ppWTJoUk0wMVdNR0pVTlU5clJXSkRWbXRMTTBSU2FHRnhURTFTUlQwPSIsInBob25lIjoiVUhVMFZrOWFTbmQ1ZVcwd1pqUTViRzVSYVc5aGR6MDkiLCJhdmF0YXIiOiJLM1ZzY1M4elMwcDBRbmxrYms4M1JEbHZla05pVVQwOSIsInJlZmVycmFsX2NvZGUiOiJOalZFYzBkM1IyNTBSM3B3VUZWbVRtbHFRVXAwVVQwOSIsImRldmljZV90eXBlIjoiYW5kcm9pZCIsImRldmljZV92ZXJzaW9uIjoiUShBbmRyb2lkIDEwLjApIiwiZGV2aWNlX21vZGVsIjoiU2Ftc3VuZyBTTS1TOTE4QiIsInJlbW90ZV9hZGRyIjoiNTQuMjI2LjI1NS4xNjMsIDU0LjIyNi4yNTUuMTYzIn19.snDdd-PbaoC42OUhn5SJaEGxq0VzfdzO49WTmYgTx8ra_Lz66GySZykpd2SxIZCnrKR6-R10F5sUSrKATv1CDk9ruj_ltCjEkcRq8mAqAytDcEBp72-W0Z7DtGi8LdnY7Vd9Kpaf499P-y3-godolS_7ixClcYOnWxe2nSVD5C9c5HkyisrHTvf6NFAuQC_FD3TzByldbPVKK0ag1UnHRavX8MtttjshnRhv5gJs5DQWj4Ir_dkMcJ4JaVZO3z8j0OxVLjnmuaRBujT-1pavsr1CCzjTbAcBvdjUfvzEhObWfA1-Vl5Y4bUgRHhl1U-0hne4-5fF0aouyu71Y6W0eg'
                url = url.split("bcov_auth")[0]+bcov
                
            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"
            
            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'

            elif "youtube.com" in url or "youtu.be" in url:
                cmd = f'yt-dlp --cookies youtube_cookies.txt -f "{ytf}" "{url}" -o "{name}".mp4'

            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:  
                
                cc = f'**馃帴 VIDEO ID: {str(count).zfill(3)}.\n\n馃搫 Title: {name1} {res} Pardeep馃挐Gauri馃挃Rohit.mkv\n\n<pre><code>馃敄 Batch Name: {b_name}</code></pre>\n\n馃摜 Extracted By : {CR}**'
                cc1 = f'**馃搧 FILE ID: {str(count).zfill(3)}.\n\n馃搫 Title: {name1} Pardeep馃挐Gauri馃挃Rohit.pdf \n\n<pre><code>馃敄 Batch Name: {b_name}</code></pre>\n\n馃摜 Extracted By : {CR}**'
                    
                
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        count+=1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                
                elif ".pdf" in url:
                    try:
                        await asyncio.sleep(4)
        # Replace spaces with %20 in the URL
                        url = url.replace(" ", "%20")
 
        # Create a cloudscraper session
                        scraper = cloudscraper.create_scraper()

        # Send a GET request to download the PDF
                        response = scraper.get(url)

        # Check if the response status is OK
                        if response.status_code == 200:
            # Write the PDF content to a file
                            with open(f'{name}.pdf', 'wb') as file:
                                file.write(response.content)

            # Send the PDF document
                            await asyncio.sleep(4)
                            copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                            count += 1

            # Remove the PDF file after sending
                            os.remove(f'{name}.pdf')
                        else:
                            await m.reply_text(f"Failed to download PDF: {response.status_code} {response.reason}")

                    except FloodWait as e:
                        await m.reply_text(str(e))
                        await asyncio.sleep(2)  # Use asyncio.sleep for non-blocking sleep
                        return  # Exit the function to avoid continuation

                    except Exception as e:
                        await m.reply_text(f"An error occurred: {str(e)}")
                        await asyncio.sleep(4)  # You can replace this with more specific
                        continue
                        
                          
                else:
                    Show = f"鉂娾煴 饾悆饾惃饾惏饾惂饾惀饾惃饾悮饾悵饾悽饾惂饾悹 鉄扁潑 禄\n\n馃搫 Title:- `{name}\n\n鈱� 饾悙饾惍饾惀饾悽饾惌饾惒 禄 {raw_text2}`\n\n**馃敆 饾悢饾悜饾悑 禄** `{url}`"
                    prog = await m.reply_text(f"**Downloading:-**\n\n**馃搫 Title:-** `{name}\n\nQuality - {raw_text2}`\n\n**link:**`{url}`\n\n **Bot Made By Pardeep馃挐Gauri馃挃Rohit **")
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                    f"鈱� 饾悆饾惃饾惏饾惂饾惀饾惃饾悮饾悵饾悽饾惂饾悹 馃槨馃が馃槇馃懣鈽狅笍馃挃饾悎饾惂饾惌饾悶饾惈饾惍饾惄饾惌饾悶饾悵\n\n鈱� 饾悕饾悮饾惁饾悶 禄 {name}\n鈱� 饾悑饾悽饾惂饾悿 禄 `{url}`"
                )
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("馃敯Stranger馃ぃ馃槄馃槀Complete ho gaya Pardeep馃挐Gauri馃挃Rohit Kar le sell ab馃敯")



bot.run()
if __name__ == "__main__":
    asyncio.run(main())
