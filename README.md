# Heaven

## 简介

本仓库集成了一些常用功能，包括数据科学处理过程、日常工作效率提升，以及一些有趣的功能。目前正在开发中，如果效果良好将在以后继续完善，打造一个数据科学专用工具箱。数据科学包括多个维度，具体针对哪方面的问题...暂时还没想好。

安装方法：

```bash
cd %PYTHON_HOME%/Lib/
git clone https://github.com/paradiseeee/heaven
```

*PS：本人小白，纯属瞎搞，路过的朋友如果感兴趣欢迎交流指教*


## 模块列表

- <strong><i>mysql_helper.py</i></strong>
    - 功能：将 MySQL 终端的常用功能集成到 Python 环境，解决变量交互问题
    - 状态：完成
    - 使用： `from Heaven import MysqlHelper` ； `MysqlHelper??`

- <strong><i>chinese_encoding.py</i></strong>
    - 功能：快速设置 matplotlib 绘图中文字体，以免每次都要设置 rcParams
    - 状态：完成
    - 使用： `from Heaven.chinese_encoding import *` 

- <strong><i><font color=#0099ff>encryption.py</font></i></strong>
    - 功能：加密与解密文档
    - 状态：进行中……
    - 使用： `python -m Heaven.encryption`

- <strong><i>pdf_processor.py</i></strong>
    - 功能：预览 PDF 文件信息、拆分 PDF、合并 PDF
    - 状态：完成
    - 使用： `python -m Heaven.pdf_processor` ； `from Heaven import PDFProcessor`

- <string><i>log_reader.py</i></strong>
    - 功能：读取大型文本文件，可以写出文件或打印到终端
    - 状态：完成
    - 使用： `python -m Heaven.log_reader` ； `from Heaven import LogReader`