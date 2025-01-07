import torch
import os
from googletrans import Translator

class TextTranslatorNode:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.translator = Translator()
        self.lang_map = {
            "翻译成英文": "en",
            "翻译成中文": "zh-cn"
        }
        
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"multiline": True}),
                "translate_to": (["翻译成英文", "翻译成中文"], {"default": "翻译成英文"}),
                "clip": ("CLIP", )
            }
        }
    
    RETURN_TYPES = ("CONDITIONING",)
    RETURN_NAMES = ("conditioning",)
    FUNCTION = "translate_and_encode"
    CATEGORY = "conditioning"

    def translate_text(self, text, target_lang):
        """使用Google Translate进行翻译"""
        try:
            dest_lang = self.lang_map[target_lang]
            # 自动检测源语言
            translated = self.translator.translate(text, dest=dest_lang)
            print(f"原文: {text}")
            print(f"源语言: {translated.src}")
            print(f"目标语言: {dest_lang}")
            print(f"翻译结果: {translated.text}")
            return translated.text
        except Exception as e:
            print(f"翻译出错: {str(e)}")
            return text  # 如果翻译失败，返回原文

    def translate_and_encode(self, text, translate_to, clip):
        try:
            # 执行翻译
            translated_text = self.translate_text(text, translate_to)
            
            # 使用CLIP编码翻译后的文本
            tokens = clip.tokenize(translated_text)
            cond, pooled = clip.encode_from_tokens(tokens, return_pooled=True)
            
            return ([[cond, {"pooled_output": pooled}]], )
        except Exception as e:
            print(f"处理过程中出错: {str(e)}")
            # 如果出错，使用原文进行编码
            tokens = clip.tokenize(text)
            cond, pooled = clip.encode_from_tokens(tokens, return_pooled=True)
            return ([[cond, {"pooled_output": pooled}]], ) 