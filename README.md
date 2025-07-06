# coder
代码分析


## FAQ
1. ImportError: cannot import name 'Markup' from 'jinja2' (/home/lwj/.local/lib/python3.10/site-packages/jinja2/__init__.py)
解决方案：pip install jinja2==3.0.3 --force-reinstall  # 推荐稳定版本
2. example/test下如何编译文件并获取覆盖率报告
解决方案：
``` shell
cd build
cmake ..
cmake --build . --target coverage
```