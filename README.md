# uwuify

![PyPI - Downloads](https://img.shields.io/pypi/dm/uwuify?style=for-the-badge)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


Command line uwuification

# Installation
```shell
pip install uwuify
```

# Usage
```shell
uwuify hello
# outputs hewwo in console

uwuify how are you? --smiley --yu
# outputs how awe yoyu? with a random smiley

uwuify how are you? --smiley --yu --stutter
# outputs h-how awe yoyu? with a random smiley
# --stutter stutters every 4-th word
```
or
```python
import uwuify

print(uwuify.uwu("hello"))
# hewwo

flags = uwuify.SMILEY | uwuify.YU
print(uwuify.uwu("how are you?", flags=flags))
# how awe yoyu? with a random smiley

flags = uwuify.SMILEY | uwuify.YU | uwuify.STUTTER
print(uwuify.uwu("how are you?", flags=flags))
# h-how awe yoyu? with a random smiley
```