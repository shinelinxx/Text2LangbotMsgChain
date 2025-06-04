from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类
from pkg.platform.types import message as platform_message
import json

# 注册插件
@register(name="Text2LangBotMsgChain", description="transfer text (eg. from dify) to message chain", version="0.1", author="shinelinxx")
class Text2LangBotMsgChain(BasePlugin):

    # 插件加载时触发
    def __init__(self, host: APIHost):
        pass

    # 异步初始化
    async def initialize(self):
        pass

    @handler(NormalMessageResponded)
    async def on_normal_message_responded(self, ctx: EventContext):
        """处理dify消息回复"""
        # # 群id
        # group_id = None \
        #     if ctx.event.launcher_id == ctx.event.sender_id \
        #         else ctx.event.launcher_id
        # # 发送方id
        # sender_id = ctx.event.sender_id

        # 消息体
        response_text = ctx.event.response_text
        try:
            message_elements = []
            message_list = json.loads(response_text)
            for item in message_list:
                msg_type = item.get("type", "")
                if msg_type == "WeChatAppMsg":
                    message_elements.append(
                        platform_message.WeChatAppMsg(app_msg = item.get("app_msg", "")))
                if msg_type == "Image":
                    message_elements.append(
                        platform_message.Image(url = item.get("url", "")))
                if msg_type == "Plain":
                    message_elements.append(
                        platform_message.Plain(text = item.get("text", "")))
            if len(message_elements) > 0:    
                await ctx.reply(platform_message.MessageChain(message_elements))
                ctx.prevent_default()  # 阻断默认行为
        except Exception as e:
            self.ap.logger.error(f"回复消息处理异常: {str(e)}")
    

    # 插件卸载时触发
    def __del__(self):
        pass
