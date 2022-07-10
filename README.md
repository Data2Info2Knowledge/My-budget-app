# Budget App

Here is my take on the Budget App project, part of [freeCodeCamp.org](https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app)'s *Scientific Computing with Python* Certification.  
This was quite an interesting introduction to object-oriented programming in Python.  

The only frustrating bit had to do with the spending chart, which ended up consuming a disproportionate amount of time, as the instructions weren't all that clear, specifically: 
> 'The percentage spent should be calculated only with withdrawals and not with deposits.'

* First, I just ignored that and calculated *total out / total in*, with predictable results. 
Then I figured out it meant:  
*(total spend in a given category)/(overall total spend)*.

* The next difficulty was largely of my own making, as I didn't pay enough attention to the conversion of percentages into bars of stacked 'o' characters:
>'The height of each bar should be rounded **down** to the nearest 10.'

I started out just rounding to the nearest 10,  
`pcround = round(100*pcspent,-1)`  
then decided to use `int()` instead of `round()`, as in:  
`pcround = int(10*pcspent)*10`

* Lastly, some tweaking was necessary to force the output to look like what was expected by the automated test module. This wasn't helped by the fact I'd chosen to use a list containing the lines of output, then concatenate it all using the `join()` method.