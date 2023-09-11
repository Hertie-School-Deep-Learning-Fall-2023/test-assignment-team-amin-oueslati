class LCM_calculator:
  """compute Least Common Multiple between two integers."""

  def calculate_lcm(self, a, b):
    # Calculate the LCM using the formula LCM(a, b) = (a * b) / GCD(a, b)
    gcd = self.calculate_gcd(a, b)
    return (a * b) // gcd

  def calculate_gcd(self, a, b):
    # Calculate the GCD using the Euclidean algorithm
    while b:
        a, b = b, a % b
    return a

lcm_calculator = LCM_calculator()
a = 2
b = 3
lcm = lcm_calculator(a, b)
print(f"The LCM of {a} and {b} is {lcm}")