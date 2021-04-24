from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵
       https://telegra.ph/file/a8636eb554e5289050124.jpg

I can play music in your group's voice call. Add me to your group for best song 

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                   [
                    InlineKeyboardButton(
                        "commands", url="https://telegra.ph/%F0%9D%90%8F%F0%9D%90%9A%F0%9D%90%AD%F0%9D%90%AB%F0%9D%90%A2%F0%9D%90%9C%F0%9D%90%A2%F0%9D%90%9A%F0%9D%90%97%F0%9D%90%A6%F0%9D%90%AE%F0%9D%90%AC%F0%9D%90%A2%F0%9D%90%9C-04-24",
                    )
                 ],

                   [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/Patricia_support"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/Patricia_updates"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/patriciaXmusic_bot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/Patricia_updates")
                ]
            ]
        )
   )


