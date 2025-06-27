# main_script.py
import my_module

print("This is the main script.")
print(f"__name__ in main_script: {__name__}")

my_module.my_function()
print(my_module.my_variable)
