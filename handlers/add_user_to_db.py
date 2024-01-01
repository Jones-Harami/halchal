# (c) @AbirHasan2005

from configs import Config
from handlers.database import db
from pyrogram import Client
from pyrogram.types import Message


async def add_user_to_database(bot: Client, cmd: Message):
    if not await db.is_user_exist(cmd.from_user.id):
        await db.add_user(cmd.from_user.id)
        if Config.LOG_CHANNEL is not None:
            await bot.send_message(
                int(Config.LOG_CHANNEL),
                f"#NEW_USER: \n\nNew User [{cmd.from_user.first_name}](tg://user?id={cmd.from_user.id}) started @{Config.BOT_USERNAME} !!"
            )

async def only_admin_access(bot: Client, cmd: Message):
    user_id = cmd.from_user.id

    # Check if user has admin access and file-saving permission
    if not Config.OTHER_USERS_CAN_SAVE_FILE or user_id not in Config.BOT_OWNER:
        if not Config.OTHER_USERS_CAN_SAVE_FILE:
            await cmd.reply_text("You do not have permission to save files.")
        elif user_id not in Config.BOT_OWNER:
            await cmd.reply_text("You do not have permission to perform this action.")
        return
