start_text = """
▰▱▱▱▱▱▱▱▱▱▱▱▱▱▱▰
𝙏𝙓𝙏 𝙁𝙞𝙡𝙚 𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙𝙚𝙧 𝘼𝙣𝙙 𝙀𝙭𝙩𝙧𝙖𝙘𝙩𝙤𝙧 𝘽𝙤𝙩.
▰▱▱▱▱▱▱▱▱▱▱▱▱▱▱▰
💠 𝙏𝙚𝙭𝙩/𝘽𝙖𝙩𝙘𝙝 𝙁𝙞𝙡𝙚 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨:
➭ /PW – Extract All Downloadable Links Using AUTH CODE
➭ /Khazana – Extract Links Using AUTH CODE KHAZANA
➭ /Apni – Extract Apni Kaksha Links Using Token
➭ /khangs – Extract Khan Sir Links Using AUTH CODE
➭ /cp – Extract Class Plus Download Links
➭ /exampur – Extract Exampur Download Links
➭ /patna – Extract Patna Downloads
➭ /infopw – Extract InfoPW Links
➭ /khan – Extract Khan Academy Downloads
➭ /adownload – Auto Download
➭ /pro_vision – Provision Batch
➭ /adda_pdf – Adda PDFs Extractor
➭ /pro_olive – Olive Board Extractor
➭ /pro_jw – JW Academy Extractor
➭ /top – Top Rankers
➭ /rozgar – Rojgar With Ankit

💠 𝙏𝙚𝙭𝙩 𝘿𝙤𝙬𝙣𝙡𝙤𝙖𝙙𝙚𝙧 / 𝙀𝙭𝙩𝙧𝙖𝙘𝙩𝙤𝙧:
➭ /Pyro – Download Listed Links via TXT File {FileName: FileLink}
➭ /Cancel – Cancel All Running Tasks

💠 𝙋𝙤𝙬𝙚𝙧 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨:
➭ /Restart – Restart the Bot

💠 𝘾𝙤𝙣𝙫𝙚𝙧𝙩𝙚𝙧:
➭ /taiyaric – Extract Taiyari Karlo JSON to TXT

💠 𝘾𝙤𝙧𝙚 𝘾𝙤𝙢𝙢𝙖𝙣𝙙𝙨:
➭ /shell – Run/install requirements [Owner Only]
➭ /eval – Execute Python Code [Owner Only]
▰▱▱▱▱▱▱▱▱▱▱▱▱▱▱▰
"""

pyro_text = """
➭ I Am The Fastest And Smoothest Bot On Telegram To UPLOAD Txt Files To Videos On Telegram
➭ Send : TXT (.txt) File
➭ Format : {Filename:FileLink}
➭ Developed By : AublicX_Robot
"""

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keyboard = InlineKeyboardMarkup([
     [
            InlineKeyboardButton(
                text="👑OWNER",
                url="https://t.me/Aublic",
            ),
    ],
    [
        InlineKeyboardButton("/PW", callback_data="PW"),
        InlineKeyboardButton("/Khazana", callback_data="Khazana"),
        InlineKeyboardButton("/Apni", callback_data="Apni")
    ],
    [
        InlineKeyboardButton("/khangs", callback_data="khangs"),
        InlineKeyboardButton("/cp", callback_data="cp"),
        InlineKeyboardButton("/exampur", callback_data="exampur")
    ],
    [
        InlineKeyboardButton("/patna", callback_data="patna"),
        InlineKeyboardButton("/infopw", callback_data="infopw"),
        InlineKeyboardButton("/khan", callback_data="khan")
    ],
    [
        InlineKeyboardButton("/adownload", callback_data="adownload"),
        InlineKeyboardButton("/pro_vision", callback_data="pro_vision"),
        InlineKeyboardButton("/adda_pdf", callback_data="adda_pdf")
    ],
    [
        InlineKeyboardButton("/pro_olive", callback_data="pro_olive"),
        InlineKeyboardButton("/pro_jw", callback_data="pro_jw"),
        InlineKeyboardButton("/top", callback_data="top")
    ],
    [
        InlineKeyboardButton("/rozgar", callback_data="rozgar"),
        InlineKeyboardButton("/Pyro", callback_data="Pyro"),
        InlineKeyboardButton("/Cancel", callback_data="Cancel")
    ],
    [
        InlineKeyboardButton("/Restart", callback_data="Restart"),
        InlineKeyboardButton("/taiyaric", callback_data="taiyaric")
    ],
    [
        InlineKeyboardButton("/shell", callback_data="shell"),
        InlineKeyboardButton("/eval", callback_data="eval")
    ]
])
