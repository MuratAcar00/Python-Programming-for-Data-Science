🧠 Python Functions – Notes from Python Programming for Data Science
This section contains structured notes on Python functions, based on the course Python Programming for Data Science by Miuul. It covers key concepts, usage patterns, and best practices.

📌 What is a Function?
A function is a reusable block of code designed to perform a specific task. It helps reduce repetition, organizes code better, and improves readability.

You define a function using the def keyword, followed by the function name and parentheses. Inside the parentheses, you can define parameters.

For example, a basic function definition:

def greet():

Inside the function body, you write the code to be executed.

You can use return to send back a result.

🧱 Topics Covered
1. Defining a Function
To define a function, use the syntax:
def function_name(parameters):

You can leave the parameter list empty or include one or more parameters.

Example:
A function named greet that takes a name parameter and returns a greeting message.

2. Calling a Function
After defining a function, you can call it by writing its name followed by parentheses.
If the function has parameters, you must pass values to them during the call.

Example:

Calling greet("Murat") returns “Hello, Murat”.

Calling greet() (if a default is set) returns “Hello, Guest”.

3. Return Statement
The return keyword is used to send back the result from a function.
You can store this result in a variable or use it directly.

4. Default Parameters
You can assign default values to parameters so that they are optional during function calls.

Example:
If a parameter is defined as name="Guest", calling the function without providing name will use the default value “Guest”.

5. Flexible Number of Arguments
Use *args to pass a variable number of positional arguments.

Use **kwargs to pass a variable number of keyword arguments.

This allows more flexible and dynamic function calls.

6. Lambda Functions
Lambda functions are small, anonymous functions defined using the lambda keyword.

They are useful for quick one-line operations and are often used with functions like map, filter, and sorted.

Example:
A lambda that adds two numbers could be written as: lambda x, y: x + y

7. Scope and Namespace
Variables defined inside a function are local and not accessible outside.

Global variables can be accessed inside functions unless shadowed.

Use the global keyword if you want to modify a global variable from inside a function.

8. Nested Functions
You can define a function inside another function.
Inner functions can be used to encapsulate logic and maintain cleaner scopes.

9. Comprehensions within Functions
Inside functions, you can use:

List comprehensions

Dictionary comprehensions

Set comprehensions

These provide a concise way to generate new data structures from iterable objects.

10. Best Practices
Use meaningful function names

Keep functions short and focused on a single task

Add docstrings to explain what the function does

Avoid side effects unless necessary

Reuse code by creating general-purpose functions

🎯 Why Use Functions?
To organize code into logical sections

To reuse logic multiple times

To make testing and debugging easier

To follow modular programming principles

📌 Source
These notes are based on the Python Programming for Data Science course by Miuul, and are intended for educational and personal study purposes.
