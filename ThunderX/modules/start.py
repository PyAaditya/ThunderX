from telethon import events, Button
from config import MK1, MK2, MK3, MK4, MK5, MK6, MK7, MK8, MK9, MK10
from AltronX.modules.help import *
import telethon

PythonButton = [
        [
        Button.inline("• ᴄᴏᴍᴍᴀɴᴅs •", data="help_back")
        ],
        [
        Button.url("• ᴜᴘᴅᴀᴛᴇs •", "https://t.me/TechXcode"),
        Button.url("• sᴜᴘᴘᴏʀᴛ •", "https://t.me/ViolenceChitChat")
        ],
        [
        Button.url("• ʀᴇᴘᴏ •", "https://github.com/Pyaaditya/ThunderX")
        ]
        ]


@MK1.on(events.NewMessage(pattern="/start"))
@MK2.on(events.NewMessage(pattern="/start"))
@MK3.on(events.NewMessage(pattern="/start"))
@MK4.on(events.NewMessage(pattern="/start"))
@MK5.on(events.NewMessage(pattern="/start"))
@MK6.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK7.on(events.NewMessage(pattern="/start"))
@MK8.on(events.NewMessage(pattern="/start"))
@MK9.on(events.NewMessage(pattern="/start"))
@MK10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        BotName = AltBot.first_name
        BotId = AltBot.id
        TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\nɪ ᴀᴍ [{BotName}](tg://user?id={BotId})​ᴀ ᴘᴏᴡᴇʀғᴜʟʟ sᴘᴀᴍʙᴏᴛ ʜᴀᴠᴇ ᴀʟʟ ᴄᴏᴏʟ sᴘᴀᴍᴍɪɴɢ ғᴇᴀᴛᴜʀᴇs ʟɪᴋᴇ ʀᴀɪᴅ, ʀᴇᴘʟʏ ʀᴀɪᴅ , sᴘᴀᴍ , ᴘ*ʀɴ sᴘᴀᴍ**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : @PythonXCoder **\n\n"
        TEXT += f"» **ʙᴏᴛ ꜱᴘᴀᴍ ᴠᴇʀsɪᴏɴ :** `M3.2`\n"
        TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{telethon.__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                event.chat_id,
                "https://telegra.ph/file/bf912e9b85971d9e4f9ad.jpg",
                caption=TEXT, 
                buttons=PythonButton)
