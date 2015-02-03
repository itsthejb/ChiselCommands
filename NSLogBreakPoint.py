#!/usr/bin/python
# Example file with custom commands, located at /magical/commands/example.py

import lldb
import fblldbbase as fb

def lldbcommands():
  return [ PrintKeyWindowLevel() ]

class PrintKeyWindowLevel(fb.FBCommand):
  def name(self):
    return 'pkeywinlevel'

  def description(self):
    return 'An incredibly contrived command that prints the window level of the key window.'

  def run(self, arguments, options):
    # It's a good habit to explicitly cast the type of all return
    # values and arguments. LLDB can't always find them on its own.
    lldb.debugger.HandleCommand('p (CGFloat)[(id)[(id)[UIApplication sharedApplication] keyWindow] windowLevel]')
    