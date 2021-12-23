from typing import ClassVar
from numutils import n2w
import time
from datetime import datetime

class WordClock:
  def __init__(self) -> None:
    self.time = datetime.now()

  def run(self):
    self.time = datetime.now()
    hours = self.time.hour
    mins = self.time.minute
    secs = self.time.second

    m = n2w(mins)
    s = n2w(secs)

    ampm = "pm" if hours > 12 else "am"
    hours = hours - 12 if hours > 12 else hours
    h = n2w(hours)

    t = f"It's {h.words()} {m.words()} {ampm} and {s.words()} seconds {datetime.now()}"

    g_mins = self.__grammar(mins)
    hours = self.time.hour
    if hours < 12:
      ampm = 'in the morning'
    elif(hours>12 and hours < 18):
      ampm = 'in the afternoon'
    else:
      ampm = 'in the evening'
    hours = hours - 12 if hours > 12 else hours
    h = n2w(hours)
    alt_t = f"It's {g_mins} {h.words()} (and {s.words()} seconds) {ampm}"
    print(alt_t)

  def __grammar(self, minutes):
    amount = ""
    direction = ""

    n = n2w(minutes)

    if minutes  == 15:
      amount = "quarter"
      direction = "past"
    elif minutes == 30:
      amount = "half"
      direction = "to"
    elif minutes == 45:
      amount = "quarter"
      direction = "to"
    elif (minutes % 5) == 0:
      amount = n.words()
      if minutes > 30:
        direction = "to"
      else:
        direction = "past"
    else:
      amount = n.words()
      if minutes > 30:
        direction = "minutes to"
      else:
        if minutes == 1:
          direction = 'minute past'
        else:
          direction = "minutes past"
    
    return f"{amount} {direction}"

c = WordClock()

while True:
  c.run()
  time.sleep(1)