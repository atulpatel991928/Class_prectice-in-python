class circle():
  pi=3.14
  def __init__(self, radius):
    self.radius = radius
  def __area__(self):
    return self.radius * self.radius * self.pi
  def __perimeter__(self):
    return  2  * self.pi * self.radius * self.radius

new_circle = circle(5)
print(new_circle.__area__())
print(new_circle.__perimeter__())



