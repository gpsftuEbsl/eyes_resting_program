from time import sleep
import tkinter as tk  # 引入 tkinter 以建立 GUI 視窗

# ===== 設定區 =====
<<<<<<< HEAD
WORK_SEC = 10            # 工作時間 (秒)；這裡是 _ 分鐘，測試用
INTERVAL_SEC = 2        # 第二次開始的固定間隔時間 (秒)
=======
WORK_SEC = 30*60            # 工作時間 (秒)；這裡是 30 分鐘，測試用
INTERVAL_SEC = 5*60        # 第二次開始的固定間隔時間 (秒)
>>>>>>> 19c4515 (新增眼睛休息提醒程式，包含 GUI 界面與定時休息功能)
MESSAGE = "TAKE A BREAK~  (=_=)~\n休息一下啦 ( -_•)\n不然你的視力會提前申請退休w"  # 休息提醒訊息

# ===== 定義函式 =====
def show_break():
    """顯示休息提醒視窗，並在關閉後排程下一次提醒"""
    
<<<<<<< HEAD
    # 建立新的彈出視窗
    popup = tk.Toplevel(root)
    popup.title("Rest Note")           # 視窗標題
    popup.attributes("-topmost", True) # 視窗保持在最前方
    popup.geometry("1500x800")         # 視窗大小
=======
    # 以下為建立新的彈出視窗：
    
    # 以 root 為父視窗，建立一個新的彈出視窗，並命名為 popup 方便後續操作
    popup = tk.Toplevel(root) 
    popup.title("Rest Note")           # 視窗標題
    popup.attributes("-topmost", True) # 視窗保持在最前方
    screen_w = popup.winfo_screenwidth()   # 取得螢幕寬度
    screen_h = popup.winfo_screenheight()  # 取得螢幕高度
    popup.geometry(f"{screen_w}x{screen_h}+0+0")  # 用螢幕大小設定滿版視窗
>>>>>>> 19c4515 (新增眼睛休息提醒程式，包含 GUI 界面與定時休息功能)
    
    # 建立訊息標籤，文字居中換行
    label = tk.Label(
        popup,
        text=MESSAGE,
        font=("Arial", 30),    # 字型與大小
        wraplength=380,        # 文字自動換行寬度
        justify="center"       # 文字置中
    )
    label.pack(expand=True)  # 置中顯示
    
    # 定義關閉視窗時的行為
    def close_popup(event=None):
        """關閉彈出視窗並排程下一次提醒"""
        popup.destroy()                       # 關閉視窗
        root.after(INTERVAL_SEC * 1000, show_break)  # 排程下一次提醒

    # 綁定 Enter 鍵或視窗 X 按鈕關閉視窗
    popup.bind("<Return>", close_popup)
    popup.protocol("WM_DELETE_WINDOW", close_popup)
<<<<<<< HEAD
=======
    
>>>>>>> 19c4515 (新增眼睛休息提醒程式，包含 GUI 界面與定時休息功能)
def loading_animation():
    """模擬系統加載動畫"""
    print("系統啟動中...")
    sleep(2)  # 暫停 2 秒以模擬啟動過程
    global WORK_SEC
<<<<<<< HEAD
    WORK_SEC = int(input("這裡是護眼小助手\n請輸入預計工作時間(分):"))*60
=======
    WORK_SEC = int(input("這裡是小晶護眼系統 ∠( ᐛ 」∠)\n請輸入預計工作時間(分):"))*60
>>>>>>> 19c4515 (新增眼睛休息提醒程式，包含 GUI 界面與定時休息功能)
    for i in range(4):
        print(f"系統加載中...\n進度:{i*30}%")
        sleep(2)  # 暫停 2 秒以模擬啟動過程
    print("系統加載中...\n進度:100%")
    sleep(2)
    print("加載完成！\n")
    sleep(1)
<<<<<<< HEAD
    print(f"🕒 系統啟動──開始計時 {WORK_SEC/60} 分鐘 ⏳\n💡 助手提醒：時間到我會跳出來喔 (=v=)~")
=======
    print(f"🕒 系統啟動──開始計時 {WORK_SEC/60} 分鐘 ⏳\n💡 小晶提醒：時間到我會跳出來喔 (=v=)~")
>>>>>>> 19c4515 (新增眼睛休息提醒程式，包含 GUI 界面與定時休息功能)

# ===== 主程式 =====
root = tk.Tk()      # 建立主視窗
root.withdraw()      # 隱藏主視窗（不顯示）

# == 程序啟動訊息 ==

loading_animation()  # 顯示加載動畫
root.after(WORK_SEC * 1000, show_break)  # 排程第一次休息提醒 (root.after:在指定毫秒後執行函式)
root.mainloop()      # 開始事件迴圈
