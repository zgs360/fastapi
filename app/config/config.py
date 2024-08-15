import glob
from pathlib import Path
from dynaconf import Dynaconf

__all__ = ['config','TORTOISE_ORM']

# 获取父目录
ROOT_DIR = Path(__file__).parent

def read_config(file_path:str) ->list:
    return glob.glob(file_path, root_dir=ROOT_DIR)


# 调用方法，读取config目录下所有yaml文件
confs = read_config('default/*.yml')

# 实例化Dynaconf
config = Dynaconf(
    settings_files=confs,
    core_loaders=['YAML'],
    load_dotenv=True,
    root_path=ROOT_DIR,
)

TORTOISE_ORM = {
    "connections": {"default": "postgres://root:123456@localhost/lawdb"},
    "apps": {
        "models": {
            "models": ["aerich.models", "app.routers.lawmodels"],
            "default_connection": "default",
        },
    },
}

# 打印配置
print(config.app)
