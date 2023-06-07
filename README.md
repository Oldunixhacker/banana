# Banana

> *Even though today's apps are written in Dart, tommorow's will be written in Python.* Banana devs

Banana is an SDK to write apps for any screen, inspired by Google's [Flutter](https://flutter.dev)
for Dart.

## Install

Run the following commands:

```
git clone https://github.com/TylerMS887/banana --branch "banana/stable"
cd banana
python3 BananaInstaller.py
```

## Modules

Banana uses a module system separate from that of Python itself. You can
create new modules using the `moduledev` Banana package:

```python
import banana
banana.bananaimp("moduledev")
banana.moduledev.define("hello_world")
```
