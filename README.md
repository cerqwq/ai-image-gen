# 🖼️ AI Image Gen

AI图像生成工具，支持图像生成提示、风格转换、图像分析。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🎨 图像提示生成
- 🖼️ 图像分析
- 🎭 风格建议
- 🔄 变体生成
- ❌ 负面提示
- ⚙️ 参数建议

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_image_gen import create_tools

tools = create_tools()

# 提示生成
prompt = tools.generate_prompt("一只橘色猫咪", "写实")

# 图像分析
analysis = tools.analyze_image("蓝色调的抽象画")

# 风格建议
styles = tools.suggest_style("风景", "宁静")

# 变体生成
variations = tools.generate_variations(prompt, 4)

# 负面提示
negative = tools.generate_negative_prompt(prompt)

# 参数建议
params = tools.suggest_parameters("写实", "high")
```

## 📁 项目结构

```
ai-image-gen/
├── tools.py       # 图像生成工具核心
└── README.md
```

## 📄 许可证

MIT License
