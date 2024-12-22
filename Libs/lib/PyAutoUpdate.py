#=======================================#
#NICEWALLPAPER自动更新器
#=======================================#
import Libs.requests as requests

def check(ufURL,downURL,ver_info):
    ver_file = requests.get(ufURL)
    if ver_file.json()["VersionID"] != ver_file["VersionID"] and ver_file.json()["identifier"] != ver_file["identifier"]:
        pass