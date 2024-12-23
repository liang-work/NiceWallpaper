###########################################################################
##程序版本 1.00
##Made in Python3.12 and
##By liang_work
###########################################################################

class InternalError(Exception):  # 自定义错误
    def __init__(self, ErrorInfo):
        super().__init__(self)
        self.errorinfo = ErrorInfo

    def __str__(self):
        return self.errorinfo

try:
    import Libs.customtkinter as ctk
    from tkinter import messagebox
    import Libs.CTkMenuBar as CMB
    import Libs.toml as toml
    import Libs.lib.PyWallpaper as pwl
    from configparser import ConfigParser
    import os
    import json
    from Libs.lib.PyAutoUpdate import *
    import sys
    import AboutWindow as AW
except ModuleNotFoundError as m:
    print(f"模块错误: {m}\n程序停止。\nEC:0x00002")
    raise IndentationError("EC:0x00002")

filePath = os.path.dirname(__file__)
lang_load = ConfigParser()

def restart_program():
  python = sys.executable
  os.execl(python, python, * sys.argv)

def load_file():
    global lang_load, config, appinfo
    with open("config/USER.cfg", "r", encoding='utf-8') as f:
        config = toml.load(f)
    with open("Assets/data/appinfo.json", 'r', encoding='utf-8') as f:
        appinfo = json.load(f)

    lang_file_path = os.path.join(filePath, f"Assets/lang/{config['MainWindow']['lang']}.lang")
    if os.path.exists(lang_file_path):
        lang_load.read(lang_file_path, encoding="utf-8")
    else:
        raise FileNotFoundError("NOT_FOUND_LANGUAGE_FILE")

def Update():
    update_check, back_version = check(ufURL=config["MainWindow"]["UpdateJson"], ver_info=appinfo)
    if update_check:
        if messagebox.askyesno(
            lang_load["update"]["FoundUpdate"],
            f"{lang_load['update']['AskDownload_1']}{back_version}{lang_load['update']['AskDownload_2']}"
        ):
            if upgrade(config["MainWindow"]["Upgrade"]):
                if messagebox.askyesno(lang_load["MainWindow"]["title"],lang_load["update"]["UpdateOk"]):
                    restart_program()
                else:
                    pass
            else:
                messagebox.showwarning("ERROR",lang_load["update"]["UpdateBad"])
    else:
        messagebox.showinfo("NOTUPDATE", lang_load["update"]["NotUpdate"])

try:
    load_file()

    app = ctk.CTk()
    menu = CMB.CTkMenuBar(app)
    # 添加菜单项
    file_menu = menu.add_cascade(lang_load["MainWindow"]["file"])
    edit_menu = menu.add_cascade(lang_load["MainWindow"]["edit"])
    settings_menu = menu.add_cascade(lang_load["MainWindow"]["settings"])
    help_menu = menu.add_cascade(lang_load["MainWindow"]["help"])

    help_menu_drop = CMB.CustomDropdownMenu(widget=help_menu)
    help_menu_drop.add_option(option=lang_load["MainWindow"]["update"],command=Update)
    help_menu_drop.add_option(option=lang_load["MainWindow"]["about"],command=lambda:AW.open(ctk,lang_load))

    app.title(lang_load["MainWindow"]["title"])
    app.iconbitmap("Assets/images/wallpaper_logo.ico")
    app.geometry(f"{int(app.winfo_screenwidth() // 2.5)}x{int(app.winfo_screenheight() // 2)}")
    
    app.mainloop()

except (FileNotFoundError, json.decoder.JSONDecodeError, toml.decoder.TomlDecodeError, KeyError, ValueError) as e:
    print(f"资源类错误: {e}\n程序停止。\nEC:0x00003")
    raise IndentationError("EC:0x00003")
