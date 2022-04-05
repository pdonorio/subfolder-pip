# subfolder-pip
Testing installation from pip in a subfolder

This works:
```bash
 pip install "git+https://github.com/pdonorio/subfolder-pip.git@0a14e9507072e9713e07e44c9ca20679540f56e2#egg=subfolder&subdirectory=vendor"

# 0a14e9507072e9713e07e44c9ca20679540f56e2 is the commit in main to fix to a specific version
# "subfolder" is the name of the library in setup.py
# "vendor" is the subfolder in which the library is found
```

So then we can:

```bash
❯ ipython
Python 3.10.2 (main, Feb  2 2022, 06:19:27) [Clang 13.0.0 (clang-1300.0.29.3)]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.2.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from subfolder.app import App

In [2]: app = App()

In [3]: app.test()
Hello, world (42)!!
```
