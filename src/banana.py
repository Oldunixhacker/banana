#!/usr/bin/python3

"""
WHAT IS BANANA?
   Banana is a free and open-source SDK to write your portable Python apps.

   Banana currently supports JavaScript for the web, Android for mobile, and
   Mac, Windows, and GNU/Linux for desktop. i(Pad)OS is not yet supported.
   
   Banana is free to use under the BSD three-clause license.
   
   Most info printed by Banana is labeled with a banana Emoji to distinguish
   them from regular info. If you cannot see the banana, ensure your
   computer can render Emoji in the console.

ETYMOLOGY
   Banana is named after a long curved fruit which grows in `clusters' and
   has soft pulpy flesh and yellow skin when developed to the point of
   readiness for harvesting and eating.
"""

import sys

sys.displayhook = display_hook

class concolors:
   """
   Colors for console output. Used primarily for the Banana compiler
   output, but can be used in any Banana console app.
   """
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class colors:
   """
   Stripped down version of concolors that removes bold and underline,
   which are not colors.
   """
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   END = '\033[0m'

def BananaExceptionHandler(message):
   """
   Prints a message and exit if not an interactive terminal.
   """
   print(f"{colors.RED}{concolors.BOLD}[ERROR]{colors.end}{colors.RED} {message}")
   if not hasattr(sys, 'ps1'):
      exit(1)
class sdkerror(Exception):
    """
    Exception related to SDK errors.
    Currently, the only use of this is in the devhelp function.
    """
    pass

import os
import ctypes
import importlib

if __name__ == "__main__":
  print(f"🍌 This script must be imported in order to run, it has {concolors.BOLD}no use{concolors.END} when run directly.")
  exit(1)

def currenttime():
   """
   The current time. Useful for command-line logs.
   """
   return importlib.import_module('datetime').datetime.now()

def devhelp(package=None):
   """
   Open the Python help page for Banana developers (not users of
   your Banana apps).
   
   This function is intended for the Python REPL and has no use in a
   standard application.
   
   A package name can be specified AS A STRING.
   """
   if package == None:
     help("banana")
   else:
     if package in globals():
       help("banana." + package)
     else:
       raise sdkerror("Banana can only offer help for Banana functions and packages imported into this app")
   
def bananaimp(packagename):
  """
  NOTE: THIS FUNCTION HAS BEEN DEPRECATED. Use pkg.add instead.
  
  Import a module designed specifically for Banana.
  """
  
  print(f"🍌 {concolors.YELLOW}{concolors.BOLD}WARNING:{concolors.END}{concolors.YELLOW} bananaimp is deprecated and will be {concolors.RED}{concolors.BOLD}removed{concolors.END}{concolors.YELLOW} in Banana 1.0. Use pkg.add instead{concolors.END}")
  if packagename == "":
   raise ImportError("Package name must not be empty")
  if packagename in globals():
   raise ImportError(f"Something with the name \"{packagename}\" is already defined, probably the same module")
  if not packagename.isidentifier():
   raise SyntaxError("Package name is not valid. Package names can contain lowercase and uppercase letters, numbers, and underscores.")
  print(f"🍌 Importing package {packagename}")
  try:
   # Python does not allow us to import with the name from an
   # argument, so we do an import using importlib as our frontend.
   globals()[packagename] = importlib.import_module("banana_module_" + packagename)
  except ModuleNotFoundError:
   print(f"🍌 Package \"{packagename}\" does not exist. If the package does exist, rename the package by adding the \"banana_module_\" prefix to the name, so that Banana identifies it")
   print(f"🍌 If you are importing a package that does not rely on Banana, such as os, add this to the start of your code:\n🍌 import {packagename}")
   return 1
  except:
   print("🍌 Importlib returned an error.")
   return 1
  print(f"🍌 Imported Banana package {packagename} with no errors")
  print("🍌 The package is accessible under your Banana import")
class pkg():
   """
   A set of tools for managing the usage of Banana packages.
   """
   class PkgError(Exception):
       """
       An exception for the pkg tools. This should not be used in your
       own packages or apps.
       """
       pass
   class PkgMissingError(Exception):
       """
       Same case as PkgError.
       """
       pass
   def add(packagename=None):
     """
     Import a module designed specifically for Banana.

     The `foundation' module is imported automatically into the app
     and cannot be imported through pkg.add.

     EXAMPLE
        import banana
        banana.pkg.add('material')
        def main():
           banana.run(myApp)
        class myApp():
           return banana.material.MaterialApp(
              useMd3=true
           )
     """

     if packagename == None:
      raise pkg.PkgError("Package name not specified")
     if packagename == "":
      raise pkg.PkgError("Package name must not be empty")
     if packagename in globals():
      raise pkg.PkgError(f"Something with the name \"{packagename}\" is already defined, probably the same module")
     if not packagename.isidentifier():
      raise SyntaxError("Package name is not valid. Package names can contain lowercase and uppercase letters, numbers, and underscores.")
     try:
      # Python does not allow us to import with the name from an
      # argument, so we do an import using importlib as our frontend.
      globals()[packagename] = importlib.import_module("banana_module_" + packagename)
     except ModuleNotFoundError:
      print(f"🍌 Installing {packagename}...")
      if os.system(f"pip install banana-module-{packagename}") != 0:
         raise pkg.PkgMissingError("Failed to install package.")
     except:
      raise pkg.PkgError
     print(f"🍌 [{concolors.BOLD}{currenttime()}{concolors.END}] Loaded {concolors.UNDERLINE}{packagename}{concolors.END}")
