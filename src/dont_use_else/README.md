# dont-use-else

This code piece illustrates how to avoid using else in your code.

But why is it wrong to use else?

Well an else in any form can actually negate OO principles like polymorphism and inheritance. It can also make the code
harder to read and understand.

If you have a lot of type switches in the code it is a good idea to refactor it to use polymorphism instead.
If you do not and a new type is introduces you might have to change a lot of switches where these are "checked" in the
code. The trouble is finding them and this violates the open-closed principle.

To make the code adhere to the Single Responsibility Principle, it is better to avoid using else.

## Pros and Cons of eliminating the else.

### Pros

- Makes the code easier to read and understand
- Makes the code easier to test
- Makes the code easier to maintain
- Makes the code easier to refactor
- Makes the code easier to extend

### Cons

- More Classes
- Potentially more files

In this case:

- extract methods in the case or if else block
- tests should still pass without change
- further refactor the extracted methods to their own classes
- tests should still pass without change
- look at the code and see the common denominator in the extracted methods
- in this case all the methods use amount but only two use discount. The discount can be moved to the constructor of the
  class making the methods have the same signature
- tests should still pass without change
- now extract an interface called Discount with an apply method using the amount as parameters
- make PercentageDiscount/AbsoluteDiscount/NoneDiscount classes implement the Discount interface by changing the
  extracted method names to apply..
- Test must be changed to reflect the new interface but other than that should still pass
- now change the DiscountService to use the Discount interface instead of the extracted methods
- tests should still pass after changing to use the new Discount* Classes
- DiscountType can be removed as it is no longer needed

# But, but, but... I like my else statements

I get it. I like them too. But they are not always the best choice. In this case, it is better to avoid them.
even if you only have something like a boolean flag to check for a condition, it might be better to think about e.g. the
strategy pattern.

# Conclusion

Whenever you are inclined to write an if / else statement you should ask yourself:

> Is there is a better way to do this without using the else?
