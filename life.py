#!/usr/bin/env python2
#
# A simple script to graphically represent (roughly) how much time
#   you have left on earth in terms of weeks, assuming:
#   1. you live to be exactly 90 years old
#   2. each year is exactly 52 weeks (it isn't; it's closer to 52.15)
# The weeks you've already used up are shaded red, the weeks you have left
#   are shaded white, and the years you'll almost certainly be infirm
#   (70th birthday onward) are shaded light blue.
#

from datetime import date, timedelta
import Image

class Square:
  def __init__(self, size=15, borderWidth=3
                ,borderColor=(0,0,0), fillColor=(255,255,255)):
    self.size = size
    self.borderWidth = borderWidth
    self.borderColor = borderColor
    self.fillColor = fillColor

  def draw(self, pixels, leftCol, topRow):
    borderWidth = self.borderWidth
    size = self.size
    for row in xrange(size):
      for col in xrange(size):
        if  row < borderWidth or (size - row) < borderWidth or \
            col < borderWidth or (size - col) < borderWidth:
          color = self.borderColor
        else:
          color = self.fillColor
        pixels[leftCol + col, topRow + row] = color

class Life:
  def __init__(self, birthday):
    self.birthday = birthday

  def time_remaining(self
                      ,today=date.today()
                      ,age_of_infirmity=70
                      ,years_per_lifetime=90):
    # variables
    week_delta = timedelta(weeks=1)
    weeks_per_year = 52
    birthday = self.birthday
    square = Square()
    width = weeks_per_year * square.size
    height = years_per_lifetime * square.size
    img = Image.new('RGB', (width, height), "white")
    pixels = img.load()
    square.fillColor = (255,0,0)
    infirm = birthday + timedelta(weeks=age_of_infirmity * weeks_per_year)
    cur_day = birthday
    # logic
    for year in xrange(years_per_lifetime):
      for week in xrange(weeks_per_year):
        square.draw(pixels, week * square.size, year * square.size)
        cur_day += week_delta
        if cur_day > today:
          square.fillColor = (255,255,255)
        if cur_day > infirm:
          square.fillColor = (170, 200, 255)
    return img

if __name__ == '__main__':
  life = Life(date(1990, 1, 1))
  life.time_remaining().show()




