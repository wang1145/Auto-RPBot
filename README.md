**抢红包自动化脚本**
=======================
最快抢红包速度：0.3278543s(网速计算在内)
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
pip install pyautogui
pip install ddddocr

```

**配置**
------

1. 将微信群的截图保存为 `last_screenshot`(Have done automatically)
2. 配置 `os/screenshot` 的路径和参数（参考下面的配置示例）

**使用**
------

1. 在终端中运行脚本：`main.py`
2. 脚本会自动识别红包并点击抢红包按钮

**代码**
-----

请见main.py
```

**注意**
------

* 此脚本仅适用于微信群内的抢红包，其他场景可能需要调整代码。
* 需要确保 `pyautogui` 和 `ddddocr` 已经安装，否则脚本可能会报错。
* 请勿滥用此脚本。


