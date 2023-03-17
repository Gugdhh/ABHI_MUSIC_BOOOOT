from AnonX import app
from pyrogram import filters


@app.on_message(filters.command('id'))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        message.reply_text(
            f"🍁ʏᴏᴜʀ ɪᴅ🍁:{reply.from_user.first_name}: {reply.from_user.id}\n🥀ɢʀᴏᴜᴘ ɪᴅ🥀: {message.chat.id}"
        )
    else:
        message.reply(
            f"🍁ʏᴏᴜʀ ɪᴅ🍁: {message.from_user.id}\n🥀ɢʀᴏᴜᴘ ɪᴅ🥀: {message.chat.id}"
       )
