from __future__ import annotations

import json

from langbot_plugin.api.definition.components.common.event_listener import EventListener
from langbot_plugin.api.entities import events, context
from langbot_plugin.api.entities.builtin.platform import message as platform_message


class DefaultEventListener(EventListener):

    async def initialize(self):
        await super().initialize()

        @self.handler(events.NormalMessageResponded)
        async def on_normal_message_responded(event_context: context.EventContext):
            """
            监听 NormalMessageResponded 事件
            将 JSON 格式的 LLM 响应转换为 LangBot 消息链
            """
            event = event_context.event
            response_text = event.response_text
            
            if not response_text:
                return
            
            try:
                message_items = json.loads(response_text)
                message_components = []

                for message_item in message_items:
                    if not isinstance(message_item, dict):
                        continue

                    message_type = message_item.get("type")
                    if not message_type:
                        continue

                    component_class = getattr(platform_message, message_type, None)
                    if not component_class:
                        continue

                    component_kwargs = {key: value for key, value in message_item.items() if key != "type"}
                    
                    try:
                        message_component = component_class(**component_kwargs)
                        message_components.append(message_component)
                    except Exception:
                        # 创建组件失败，跳过
                        continue

                if message_components:
                    await event_context.reply(platform_message.MessageChain(message_components))
                    event_context.prevent_default()
            except Exception:
                # JSON 解析失败或处理异常，使用默认行为
                pass
