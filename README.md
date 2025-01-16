**抢红包自动化脚本** _(still progressing)_
=======================
最快抢红包速度：0.3278543s(网速计算在内)
基于 OCR 和 PyAutoGUI 的 Python 脚本，用于抢红包。此项目由10G4余胜军徒儿开发，不会用请加微信：wangmianhao2019

**common errors**
_ModuleNotFoundError: No module named 'sf'_:check if you have installed modules,check below.
_PyAutoGUI fail-safe triggered from mouse moving to a corner of the screen. _:Add **pyautogui.FAILSAFE = False** to init of bot (after import)

**功能**
--------

* 自动识别微信群内红包
* 自动点击抢红包按钮
<video src="https://private-user-images.githubusercontent.com/120712727/403840387-7ad0f088-2679-4beb-81fa-74adbcf88a44.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzcwMjY3MTYsIm5iZiI6MTczNzAyNjQxNiwicGF0aCI6Ii8xMjA3MTI3MjcvNDAzODQwMzg3LTdhZDBmMDg4LTI2NzktNGJlYi04MWZhLTc0YWRiY2Y4OGE0NC5tcDQ_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDExNlQxMTIwMTZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03MGRkNmEwYjQwZDk4ZWFlY2RkNDIzY2ZkYmNjYTVhNTU2MWI3NTc5MWZkNDA5MDY2ZmEyZTI5ZTk2NWY1YWYyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.2fkfWwRCtP657tmU8KbM3ZuVWrSXKHGJFoXTvoDyMzY" data-canonical-src="https://private-user-images.githubusercontent.com/120712727/403840387-7ad0f088-2679-4beb-81fa-74adbcf88a44.mp4?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzcwMjY3MTYsIm5iZiI6MTczNzAyNjQxNiwicGF0aCI6Ii8xMjA3MTI3MjcvNDAzODQwMzg3LTdhZDBmMDg4LTI2NzktNGJlYi04MWZhLTc0YWRiY2Y4OGE0NC5tcDQ_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwMTE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDExNlQxMTIwMTZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03MGRkNmEwYjQwZDk4ZWFlY2RkNDIzY2ZkYmNjYTVhNTU2MWI3NTc5MWZkNDA5MDY2ZmEyZTI5ZTk2NWY1YWYyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.2fkfWwRCtP657tmU8KbM3ZuVWrSXKHGJFoXTvoDyMzY" controls="controls" muted="muted" class="d-block rounded-bottom-2 border-top width-fit" style="max-height:640px; min-height: 200px">

  </video>

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
3. 请安装bluestacks5或其他安卓模拟器运行微信

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


