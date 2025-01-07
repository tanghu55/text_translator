# ComfyUI Text Translator Node

这是一个用于ComfyUI的文本翻译节点插件，可以在生成图片之前对提示词进行翻译。

## 功能特点

- 支持中英文互译
- 与CLIP文本编码器无缝集成
- 保持原有的编码功能
- 本地模型存储，避免重复下载

## 安装方法

1. 将整个`text_translator`文件夹复制到ComfyUI的`custom_nodes`目录下
2. 安装依赖：
   ```bash
   pip install -r custom_nodes/text_translator/requirements.txt
   ```
3. 重启ComfyUI

## 使用方法

1. 在节点菜单中找到"Text Translator"节点
2. 连接输入：
   - text: 输入要翻译的文本
   - translate_to: 选择目标语言（中文/英文）
   - clip: 连接CLIP模型
3. 输出将直接连接到需要CLIP编码的其他节点

## 模型存储

- 翻译模型会自动下载并保存在插件目录下的`models`文件夹中
- 支持的模型：
  - 中译英：opus-mt-zh-en
  - 英译中：opus-mt-en-zh
- 模型下载后会保存在本地，避免重复下载

## 注意事项

- 首次使用时会自动下载并保存翻译模型到本地
- 建议使用GPU来加速翻译过程
- 如果遇到CUDA内存不足，可以尝试减少批处理文本的长度
- 模型文件保存在`custom_nodes/text_translator/models`目录下
 