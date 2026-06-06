"""
AI Image Gen - AI图像生成工具
支持图像生成提示、风格转换、图像分析
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIImageGenTools:
    """
    AI图像生成工具
    支持：提示、风格、分析
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def generate_prompt(self, description: str, style: str = "realistic") -> str:
        """生成图像生成提示"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为以下描述生成{style}风格的图像生成提示：

描述：{description}

要求：
1. 详细描述
2. 风格关键词
3. 技术参数
4. 适合Midjourney/Stable Diffusion"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        return response.choices[0].message.content

    def analyze_image(self, image_description: str) -> Dict:
        """分析图像"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请分析以下图像：

{image_description}

请返回JSON格式：
{{
    "objects": ["物体"],
    "colors": ["颜色"],
    "composition": "构图",
    "mood": "氛围",
    "style": "风格",
    "improvements": ["改进建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"analysis": content}

    def suggest_style(self, content: str, mood: str) -> Dict:
        """建议艺术风格"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为以下内容建议艺术风格：

内容：{content}
情绪：{mood}

请返回JSON格式：
{{
    "styles": [
        {{"name": "风格名", "description": "描述", "keywords": ["关键词"]}}
    ],
    "recommended": "推荐风格"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"styles": content}

    def generate_variations(self, base_prompt: str, count: int = 4) -> List[str]:
        """生成变体提示"""
        if not self.client:
            return ["LLM客户端未配置"]

        prompt = f"""请为以下提示生成{count}个变体：

基础提示：{base_prompt}

请返回JSON数组格式：["变体1", "变体2", ...]"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\[.*\]', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return [response.choices[0].message.content]

    def generate_negative_prompt(self, positive_prompt: str) -> str:
        """生成负面提示"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为以下正面提示生成负面提示：

正面提示：{positive_prompt}

只返回负面提示："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )

        return response.choices[0].message.content

    def suggest_parameters(self, style: str, quality: str = "high") -> Dict:
        """建议生成参数"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为{style}风格建议生成参数：

质量：{quality}

请返回JSON格式：
{{
    "steps": "步数",
    "cfg_scale": "CFG Scale",
    "sampler": "采样器",
    "resolution": "分辨率",
    "model": "推荐模型"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"parameters": content}


def create_tools(**kwargs) -> AIImageGenTools:
    """创建图像生成工具"""
    return AIImageGenTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Image Gen Tools")
    print()

    # 测试
    prompt = tools.generate_prompt("一只橘色猫咪坐在窗台上", "写实")
    print(prompt)
