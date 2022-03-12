from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from keyboards.inline.call_backlar import dasturlash_call_back,kitob_call_back
inline_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📚Kitoblar",callback_data="Kitoblar"),
            InlineKeyboardButton(text="💻Dasturlash",callback_data="Dasturlash"),
        ],
        [
            InlineKeyboardButton(text="🔍Qidirish",switch_inline_query_current_chat=""),
            InlineKeyboardButton(text="⬅️Ulashish",switch_inline_query="\n Bu bot zo'r ekan,kirib ko'ring"),
        ],
        [
            InlineKeyboardButton(text="♾Oliy matematika kanaliga o'tish",url="https://t.me/Oliy_matematika_kanali"),
            InlineKeyboardButton(text="🔜Admin bilan bog'lanish",url="https://t.me/Allohumma_solli_vas_sallim"),
        ],
        [
            InlineKeyboardButton(text="🔙Ortga",callback_data="ortga"),
        ],
    ],

)
#######Kurslar
Dasturlash_menu = InlineKeyboardMarkup(row_width=1)
python = InlineKeyboardButton(text="🐍Python",callback_data=dasturlash_call_back.new(name='python'))
Dasturlash_menu.insert(python)
django = InlineKeyboardButton(text="🌐Django",callback_data=dasturlash_call_back.new(name='django'))
Dasturlash_menu.insert(django)
bot = InlineKeyboardButton(text="🤖Telegram bot",callback_data=dasturlash_call_back.new(name='bot'))
Dasturlash_menu.insert(bot)
ortga = InlineKeyboardButton(text="🔙Ortga",callback_data="ortga")
Dasturlash_menu.insert(ortga)
####kitoblar
Kitoblar_menu = InlineKeyboardMarkup(row_width=1)
matematika1 = InlineKeyboardButton(text="📚Matematika1",callback_data=kitob_call_back.new(name='matematika1'))
Kitoblar_menu.insert(matematika1)
matematika2 = InlineKeyboardButton(text="📚Matematika2",callback_data=kitob_call_back.new(name='matematika2'))
Kitoblar_menu.insert(matematika2)
dasturlash = InlineKeyboardButton(text="📚Dasturlash",callback_data=kitob_call_back.new(name='dasturlash'))
Kitoblar_menu.insert(dasturlash)
Kitoblar_menu.insert(ortga)
######

python_tugma = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Sariq dev:',url='https://python.sariq.dev/'),
            InlineKeyboardButton(text="🔙Ortga",callback_data="ortga"),
        ],
    ]
)

django_tugma = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Sariq dev:',url='https://www.youtube.com/channel/UCWIzlxf_d6fmt2XKTcBANtQ'),
            InlineKeyboardButton(text="🔙Ortga",callback_data="ortga")
        ],
    ]
)

bot_tugma = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Sariq dev:',url='https://www.youtube.com/watch?v=1WRJQV3-lws'),
            InlineKeyboardButton(text="🔙Ortga",callback_data="ortga")
        ],
    ]
)



