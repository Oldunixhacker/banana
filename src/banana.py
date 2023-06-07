#!/usr/bin/python3

"""
WHAT IS BANANA?
   Banana is a free and open-source SDK to write your portable Python apps.

   Banana currently supports JavaScript (web apps), Android, Mac, Windows,
   and Linux.

ETYMOLOGY
   Banana is named after a long curved fruit which grows in `clusters' and
   has soft pulpy flesh and yellow skin when developed to the point of
   readiness for harvesting and eating.
"""

import os
import ctypes
import sys
import importlib

if __name__ == "__main__":
  print("Hello World!")
  exit(0)

def bananaimp(packagename):
  """
  Import a module designed specifically for Banana.
  
  The `foundation' module is imported automatically into the app
  and cannot be imported through bananaimp.
  
  ETYMOLOGY
     Originates from an abberivation:
     `BANANA has its own way of IMPorting modules.'
  
  EXAMPLE
     import banana
     banana.bananaimp('material')
     def main():
        banana.run(myApp)
     class myApp():
        return banana.material.MaterialApp(
           useMd3=true
        )
  """
  
  # Python does not allow us to import with the name from an
  # argument, so we do an import using importlib as our frontend.
  try:
   globals()[packagename] = importlib.import_module("banana_module_" + packagename)
  except:
   raise ImportError("When banana called importlib, importlib returned an error.\n\nIf the package exists, rename the package by adding the \"banana_module_\" prefix to the name, so that Banana identifies it.")
  print(f"🍌 Import package {packagename}")
