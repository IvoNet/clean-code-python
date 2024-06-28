# is it there or not

This code piece illustrates how to improve behavior.

We have a couple of customers interested in a product. these customers periodically go to the store to check if the
product is available. If the product is available, they buy it. If the product is not available, they leave the store.

How can we improve this code? What will it lead to?

## Solution

We will refactor this code to make use of the Observables pattern.
This pattern will allow us to notify the customers when the state of the store has changed.
e.g. when the store receives a new product.

### Steps to refactor:

- Create an observer interface
- give it an update method
- add addObserver and removeObserver methods to the store
- notify the observers when the store receives a new product
- refactor the customer class to implement the observer interface
- Tests should still pass without any changes at this point
- Change the customer class to use the observer pattern
- Change the store class to use the observer pattern
- Tests should still pass
- Add new tests to make to test the new behavior of the observer pattern
- All tests should still pass
- Remove the threaded tests as they are not needed anymore
- Coverage should still be 100%
- Test should be faster as no sleeps have bean build in anymore

This is the observer pattern in action.

Note that the removeObserver method is not strictly speaking part of the pattern, but that does not mean it is a bad
idea :-).
