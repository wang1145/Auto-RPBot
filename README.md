**抢红包自动化脚本**
=======================

基于 OCR 和 PyAutoGUI 的 Python 脚本，用于抢红包。此项目由10G4余胜军徒儿开发，不会用请加微信：wangmianhao2019

**功能**
--------

* 自动识别微信群内红包
* 自动点击抢红包按钮

**依赖**
--------

* `ddddocr`（百度OCR引擎）
* `pyautogui`
* `pypi`

**安装依赖**
-------------

```bash
pip install pytesseract Pillow pyautogui
```

**配置**
------

1. 安装 `Tesseract-OCR` 引擎并设置环境变量：https://github.com/tesseract-ocr/tesseract/wiki
2. 将微信群的截图保存为 `screenshot.png`
3. 配置 `pytesseract` 的路径和参数（参考下面的配置示例）

**使用**
------

1. 在终端中运行脚本：`python redpacket.py`
2. 脚本会自动识别红包并点击抢红包按钮

**代码**
-----

```python
import pytesseract
from PIL import Image
import pyautogui
import time

# 配置 Tesseract-OCR 的路径和参数
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
config = ('-l chi_sim --psm 11')

# 读取截图
image = Image.open('screenshot.png')
text = pytesseract.image_to_string(image, config=config)

# 识别红包
if '红包' in text:
    # 点击抢红包按钮
    pyautogui.click(100, 200)
else:
    print('未发现红包')

# 等待 5 秒钟
time.sleep(5)
```

**注意**
------

* 此脚本仅适用于微信群内的抢红包，其他场景可能需要调整代码。
* 需要确保 `pyautogui` 和 `Pillow` 已经安装，否则脚本可能会报错。
* 请勿滥用此脚本。

如果你想上传到 GitHub，你可以将 README 文件作为根目录下的文件，脚本放在 src 或 scripts 子目录下。
