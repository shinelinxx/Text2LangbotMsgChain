# Text2LangbotMsgChain

<!--
## 插件开发者详阅

### 开始

此仓库是 LangBot 插件模板，您可以直接在 GitHub 仓库中点击右上角的 "Use this template" 以创建你的插件。  
接下来按照以下步骤修改模板代码：

#### 修改模板代码

- 修改此文档顶部插件名称信息
- 将此文档下方的`<插件发布仓库地址>`改为你的插件在 GitHub 上的地址
- 补充下方的`使用`章节内
- 修改`main.py`中的`MyPlugin`类名为你的插件类名
- 修改`manifest.yaml`中的信息
- 将插件所需依赖库写到`requirements.txt`中
- 根据[插件开发教程](https://docs.langbot.app/zh/plugin/dev/tutor.html)编写插件代码
- 删除 README.md 中的注释内容


#### 发布插件

推荐将插件上传到 GitHub 代码仓库，以便用户通过下方方式安装。   
欢迎[提issue](https://github.com/RockChinQ/LangBot/issues/new?assignees=&labels=%E7%8B%AC%E7%AB%8B%E6%8F%92%E4%BB%B6&projects=&template=submit-plugin.yml&title=%5BPlugin%5D%3A+%E8%AF%B7%E6%B1%82%E7%99%BB%E8%AE%B0%E6%96%B0%E6%8F%92%E4%BB%B6)，将您的插件提交到[插件列表](https://github.com/stars/RockChinQ/lists/qchatgpt-%E6%8F%92%E4%BB%B6)


下方是给用户看的内容，按需修改
-->

## 安装

1. 完成 [LangBot](https://github.com/RockChinQ/LangBot) 主程序配置
2. 到插件管理页面安装本插件  
   → 或查看详细[插件安装说明](https://docs.langbot.app/zh/plugin/plugin-intro#%E5%AE%89%E8%A3%85)

---

## 使用说明
<!-- 插件开发者自行填写具体使用说明 -->

---

## `response_text` 格式规范

```json
[
  {"type": "Image", "url": "必填：图片URL"},
  {"type": "Plain", "text": "必填：纯文本内容"},
  {"type": "WeChatAppMsg", "app_msg": "必填：微信App消息"}
]
```
 ​其他消息类型，字段要求​（对齐 [message.py](https://github.com/RockChinQ/LangBot/blob/955b391253aaab686356efecac34c222299aa829/pkg/platform/types/message.py) 定义）

## 脚本优点
- 当返回字段为json时，插件才会做转换处理。
- 无需重复定义消息结构，使用langbot原生定义的message结构

## 效果展示
- Dify 工作流输出效果

![image](https://github.com/user-attachments/assets/31ff0c34-779d-419c-9d50-e8aadf5fccc7)


- Appmsg消息转发效果

![image](https://github.com/user-attachments/assets/4bf37f30-9ff6-429a-a3e2-1f552423c3ac)



