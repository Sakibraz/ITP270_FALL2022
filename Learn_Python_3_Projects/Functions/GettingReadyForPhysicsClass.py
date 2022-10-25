# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1
c = 300000000


# Write your code below: 

# fuction f_to_c to convert f to c
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

# f100_in_celcius variable for test
f100_in_celcius = f_to_c(100)
# print to test conversion of f to c
print(f100_in_celcius)

# function c_to_f to covert c_to_f
def c_to_f(c_temp):
  f_temp = ((c_temp * 9/5) + 32)
  return f_temp

# c0_in_fahrenheit variable for test
c0_in_fahrenheit = c_to_f(0)
# print to test conversion of c to f
print(c0_in_fahrenheit)

# function get_force to calculate force
def get_force(mass, acceleration):
  g_force = (mass * acceleration)
  return g_force

# train_force variable for to test get_force function
train_force = get_force(train_mass, train_acceleration)
print(f"The GE train supplies {train_force} Newtons of force.")

# function get_energy to calculate bomb_energy
def get_energy(mass, c):
  g_energy = (mass * (c**2))
  return g_energy

# bomb_energy variable to test get_energy function
bomb_energy = get_energy(bomb_mass, c)
# print to test bomb_energy
print(f"A 1kg bomb supplies {bomb_energy} Joules.")

# function get_work to calculate train_work
def get_work(mass, acceleration, distance):
  g_work = get_force(mass, acceleration) * distance
  return g_work

# train_work variable to test get_work function
train_work = get_work(train_mass, train_acceleration, train_distance)
# print to test train_work
print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")