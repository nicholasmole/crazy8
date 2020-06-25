import time
import sys

def delay_print(s = " ", sleep_time = 0.025):
  for c in s:
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(sleep_time)
  print("\n", end ="")
