# 🍌 Banana

Banana is an SDK to write apps for any screen, inspired by Google's [Flutter](https://flutter.dev)
for [Dart](https://dart.dev).

## Install

Run the following commands:

```
git clone https://github.com/TylerMS887/banana --branch "banana/stable"
cd banana
python3 BananaInstaller.py
```

## Modules

### App Developers

Banana has the `pkg` set of tools, which allow you to add and remove Banana packages.
It replaces the old and deprecated `bananaimp` function.

For example, to import the Material UI, use `banana.pkg.add("material")`.
You can run `banana.devhelp("pkg")` in a Python console with Banana imported for
more information.

### Package Developers

Banana uses a module system separate from that of Python itself. You can create new modules
using the main Banana package:

```python
import banana
print("Hello World!")
```

You must prefix the name of your package with `banana_module_` so that Banana can identify it as a
Banana package. There is currently no API to define packages inside Banana's class.

## Rules of Banana

* Banana is not a programming language.
* Banana is simply a toolkit for writing cross-platform apps in Python.
* You must capitalize the B in "Banana" if you are referring to the SDK.
* Banana is not a toolkit to control and eat bananas.
  You might be thinking of HTBMP, "Hypertext Banana Mouth Protocol" \[not real\], but no,
  Banana isn't an implementation of that.
