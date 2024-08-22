import sympy


def derivative(f, h=1): 
    return lambda x: sympy.limit((f(x + h) - f(x)) / h, h, 0)


def optimize(starting_x, num_of_steps, required_error, f_first_derivative, f_second_derivative): # Utilizes Newton's Method
    list_of_steps = [starting_x]
    error = 10000

    if type(num_of_steps) != "int": # This if-statement decides whether we are running a loop that goes until the error is below a certain size, or alternatively, a loop which has a set number of iterations
        i = 0
        while error > required_error:
            last_step = list_of_steps[i]
            next_step = last_step - f_first_derivative(last_step) / f_second_derivative(last_step)

            list_of_steps.append(next_step)
            error = last_step - next_step
            i = i + 1
    else:
        for i in range(num_of_steps):
            last_step = list_of_steps[i]
            next_step = last_step - f_first_derivative(last_step) / f_second_derivative(last_step)

            list_of_steps.append(next_step)

    return list_of_steps

# Creating our functions and their respective derivatives
f = lambda x: 3 * (x**3)
f_first_derivative = derivative(f)
f_second_derivative = derivative(f_first_derivative)

# Running our Newton's Method code
optimize(starting_x=10, num_of_steps="no", required_error=0.5, f_first_derivative=f_first_derivative, f_second_derivative=f_second_derivative)
