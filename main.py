#由余胜军徒儿开发()          开源协议:CC0 public domain
import ddddocr
import time
import pyautogui
from PIL import ImageGrab  # 导入ImageGrab模块，用于截取屏幕图像
import numpy as np  # 导入numpy模块，用于处理图像数据
import os
ocr = ddddocr.DdddOcr(show_ad=False)
i=0
#主程序
input("start?(Y/N)")
print("初始化中，请打开微信群......")
time.sleep(1)
print("将大局逆转吧！")

# 设置截图保存路径
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
screenshot_folder = os.path.join(desktop_path, "Screenshots")
os.makedirs(screenshot_folder, exist_ok=True)

# 定义监控区域的左上角和右下角坐标
monitor_region = (83,910,165,933)

# 初始化上一次截图
last_screenshot = ImageGrab.grab(bbox=monitor_region)
try:
    while True:  # 进入无限循环，持续监控屏幕变化
        # 获取当前屏幕截图
        current_screenshot = ImageGrab.grab(bbox=monitor_region)

        # 将图像转换为 NumPy 数组
        current_screenshot_array = np.array(current_screenshot)  # 将当前截图转换为NumPy数组
        last_screenshot_array = np.array(last_screenshot)  # 将上一次截图转换为NumPy数组

        # 计算监控区域的像素值差异
        pixel_diff = np.sum(current_screenshot_array != last_screenshot_array)  # 计算两张截图像素差异的总和

        # 检查像素值差异是否超过阈值（根据具体情况调整阈值）
        threshold = 1000  # 示例阈值，根据实际情况调整
        if pixel_diff > threshold:  # 如果像素值差异超过阈值，则表示屏幕发生了变化
            time.sleep(0.1)# 生成截图文件名
            screenshot_filename = f"screenshot_{int(time.time())}.png" # 根据当前时间生成截图文件名
            screenshot_path = os.path.join(screenshot_folder, screenshot_filename)  # 拼接截图文件路径
            # 保存截图
            current_screenshot.save(screenshot_path)  # 将当前截图保存为图片文件

            # 更新上一次截图
            last_screenshot = current_screenshot  # 将当前截图赋值给上一次截图      # 每隔一定时间进行一次截图
            time.sleep(0.1)  #0.1查一次屏幕变化，可根据需要调整
            start = time.time()
            image = open(screenshot_path, "rb").read()
            result = ocr.classification(image)
            end = time.time()
            length = end - start
            if result == "微信红包":
                print("发现红包,OCR仅用时",length,"秒！")
                pyautogui.moveTo(262,876)
                pyautogui.click()
                time.sleep(0.4)
                pyautogui.moveTo(273,704)
                pyautogui.click()
                print("抢到红包！")
                time.sleep(3)
                print("即将返回检测")
                pyautogui.moveTo(21,105)
                pyautogui.click()




except KeyboardInterrupt:1
