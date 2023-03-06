# Securing Jupyter Notebook

## 安装虚拟环境Virtualenv，并激活

## 安装Jupyter Notebook

pip install notebook

## 卸载第三方包terminado
pip uninstall terminado

## 修改第三方包IPython

### 屏蔽magic

在**IPython.core.interactiveshell.py**中，找到函数**def init_magics(self)** ，在该函数中找到**self.register_magics(...)**，注释以下：
* m.ExtensionMagics 
    Jupyter扩展管理命令
* m.PackagingMagics  
    Python包管理命令
* m.OSMagics
    执行操作系统命令
* m.ScriptMagics
    执行操作系统脚本

### 屏蔽shell magic

在**IPython.core.inputtransformer2.py**中，找**tr = [...]**，将**ESC_SHELL**和**ESC_SH_CAP**替换为空字符串

在**IPython.core.inputtransformer2.py**中，找到class TransformerManager的函数**def __init__(self)** ，在该函数中找到**self.token_transformers = [...]**，注释以下：
* SystemAssign
    禁止`a = !ls`之类操作系统操作

## 安全控制脚本，存放`security`目录中

## Jupyter Notebook的运行目录是`jupyter-home`

## 启动Jupyter Notebook

export PYTHONSTARTUP=../security/ban_importer.py
jupyter notebook --autoreload --notebook-dir=jupyter-home

## `安全验证.ipynb`用于验证以上控制是否有效
