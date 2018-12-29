train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

# convert a temperature in Fahrenheit to Celsius
def f_to_c(f_temp):
  c_temp = f_temp - 32 * 5/9
  return c_temp

# test f_to_c
print("This should be about 82:", f_to_c(100))

# convert a temperature in Celsius to Fahrenheit
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

# test f_to_c
print("This should be 32.0: ", c_to_f(0))

# calculate force from mass and acceleration
def get_force(mass, acceleration):
  return mass * acceleration

# test get_force
print("This should be 226800: ", get_force(train_mass, train_acceleration))

def get_energy(mass, c = 3*10**8):
  return mass * c

# test get_energy
print("This should be 300000000: ", get_energy(bomb_mass))

# calculate work from mass, acceleration, and distance
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance

#test get_work
print("This should be 22680000: ", get_work(train_mass, train_acceleration, train_distance))
