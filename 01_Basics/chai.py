# bring method from hello_chai and execute the method

from hello_chai import chai

chai("ginger tea");
# after runnig this a new folder is started named as "__pycache__"
###
# __pycache__ is a folder automatically created by Python.
# worls only for imported file
# 👉 What it contains?

# It stores compiled bytecode files (.pyc files).

# Example:

# myfile.py
# __pycache__/
#    myfile.cpython-311.pyc
# 👉 Why it is created?

# When you run a Python file:

# Python converts .py → bytecode

# Saves it inside __pycache__

# Next time, Python loads the .pyc file
# ➝ Program runs faster

# 👉 Can you delete it?

# ✅ Yes.
# Python will recreate it automatically.
###