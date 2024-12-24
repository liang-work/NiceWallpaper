#=======================================#
#NICEWALLPAPER自动更新器
#=======================================#
import requests as requests
import zipfile
import os

def check(ufURL,ver_info):
    requests.packages.urllib3.disable_warnings()
    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.session()
    s.keep_alive = False
    ver_file = requests.get(ufURL,verify=False)
    if ver_file.json()["versionID"] > ver_info["versionID"] and ver_file.json()["identifier"] != ver_info["identifier"]:
        return True,ver_file.json()["Version"]
    else:
        return False,ver_info["Version"]

def upgrade(downURL):
    requests.packages.urllib3.disable_warnings()
    update_file = requests.get(url=downURL,verify=False)
    if update_file.status_code != requests.codes.ok:
        return False,"REQUESTS_ERROR"+update_file.status_code
    with open("cache/temp_update.zip","wb") as f:
        f.write(update_file.content)
    zipfile.is_zipfile('cache/temp_update.zip')
    zip_file = zipfile.ZipFile('cache/temp_update.zip')
    zip_list = zip_file.namelist() # 得到压缩包里所有文件

    for f in zip_list:
        zip_file.extract(f, "cache/") # 循环解压文件到指定目录
    
    zip_file.close() # 关闭文件，释放内存
    if os.path.exists(os.getcwd()+"\\cache\\temp_update.zip"):
        os.remove(os.getcwd()+"/cache/temp_update.zip")
    os.rename("cache/NiceWallpaper-main","cache/"+os.path.basename(os.getcwd()))
    return True,"OK"