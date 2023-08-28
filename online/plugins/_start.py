from online.core.clients import bot
from online.helpers.sudoers import one
from online.helpers.button import keyboard
from pyrogram import Client, filters
from pyrogram.types import Message
start_text = """
▰▱▱▱▱▱▱▱▱▱▱▱▱▱▱▰
𝙏𝙓𝙏 𝙁𝙞𝙡𝙚 𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙𝙚𝙧 𝘼𝙣𝙙 𝙀𝙭𝙩𝙧𝙖𝙘𝙩𝙤𝙧 𝘽𝙤𝙩.
▰▱▱▱▱▱▱▱▱▱▱▱▱▱▱▰

➭ 𝗣𝗿𝗲𝘀𝘀 /Pyro 𝗧𝗼 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗟𝗶𝗻𝗸𝘀 𝗟𝗶𝘀𝘁𝗲𝗱. 𝗦𝗲𝗻𝗱 𝗧𝗫𝗧 𝗙𝗶𝗹𝗲 𝗙𝗢𝗥𝗠𝗔𝗧 {𝗙𝗶𝗹𝗲𝗡𝗮𝗺𝗲 : 𝗙𝗶𝗹𝗲𝗟𝗶𝗻𝗸}

➭ 𝗣𝗿𝗲𝘀𝘀 /Cancel 𝗧𝗼 𝗖𝗮𝗻𝗰𝗲𝗹 𝗔𝗹𝗹 𝗧𝗵𝗲 𝗥𝘂𝗻𝗻𝗶𝗻𝗴 𝗧𝗮𝘀𝗸𝘀 𝗢𝗻 𝗕𝗼𝘁.

➭ 𝗣𝗿𝗲𝘀𝘀 /Restart 𝗧𝗼 𝗥𝗲𝘀𝘁𝗮𝗿𝘁 𝗧𝗵𝗲 𝗕𝗼𝘁.

➭ 𝗣𝗿𝗲𝘀𝘀 /PW 𝗧𝗼 𝗘𝘅𝘁𝗿𝗮𝗰𝘁 𝗔𝗹𝗹 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗮𝗯𝗹𝗲 𝗟𝗶𝗻𝗸𝘀 𝗨𝘀𝗶𝗻𝗴 𝗔𝗨𝗧𝗛 𝗖𝗢𝗗𝗘

➭ 𝗣𝗿𝗲𝘀𝘀 /Apni 𝗧𝗼 𝗘𝘅𝘁𝗿𝗮𝗰𝘁 𝗔𝗹𝗹 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗮𝗯𝗹𝗲 𝗟𝗶𝗻𝗸𝘀 𝗼𝗳 𝗔𝗽𝗻𝗶 𝗞𝗮𝗸𝘀𝗵𝗮 𝗨𝘀𝗶𝗻𝗴 𝗧𝗼𝗸𝗲𝗻

➭ 𝗣𝗿𝗲𝘀𝘀 /Logink 𝗧𝗼 𝗘𝘅𝘁𝗿𝗮𝗰𝘁 𝗔𝗹𝗹 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗮𝗯𝗹𝗲 𝗟𝗶𝗻𝗸𝘀 𝗼𝗳 𝗞𝗵𝗮𝗻 𝗦𝗶𝗿 𝗨𝘀𝗶𝗻𝗴 𝗔𝗨𝗧𝗛 𝗖𝗢𝗗𝗘

➭ 𝗣𝗿𝗲𝘀𝘀 /Khazana 𝗧𝗼 𝗘𝘅𝘁𝗿𝗮𝗰𝘁 𝗔𝗹𝗹 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗮𝗯𝗹𝗲 𝗟𝗶𝗻𝗸𝘀 𝗨𝘀𝗶𝗻𝗴 𝗔𝗨𝗧𝗛 𝗖𝗢𝗗𝗘 𝗞𝗛𝗔𝗭𝗔𝗡𝗔
▰▱▱▱▱▱▱▱▱▱▱▱▱▱▱▰"""

@bot.on_message(filters.command(["start"]))
async def start(bot: Client, m: Message):
    if not one(m.from_user.id):
        return await m.reply_photo(
            photo="https://graph.org/file/f60051408d17fd505fa11.jpg", caption=f"» Hello i am online class bot which help you to **Extract** and **Download** video of Physics Wallah / Apni Kaksha / Khan Gs\n\n• __This Bot is paid__\n\n**For 1 Month** : __Rs 99__\n**For 2 Month** : __Rs 149__\n\n**If you want to Buy Source Code ** \n__Contact Now__",
            reply_markup=keyboard,
        )
    await m.reply_text(start_text)
