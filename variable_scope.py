def example_function():
    local_var = "I'm a local var."
    print(f"Inside example_function: {local_var}")


example_function()

global_var = "I'm a global var."
def example_function_2():
    global_var = "I'm modified global var" # Global shadowing
    print(f"Inside example_function: {global_var}")

example_function_2()
print(f"Inside example_function: {global_var}")