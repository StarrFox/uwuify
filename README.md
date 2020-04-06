# uwuify

Command line uwuification

# Installation
```shell
# Stable
pip install -U uwuify

# Dev
pip install -U git+https://starrfox/uwuify@master
```

# Usage
```shell
echo hello | uwuify - -
# outputs hewwo in console

uwuify input.txt output.txt
# contents of input.txt uwuifed into output.txt
```
or
```python
from uwuify import uwu_text

print(uwu_text('hello'))
# hewwo
```