import asyncio
from aiogram import Bot, Dispatcher
import logging
from config_reader import config
from handlers import bot_message, user_commands, callback_handlres, state_handlres
from midlwares.antiflood import AntiFloodMiddleware
from midlwares.badwordshandler import MultiLangBadWordsMiddleware




async def main() -> None:
    bot = Bot(config.bot_token.get_secret_value())
    dp = Dispatcher()

    dp.message.middleware(MultiLangBadWordsMiddleware(file_paths=["badwordsru.json"]))

    dp.message.middleware(AntiFloodMiddleware(0.2))

   
    dp.include_routers(
        user_commands.router,
        callback_handlres.router,
        bot_message.router,
        state_handlres.router
    )

    
    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exiting')