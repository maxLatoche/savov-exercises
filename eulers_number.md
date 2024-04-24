When calculating the derivative of some function like 2^t, it might seem like the rate of change (which is essentially what we're solving for) is the same as the function.  Every period, the size doubles, so the rate of change is 2^t.

2^1 === 2
2^2 === 4
2^3 === 8
2^4 === 16

but the period is too large, we're looking for the instantaneous rate of change, not the rate of change after each "step"

So we're looking for "super small change in value"/"super small change in time", and in reality we're not going to find the infinitesimally small number to plug into that equation, we'll look for what that value _approaches_.   Think of Achilles and the tortoise, taking imperceptibly small step after imperceptibly small step.

rate_of_change(2^t)/rate_of_change = 2^t NO

for this to hold, we'd have to keep that period of "1 unit"

1(2^t)/1 = 2^t

But we know that period is too large, what happens when we approach 0, instantaneous rate of change?

the new state after the change would be 2^t * 2^rate_of_change

take the difference between the state after the change and the state before (2^t * 2^rate_of_change) - 2^t

finally, we want the average rate of change per unit, not the absolute change in a given time t.  So divide by the rate of change

((2^t * 2^rate_of_change) - 2^t)/rate_of_change

Now that we have that, factor out the value specific to are problem and leave the general formula that's applicable for any base.

2^t((2^rate_of_change - 1)/rate_of_change)

x^t((x^rate_of_change - 1)/rate_of_change)

As we plug in smaller and smaller values for rate_of_change, it approaches 0.6931472...  which is a _type_ of constant, but it's not the constant we're after because it changes based on the value of x.

2 === 0.6931472
3 === 1.0986123
4 === 1.3862944
5 === 1.6094380

So the rate of change we _thought_ was equal to itself is actually proportional to itself, multiplied by a factor of that proportionality constant.

slope where y
m === 2^t(0.6931472) | y === 2^t
m === 3^t(1.0986123) | y === 3^t
m === 4^t(1.3862944) | y === 4^t
m === 5^t(1.6094380) | y === 5^t

