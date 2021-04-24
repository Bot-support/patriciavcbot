from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):

      await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I can play music in your group's voice call. Add me to your group for best song 

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                   [
                    InlineKeyboardButton(
                        "commands", url="https://t.me/Patricia_updates/9",
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


