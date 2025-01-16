# MIT License
#
# Copyright (c) 2025 wang1145
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import ddddocr
import time
import pyautogui
from PIL import ImageGrab  # 导入ImageGrab模块，用于截取屏幕图像
import numpy as np  # 导入numpy模块，用于处理图像数据
import os
import pathlib as pl
pyautogui.FAILSAFE = False



class wx_red_pocket_bot:
    POCKET_KEYWORD = "微信红包"
    MIN_DIFFERENCE = 1000


    def __init__(self, monitor_region: tuple):
        self.ocr = ddddocr.DdddOcr(show_ad=False)

        # 设置截图保存路径
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        self.screenshot_folder = os.path.join(desktop_path, "Screenshots")
        os.makedirs(self.screenshot_folder, exist_ok=True)

        self.monitor_region = monitor_region


    def detect_screen_difference(self) -> tuple[bool, object]:
        # 获取当前屏幕截图
        current_screenshot = ImageGrab.grab(bbox=monitor_region)

        # 将图像转换为 NumPy 数组
        current_screenshot_array = np.array(current_screenshot)  # 将当前截图转换为NumPy数组
        last_screenshot_array = np.array(self.last_screenshot)  # 将上一次截图转换为NumPy数组

        # 计算监控区域的像素值差异
        pixel_diff = np.sum(current_screenshot_array != last_screenshot_array)  # 计算两张截图像素差异的总和

        is_different = (pixel_diff > self.MIN_DIFFERENCE)

        self.last_screenshot = current_screenshot

        return (is_different, current_screenshot)


    def save_screenshot(self, screenshot) -> str:
            screenshot_filename = f"screenshot_{int(time.time())}.png" # 根据当前时间生成截图文件名
            screenshot_path = os.path.join(self.screenshot_folder, screenshot_filename)  # 拼接截图文件路径
            screenshot.save(screenshot_path)  # 将当前截图保存为图片文件

            return screenshot_path


    def open_pocket(self):
        pyautogui.moveTo(262,876)
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.moveTo(273,704)
        pyautogui.click()
        print("抢到红包！")
        time.sleep(3)
        print("即将返回检测")
        pyautogui.moveTo(21,105)
        pyautogui.click()
        pyautogui.moveTo(281,947)
        pyautogui.click()
        time.sleep(1)


    def main_loop(self):
        try:
            print("初始化中，请打开微信群......")
            time.sleep(1)
            print("此项目由 GitHub：wang1145/lllrmm 制作，开源协议为 MIT License，仓库地址：https://github.com/wang1145/Auto-RPBot，如有问题欢迎issue或request")
            print(" ")
            print("Copyright (c) 2025 wang1145")
            print("scanning, please wait...")

            self.last_screenshot = ImageGrab.grab(bbox=monitor_region) # 初始化上一次截图

            while True:  # Main Loop
                # 检查像素值差异是否超过阈值（根据具体情况调整阈值）,如果像素值差异超过阈值，则表示屏幕发生了变化
                is_different, current_screenshot = self.detect_screen_difference()

                if is_different:
                    # time.sleep(0.1)

                    screenshot_path = self.save_screenshot(current_screenshot)

                    # time.sleep(0.1)  #0.1查一次屏幕变化，可根据需要调整

                    start_time = time.time()

                    # 确保读取完后文件停止占用
                    with open(screenshot_path, "rb") as img:
                        image = img.read()

                    ocr_result = self.ocr.classification(image) # OCR

                    end_time = time.time()
                    duration = end_time - start_time

                    if ocr_result == self.POCKET_KEYWORD:
                        print(f"发现红包,OCR仅用时{duration}秒！")
                        self.open_pocket()

        except KeyboardInterrupt:
            print("用户终止！")



# 定义程序入口
if __name__ == "__main__":
    # 定义监控区域的左上角和右下角坐标
    monitor_region = (83,910,165,933)

    bot = wx_red_pocket_bot(monitor_region)
    bot.main_loop()

#21:55:54.370: [Auto-RPBot] git -c credential.helper= -c core.quotepath=false -c log.showSignature=false add --ignore-errors -A -f -- main.py
#21:55:54.439: [Auto-RPBot] git -c credential.helper= -c core.quotepath=false -c log.showSignature=false commit -F C:\Users\Sam\AppData\Local\Temp\git-commit-msg-.txt "--author=wangsz192 <wangmianhao2020@163.com>" --