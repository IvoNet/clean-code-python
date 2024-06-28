# is it there or not

This code piece illustrates how to improve behavior.

We have a couple of customers interested in a product. these customers periodically go to the store to check if the
product is available. If the product is available, they buy it. If the product is not available, they leave the store.

How can we improve this code? What will it lead to?

## Solution

We will refactor this code to make use of the Observables pattern.
This pattern will allow us to notify the customers when the state of the store has changed.
e.g. when the store receives a new product.
