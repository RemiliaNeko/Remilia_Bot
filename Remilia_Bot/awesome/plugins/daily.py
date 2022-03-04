import requests
from nonebot import on_command, CommandSession

@on_command('daily',aliases=('每日一句',))
async def daily(session:CommandSession):
    daily_send = await get_daily()
    await session.send(daily_send)

async def get_daily():
    daily_sentence = get_content()
    return daily_sentence

def get_content():
    url = 'http://open.iciba.com/dsapi/'
    res = requests.get(url)
    content = res.json()['content']
    return [content]