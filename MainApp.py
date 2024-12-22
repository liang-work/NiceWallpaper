###########################################################################
##程序版本 1.00
##Made in Python3.12 amd
##By liang_work
###########################################################################
class InternalError(Exception):#自定义错误
    def __init__(self,ErrorInfo):
        super().__init__(self) #初始化父类
        self.errorinfo=ErrorInfo
    def __str__(self):
        return self.errorinfo
try:
    import Libs.customtkinter as ctk
    import Libs.CTkMenuBar as CTkMenuBer
    import Libs.toml as toml
    import Libs.lib.PyWallpaper as pwl
    from configparser import ConfigParser
    import os
except ModuleNotFoundError as m:
    print(f"未找到模块:{m}\n程序停止。\nEC:0x00002")
    raise IndentationError("EC:0x00002")

filePath = os.path.dirname(__file__)
lang_load = ConfigParser(filePath+"/Assets/lang/zh_cn.lang")
lang_load.read("")
app = ctk.CTk()
app.title("")
app.geometry(f"{int(app.winfo_screenwidth()//2.5)}x{int(app.winfo_screenheight()//2)}")
app.mainloop()
