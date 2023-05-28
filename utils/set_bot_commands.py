from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("weather", "показать погоду"),
            types.BotCommand("horo", "составить гороскоп"),
            types.BotCommand("jokes", "анекдоты"),
            types.BotCommand("dubai", 'показать дубай'),
            types.BotCommand("cat", "специально для Полины"),
            types.BotCommand("game", "игры"),
            types.BotCommand('mute', 'хихихиха'),
            types.BotCommand('sovmestimost', 'совместимость знаков зодиака')
        ]
    )
