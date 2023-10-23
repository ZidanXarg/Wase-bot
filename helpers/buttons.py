from pyrogram.types import ( InlineKeyboardButton ,
                            InlineKeyboardMarkup ,
                            ReplyKeyboardMarkup ,
                            ReplyKeyboardMarkup)
from config import Variables                          
Var = Variables()

class Buttons:
    
    WELCOME_MARKUP = InlineKeyboardMarkup(
                                    [
                                        [
                                        InlineKeyboardButton("🍁ቻናል🍁",url="https://t.me/Wase_Records")
                                        ],
                                        [    
                                        
                                            InlineKeyboardButton("🍁ግሩፕ🍁",url="https://t.me/Wase_Records_Group")
                                        ],
                                        [
                                        InlineKeyboardButton("🍁የቦቱ ባለቤት🍁",url="https://t.me/The_Hacker_Person")
                                        ],
                                        [
                                        InlineKeyboardButton("🍁ማዘዣዎች🍁",callback_data="help")
                                        ]
                                    ]
                                    )
    
    
    HELP_KEYBOARD = ReplyKeyboardMarkup(
                                    [
                                        [
                                        ('💵 ቀሪ ሂሳብ')
                                        ],
                                        [    
                                        ('🍁ማዘዣዎች🍁'),
                                        ('🎁 ሂሳብ ለመሙላት')
                                        ],
                                        [
                                        ('🙌🏻 መጋበዣ ሊንክ')
                                        ],
                                        [ ('በ ካርድ'),
                                          ('በ ቴሌብር')
                                        ]
                                         
                                    ],
                                    resize_keyboard=True
                                    )
    FORCE_MARKUP = InlineKeyboardMarkup(
                                    [
                                        [
                                        InlineKeyboardButton("✅ለመቀላቀል", url="https://t.me/+qZXWNtb0C0xiNjU0")
                                        ]
                                    ]
                                    )
    FORCE_INVITED = [
                      [
                        InlineKeyboardButton("✅ለመቀላቀል", url="https://t.me/+qZXWNtb0C0xiNjU0")
                     ]
                  ]
    HELP_MARKUP = InlineKeyboardMarkup(
                                    [
                                        [
                                        InlineKeyboardButton("Instruction",callback_data = "instruct")
                                        ],
                                        [    
                                            InlineKeyboardButton("🍁ግሩፓችን ላይ ለመጠየቅ🍁",url="https://t.me/wase_records_group"),
                                        ],
                                        [
                                        InlineKeyboardButton("🍁ተደጋጋሚ ጥያቄዎች!🍁",callback_data='faq')
                                        ]
                                    ]
                                    )
    ACCEPTANCE = InlineKeyboardMarkup(
                                    [
                                        [
                                        InlineKeyboardButton("accept",callback_data='approved')
                                        ],
                                        [
                                        InlineKeyboardButton("decline",callback_data='denied')
                                        ]
                                    ]
                                    )
                                    
    def film_selection (file_instances):
        pages = [] ; button_limit = 1 ; line_limit = 10
        for i in file_instances :
            button = InlineKeyboardButton(file_instances.get(i)[0], url =("https://t.me/wase_records_bot?start="+i))
            if len(pages) == 0 or len(pages[-1]) >= line_limit and len(pages[-1][-1]) >= button_limit:
                pages.append([[button]])
            elif len(pages[-1]) == 0 or len(pages[-1][-1]) >= button_limit:
                pages[-1].append([button])
            else:
                pages[-1][-1].append(button)
        page_no = 0
        no_buttons = []
        if len(pages) == 1:
            return pages
        for page in pages:
            page_no += 1
            page_buttons = []
            if page == pages[0]:
                page_buttons.append(
                    InlineKeyboardButton(
                        text="ቀጣይ ⏩",
                        callback_data="tpage+"+str(page_no+1)
                    )
                )
            elif page == pages[-1]:
                page_buttons.append(
                    InlineKeyboardButton(
                        text="⏪ ለመመለስ",
                        callback_data="tpage+"+str(page_no-1)
                    )
                )
            else:
                page_buttons.append(
                    InlineKeyboardButton(
                        text="⏪ ለመመለስ",
                        callback_data="tpage+"+str(page_no-1)
                    )
                )
                page_buttons.append(
                    InlineKeyboardButton(
                        text="ቀጣይ ⏩",
                        callback_data="tpage+"+str(page_no+1)
                    )
                )
            pages[page_no-1].append(page_buttons)
            no_buttons.append(
                InlineKeyboardButton(
                    text=str(page_no),
                    callback_data="tpage+"+str(page_no)
                )
            )
            pages[page_no-1].append(no_buttons)
        return pages        
        
    
