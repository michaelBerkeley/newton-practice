import sympy
def derivative(f, h=1):
    return lambda x: sympy.limit((f(x+h) - f(x)) / h, h, 0)

def optimize(starting_x, num_of_steps, required_error, equation_first_derivative, equation_second_derivative):
    list_of_steps = [starting_x]
    error = 10000

    if(type(num_of_steps) != "int"):
        i=0
        while(error > required_error):
            last_step = list_of_steps[i]
            next_step = last_step - equation_first_derivative(last_step)/equation_second_derivative(last_step)

            list_of_steps.append(next_step)
            error = last_step - next_step
            i = i+1
    else:
        for i in range (num_of_steps):
            last_step = list_of_steps[i]
            next_step = last_step - equation_first_derivative(last_step)/equation_second_derivative(last_step)
        
            list_of_steps.append(next_step)
    
    return list_of_steps


equation = lambda x: 3*(x**3)

equation_first_derivative = derivative(equation)
equation_second_derivative = derivative(equation_first_derivative)
equation_first_derivative(1), equation_second_derivative(1)

optimize(starting_x=10, num_of_steps="no", required_error = .5, equation_first_derivative=equation_first_derivative, equation_second_derivative=equation_second_derivative)