#=======================================#
#NICEWALLPAPER自动更新器
#=======================================#
import Libs.requests as requests

def check(ufURL,ver_info):
    requests.packages.urllib3.disable_warnings()
    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.session()
    s.keep_alive = False
    ver_file = requests.get(ufURL,verify=False)
    if ver_file.json()["versionID"] > ver_info["versionID"] and ver_file.json()["identifier"] != ver_info["identifier"]:
        return True,ver_file.json()["versionID"]
    else:
        return False,ver_info["versionID"]

def upgrade(downURL):
    return True