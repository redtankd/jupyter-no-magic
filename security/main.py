# 加载应用需要的第三方库
import sys
import flask

# 加载允许应用使用的系统函数
import allow

# 禁止加载的系统包
BANNED_MODULES = {'os'}

class BanFinder:
    @classmethod
    def find_spec(cls, name, path, target=None):
        if name in BANNED_MODULES:
            raise ModuleNotFoundError(f"{name!r} is banned")

sys.meta_path.insert(0, BanFinder)

# 删除已经加载的系统包
del sys.modules['os']

# 加载应用
import web