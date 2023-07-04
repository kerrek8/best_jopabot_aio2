from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("weather", "показать погоду"),
            types.BotCommand("horo", "составить гороскоп"),
            types.BotCommand("jokes", "анекдоты"),
            types.BotCommand("kraken", "Выпустить кракена"),
            types.BotCommand("dubai", 'показать дубай'),
            types.BotCommand("cat", "специально для Полины"),
            types.BotCommand("lc", "Калькулятор молний (не нажимайте на эту кнопку, а просто введите команду)"),
            types.BotCommand("game", "игры"),
            types.BotCommand("city_game", "игра в города"),
            types.BotCommand('mute', 'хихихиха'),
            types.BotCommand('sovmestimost', 'совместимость знаков зодиака')
        ]
    )
