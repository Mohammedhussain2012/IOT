import telepot
token = '1345319812:AAGS2P9sCx78T8tsw1K44TMRDpNIqSSvWcw'
TelegramBot = telepot.Bot(token)
print(TelegramBot.getMe())
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        TelegramBot.sendMessage(chat_id, "You said '{}'".format(msg["text"]))


TelegramBot.message_loop(handle)
