# OxyXmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""➼ Helloowww 👋 {message.from_user.first_name}! I can play music in voice chats of Telegeam Groups. I have a lot of cool feature that will amaze you!\n\n➼ Do you want me to play music in your Telegram groups'voice chats? Please click the " cσммαη∂s " button below to know how you can use me.\n\n➼ Use the buttons below to know more about me ❤️🔥\n\n➼ Contact my owner [🔥『 𝐒𝐎𝐔𝐋𝐌𝐀𝐓𝐄 』🔥](https://t.me/unknown_soulmate)\n\nA project by @unknown_soulmate""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "📜 cσммαη∂s 📜", url="https://telegra.ph/%E1%8F%AB%E1%8E%AE-%F0%9D%90%92%F0%9D%90%8E%F0%9D%90%94%F0%9D%90%8B%F0%9D%90%8C%F0%9D%90%80%F0%9D%90%93%F0%9D%90%84--%F0%9D%90%8C%F0%9D%90%94%F0%9D%90%92%F0%9D%90%88%F0%9D%90%82-05-12")
                  ],[
                    InlineKeyboardButton(
                        "❤️ αвσυт 『 𝐒𝐎𝐔𝐋𝐌𝐀𝐓𝐄 』 ❤️", url="https://t.me/unknownn_soulmate"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🔥 σғғιcιαℓ gяσυρ 🔥", url="https://t.me/joinchat/MK4RoLY0icRjZGQ1"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**➼ Music player is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔥 мү σωηεя 🔥", url="https://t.me/unknown_soulmate")
                ]
            ]
        )
   )

