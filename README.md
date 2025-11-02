# Text2LangbotMsgChain 插件

将 JSON 格式的 LLM 响应转换为 LangBot 消息链。

## 功能

监听 `NormalMessageResponded` 事件，当 LLM 返回 JSON 格式的响应时，自动将其转换为 LangBot 消息链并发送。

## 使用方法

### 1. 安装插件

将插件目录放置在 LangBot 的插件目录中，然后通过 Web UI 启用插件。

### 2. 配置 LLM 返回 JSON 格式

在 LLM 的 prompt 中添加指令，让其返回 JSON 格式的消息。例如：

```
请以 JSON 数组格式返回消息，每个元素包含 type 和对应的参数。
支持的类型：Plain（文本）、Image（图片）、At（@某人）等。

示例：
[
  {"type": "Plain", "text": "这是一条文本消息"},
  {"type": "Image", "url": "https://example.com/image.jpg"}
]
```

### 3. LLM 响应示例

```json
[
  {
    "type": "Plain",
    "text": "你好！这是一条文本消息"
  },
  {
    "type": "Image",
    "url": "https://example.com/image.jpg"
  },
  {
    "type": "At",
    "target": "123456"
  },
  {
    "type": "Plain",
    "text": " 你好！"
  }
]
```

## 支持的消息组件类型

- `Plain` - 纯文本消息
  - 参数：`text` (字符串)
  
- `Image` - 图片消息
  - 参数：`url` (字符串)
  
- `At` - @指定成员
  - 参数：`target` (用户ID)
  
- `AtAll` - @全体成员
  - 参数：无
  
- `Voice` - 语音消息
  - 参数：`url` (字符串)
  
- `File` - 文件消息
  - 参数：`url` (字符串), `name` (文件名)

更多组件类型请参考 LangBot 文档。

## 工作原理

1. 插件监听 `NormalMessageResponded` 事件
2. 获取 LLM 的响应文本 `response_text`
3. 尝试将响应文本解析为 JSON 数组
4. 遍历数组，根据 `type` 字段创建对应的消息组件
5. 将所有消息组件组合成 `MessageChain`
6. 设置到 `event.reply_message_chain`
7. 调用 `event_context.prevent_default()` 阻止默认行为

## 注意事项

- 如果 LLM 返回的不是 JSON 格式，插件会自动跳过，使用默认的文本回复
- 如果 JSON 格式不正确或包含不支持的消息类型，会在日志中记录警告
- 插件会忽略无效的消息组件，只处理有效的部分


## 效果展示
- Dify 工作流输出效果

![image](https://github.com/user-attachments/assets/31ff0c34-779d-419c-9d50-e8aadf5fccc7)


- Appmsg消息转发效果

![image](https://github.com/user-attachments/assets/4bf37f30-9ff6-429a-a3e2-1f552423c3ac)

## 版本

- 当前版本: 1.0.0
- 作者: shinelinxx
- 仓库: https://github.com/shinelinxx/Text2LangbotMsgChain

## 许可证

MIT License
