🍌 Banana
=========

Banana is an SDK to write apps for any screen, inspired by Google’s
`Flutter <https://flutter.dev>`__ for `Dart <https://dart.dev>`__.

**Do not confuse Banana with the fruit (which Banana was named
after), or other software, such as a library written by
Wikimedia users to localise Toolforge tools.**

Install
-------

Run the following commands:

.. code:: bash

   git clone https://github.com/TylerMS887/banana --branch "banana/stable"
   cd banana
   python3 BananaInstaller.py

Modules
-------

App Developers
~~~~~~~~~~~~~~

Banana has the ``pkg`` set of tools, which allow you to add and remove
Banana packages. It replaces the old and deprecated ``bananaimp``
function.

For example, to import the Material UI, use
``banana.pkg.add("material")``. You can run ``banana.devhelp("pkg")`` in
a Python console with Banana imported for more information.

Banana modules are not imported into ``__main__``.
They are imported in Banana. To use a module for
Banana, e.g. use ```banana.foo.bar()``, not
``foo.bar()``.

Package Developers
~~~~~~~~~~~~~~~~~~

Banana uses a module system separate from that of Python itself. You can
create new modules using the main Banana package:

.. code:: python

   import banana
   print("Hello World!")

You must prefix the name of your package with ``banana_module_`` so that
Banana can identify it as a Banana package. There is currently no API to
define packages inside Banana’s class.

Rules of Banana
---------------

-  Banana is not a programming language.
-  Banana is simply a toolkit for writing cross-platform apps in Python.
-  You must capitalize the B in “Banana” if you are referring to the
   SDK.