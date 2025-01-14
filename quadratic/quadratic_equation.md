Let's start from the usefulness of understanding what an x/y graph represents.


For any 2d graph (a cartesian coordinate system for the sophisticate 🧐), _what we're representing is the output of a function_, where x is the input and y is the output.

Take an identity function, where x = y. (linear_pot.png)
```py
def identity(x):
    return x
```

Now pick any point on the x-axis, and the result of the function will determine what the y value will be.

```py
# linear_plot_point_2.png
y = identity(2)
# linear_plot_point_minus_3.png
y = identity(-3)
```

_Any_ function with this [signature](https://google.com) works this way.

```py
def addOne(x):
    return x + 1
```

which we would represent with this graph (linear.png)
