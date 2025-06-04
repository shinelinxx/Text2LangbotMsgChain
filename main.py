from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类
from pkg.platform.types import message as platform_message
import json
import inspect

# 注册插件
@register(name="Text2LangBotMsgChain", description="transfer text (eg. from dify) to message chain", version="0.1", author="shinelinxx")
class Text2LangBotMsgChain(BasePlugin):

    # 插件加载时触发
    def __init__(self, host: APIHost):
        pass

    # 异步初始化
    async def initialize(self):
        pass


    def create_message_component(self, item):
        msg_type = item.get("type", "")
        if not msg_type:
            return None
        try:
            msg_class = getattr(platform_message, msg_type, None)
            if not msg_class:
                return None
            
            kwargs = {}
            for key, value in item.items():
                if key == "type":
                    continue
                kwargs[key] = value
            return msg_class(**kwargs)
        except Exception as e:
            self.ap.logger.error(f"创建消息对象失败: {str(e)}")
            return None

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
                component = self.create_message_component(item)
                if component:
                    message_elements.append(component)
            
            if message_elements:
                await ctx.reply(platform_message.MessageChain(message_elements))
                ctx.prevent_default()
        except Exception as e:
            self.ap.logger.error(f"回复消息处理异常: {str(e)}")
    

    # 插件卸载时触发
    def __del__(self):
        pass
