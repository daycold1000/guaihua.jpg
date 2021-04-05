

import re
from itertools import zip_longest

from nonebot.message import escape

from hoshino import Service
from hoshino.typing import CQEvent

from . import yinglish


sv2 = Service('淫语翻译')



def chs2yin(s, 淫乱度=1):
    return




@sv2.on_prefix('淦翻译')
async def ganfanyi(bot, ev: CQEvent):
    s = ev.message.extract_plain_text()
    if len(s) > 500:
        await bot.send(ev, '淦，内容太多，翻译不了', at_sender=True)
        return
    if len(s) < 1:
        await bot.send(ev, '淦！')
        return
    await bot.send(ev, yinglish.chs2yin(s))









#s = '不行，那里不行。'
#print(yinglish.chs2yin(s))
# 不行，那……那里不行……

#测试用的，无视（笑
