{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "0b10a7bf-a288-4e91-ba33-f20924e6c835",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sympy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "7aea5d08-c5bf-40c5-80b6-dd3bdf8993b4",
   "metadata": {},
   "outputs": [],
   "source": [
    "def derivative(f, h=1):\n",
    "    return lambda x: sympy.limit((f(x+h) - f(x)) / h, h, 0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "a290e8ca-ec5b-4afa-886b-7dea254f2b39",
   "metadata": {},
   "outputs": [],
   "source": [
    "def optimize(starting_x, num_of_steps, required_error, equation_first_derivative, equation_second_derivative):\n",
    "    list_of_steps = [starting_x]\n",
    "    error = 10000\n",
    "\n",
    "    if(type(num_of_steps) != \"int\"):\n",
    "        i=0\n",
    "        while(error > required_error):\n",
    "            last_step = list_of_steps[i]\n",
    "            next_step = last_step - equation_first_derivative(last_step)/equation_second_derivative(last_step)\n",
    "\n",
    "            list_of_steps.append(next_step)\n",
    "            error = last_step - next_step\n",
    "            i = i+1\n",
    "    else:\n",
    "        for i in range (num_of_steps):\n",
    "            last_step = list_of_steps[i]\n",
    "            next_step = last_step - equation_first_derivative(last_step)/equation_second_derivative(last_step)\n",
    "        \n",
    "            list_of_steps.append(next_step)\n",
    "    \n",
    "    return list_of_steps"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "94f3bbcb-65f4-4081-b262-f4144ec32216",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(21.0000000000000, 36.0000000000000)"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "equation = lambda x: 3*(x**3)\n",
    "\n",
    "equation_first_derivative = derivative(equation)\n",
    "equation_second_derivative = derivative(equation_first_derivative)\n",
    "equation_first_derivative(1), equation_second_derivative(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "81fc541b-4fd9-415f-acdd-ae72d10582d5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[10,\n",
       " 4.98484848484848,\n",
       " 2.46457614115842,\n",
       " 1.18418213788323,\n",
       " 0.515784856297557,\n",
       " 0.147938389503898]"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "optimize(starting_x=10, num_of_steps=\"no\", required_error = .5, equation_first_derivative=equation_first_derivative, equation_second_derivative=equation_second_derivative)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "f15b21c7-6395-4bf0-8c1f-d74dd3936284",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "int"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "type(1)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
