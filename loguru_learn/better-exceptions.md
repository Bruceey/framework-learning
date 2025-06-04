# 一、Python 模块查找路径

Python 模块查找路径确实是个重要话题！Python 按照特定顺序在以下路径中查找模块：

## 1. 脚本所在目录

Python 首先在当前脚本所在目录中查找模块。这就是为什么在同一脚本目录下可以直接 `import` 其他 `.py` 文件的原因。

## 2. PYTHONPATH 环境变量

如果设置了 `PYTHONPATH` 环境变量，Python 会在这些路径中查找模块：

bash

```bash
export PYTHONPATH="/path/to/my/modules:/another/path"
```

## 3. 标准库路径

Python 内置标准库的安装路径，通常是：

- Unix/Linux: `/usr/lib/python3.x/`
- Windows: `C:\Python3x\Lib\`

## 4. site-packages 目录

第三方包的默认安装位置：

- 全局安装：`/usr/lib/python3.x/site-packages/`
- 用户安装：`~/.local/lib/python3.x/site-packages/`
- 虚拟环境：`venv/lib/python3.x/site-packages/`

## 5. .pth 文件指定的路径

就像你刚才问的 better-exceptions，`.pth` 文件可以添加额外的搜索路径。这些文件通常位于 site-packages 目录中。

`.pth` 文件有两个主要功能：

1. **添加路径到 sys.path**：通常用来添加模块搜索路径

2. **执行代码**：`.pth` 文件可以被稍微滥用来做其他事情 [Don't treat pth files as data files · Issue #885 · scikit-build/scikit-build](https://github.com/scikit-build/scikit-build/issues/885)，包括执行 Python 代码

## 6. sys.path 动态添加

在运行时可以通过代码修改模块搜索路径：

python

```python
import sys
sys.path.append('/custom/module/path')
sys.path.insert(0, '/priority/path')  # 插入到开头，优先级更高
```

## 7. zip 文件和 egg 文件

Python 还可以从压缩文件中导入模块，这些文件路径也会被添加到 `sys.path` 中。

## 查看当前搜索路径

你可以通过以下方式查看当前的模块搜索路径：

python

```python
import sys
for path in sys.path:
    print(path)
```

## 查找顺序的重要性

Python 按照 `sys.path` 中的顺序依次查找，找到第一个匹配的模块就停止搜索。这就是为什么有时候会出现"模块被意外覆盖"的问题——如果当前目录有个 `json.py` 文件，它会覆盖标准库的 `json` 模块！

**sys.path中路径下如果还有文件夹，会递归进入查找吗？**

**不会递归查找！** 这是一个很重要的点。



# 二. better-exceptions简介
项目地址： [https://github.com/Qix-/better-exceptions](https://github.com/Qix-/better-exceptions)

## 1. 安装使用

```bash
pip install better_exceptions

# 配置完环境变量就行了
export BETTER_EXCEPTIONS=1  # Linux / OSX
setx BETTER_EXCEPTIONS 1    # Windows，setx默认永久设置用户环境变量

# 为什么配置完环境变量就可以直接使用？
答: 利用python模块查找路径的原理，pip安装完better_exceptions后，在site-packages下存在better_exceptions_hook.pth
，此时会执行它。
注意:  不能在py文件中通过os.environ['BETTER_EXCEPTIONS'] = "1"设置环境变量，
      因为执行better_exceptions_hook.pth中的代码会在之前发生
```



## 2. 其他常用用法

If you want to allow the entirety of values to be outputted instead of being truncated to a certain amount of characters:

```python
import better_exceptions
better_exceptions.MAX_LENGTH = None
```

## 3. 其他引用该包的库

1. **loguru**
