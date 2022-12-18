// SCALA Dev Playground

// Functional 
def hello_world: Unit =
  // Call in message defined outside
  print(msg, "\n")

def msg = "Hello World... this code has been compiled in Scala 3"

// math
def one_line_add(a: Int, b: Int): Int = a + b
def one_line_sub(a: Int, b: Int): Int = a - b
def one_line_mult(a: Int, b: Int): Int = a * b
def one_line_div(a: Int, b: Int): Int = a / b
def one_line_pow(a: Int, b: Int): Int = a ^ b
def one_line_mod(a: Int, b: Int): Int = a % b


// Data structures - always use val unless mutation is req - then use var
def data_structures =
  val x_list = List(1,2,3,4,5,6,7,8)
  val x_dict = Map("first" -> 1, "second" -> 2, "third" -> 3)
  val x_set = Set(1,2,3,4)
  val x_tup = (1,2,3,4)


// OOP structures
class Intro(var name: String = ""):
  def speak() = println(s"Hi, my name is $name \n $msg")


@main
def  run_main: Unit =
  //hello
  hello_world

  // OOP test 
  val p = Intro()
  p.name = "Danny"
  p.speak()

  // math
  print(s"Math Results...",
    one_line_add(2, 4),
    one_line_div(2, 4),
    one_line_mod(2, 4),
    one_line_mult(2, 4),
    one_line_pow(2, 4),
    one_line_sub(2, 4),
    "\n",
  )
  // DS
  print(
    s"Data Structures...",
    data_structures,
    "\n"
  )

  // Control flow
  var x = 0.99999999999999994 // rounding limit 
  if x >= 1 then print(s"x = $x \n") else print(s"x must be greater than or equal to one... try again \n")

  x = 0.49999999999999999 // when re-assigning - don't use var again or it will error
  if x > 1 then 
    print(">1 \n")
  else if x >= 0.5 && x < 1 then
    print("Top 50% \n")
  else
    print("Try Again... \n")

  var a = 2
  var b = 4

  // Same as each other
  val min_val = if a < b then a else b
  def mini(a: Int, b: Int): Int = 
    if a < b then a else b

  print(min_val == mini(a, b))
  print("\n")