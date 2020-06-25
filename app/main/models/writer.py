import threading
import time
import sys
import os
from subprocess import call 
from time import sleep
import signal
from select import select

class Writer:
  """Write output @ given speed

  """
  def __init__(self, speed = 0.025):
    self.speed = speed
    self.interrupted = False

  def write(self, s = " "):
    """ Write Print To Terminal """
    speed = self.speed
    sys.stdin.flush()
    for c in s:
      if self.interrupted is False:
        sys.stdout.write(c),
        rlist, _, _ = select([sys.stdin], [], [], speed)
        if rlist: 
          speed = 0.0
          input()
          sys.stdin.flush()
          self.interrupted = True
        sys.stdout.flush()
      else:
        sys.stdout.write(c)
        sys.stdout.flush()

    print("\n", end = "")

  def reset(self):
    self.interrupted = False

  def clear(self): 
    _ = call('clear' if os.name =='posix' else 'cls')
