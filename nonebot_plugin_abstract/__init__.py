from nonebot import on_command
from nonebot.log import logger
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event, Message
from nonebot.params import CommandArg, ArgStr
from nonebot.plugin import PluginMetadata
from .data import text_to_emoji

__plugin_meta__ = PluginMetadata(
    name="nonebot-plugin-abstract",
    description="适用于 Nonebot2 的语句抽象化插件",
    usage="抽象 [要抽象的语句]",
    type="application",
    homepage="https://github.com/ArrebolCherries/nonebot-plugin-abstract",
)

abstract = on_command("abstract", aliases={"抽象", "抽象化"}, priority=5, block=True)

@abstract.handle()
async def _(state: T_State, arg: Message = CommandArg()):
    if arg.extract_plain_text().strip():
        state["abstract"] = arg.extract_plain_text().strip()

@abstract.got("abstract", prompt="你要抽象什么？")
async def _(bot: Bot, event: Event, target_text: str = ArgStr("abstract")):
    abstract_responses = text_to_emoji(target_text)
    if abstract_responses:
        logger.info("抽象成功！")
        await abstract.send(abstract_responses)
    else:
        logger.error("抽象失败~")
        await abstract.send("抽象异常了~一定是程序出了点问题！")
