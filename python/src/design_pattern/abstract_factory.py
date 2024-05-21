from __future__ import annotations

from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    """
    The Abstract Factory interface defines a set of methods to create various
    abstract products. These products form a family that shares a common theme
    or concept. Typically, products within a family can collaborate with each
    other, and different families of products are incompatible.
    """

    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):
    """
    Concrete Factories produce a family of products belonging to a specific
    variant. The factory ensures that the resulting products are compatible.
    Notably, the method signatures of Concrete Factory return abstract products,
    while actual concrete products are instantiated inside the methods.
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    """
    Each Concrete Factory corresponds to a specific product variant.
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


class AbstractProductA(ABC):
    """
    Each unique product in a product family should have a base interface. All
    product variants must adhere to this interface.
    """

    @abstractmethod
    def perform_function_a(self) -> str:
        pass


# Concrete Factories produce a family of concrete products that belong to a single variant.


class ConcreteProductA1(AbstractProductA):
    def perform_function_a(self) -> str:
        return "The outcome of product A1."


class ConcreteProductA2(AbstractProductA):
    def perform_function_a(self) -> str:
        return "The outcome of product A2."


class AbstractProductB(ABC):
    """
    This is the base interface for another product. All products can interact
    with each other, but meaningful interaction occurs only between products of
    the same concrete variant.
    """

    @abstractmethod
    def execute_function_b(self) -> None:
        """
        Product B can perform its own functionality...
        """
        pass

    @abstractmethod
    def collaborate_function_b(self, collaborator: AbstractProductA) -> None:
        """
        ...and it can collaborate with Product A.

        The Abstract Factory ensures that all products it creates belong to the
        same variant, ensuring compatibility.
        """
        pass


# Concrete Factories produce concrete products, that belong to a single variant.


class ConcreteProductB1(AbstractProductB):
    def execute_function_b(self) -> str:
        return "The outcome of product B1."

    """
    Product B1 is only compatible with Product A1. Nevertheless, it accepts any
    instance of AbstractProductA as an argument.
    """

    def collaborate_function_b(self, collaborator: AbstractProductA) -> str:
        result = collaborator.perform_function_a()
        return f"The outcome of B1 collaborating with ({result})"


class ConcreteProductB2(AbstractProductB):
    def execute_function_b(self) -> str:
        return "The outcome of product B2."

    def collaborate_function_b(self, collaborator: AbstractProductA):
        """
        Product B2 is only compatible with Product A2. Nevertheless, it accepts
        any instance of AbstractProductA as an argument.
        """
        result = collaborator.perform_function_a()
        return f"The outcome of B2 collaborating with ({result})"


def client(factory: AbstractFactory) -> None:
    """
    The client code interacts with factories and products solely through
    abstract types: AbstractFactory and AbstractProduct. This enables the
    passing of any factory or product subclass to the client code without
    causing disruptions.
    """
    print(f"Client: I'm not aware of the factory's class, but it still works.")
    print(f"Apparently this time my factory is {factory.__class__.__name__}")
    print("and I just do my thing with it.")
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.execute_function_b()}")
    print(f"{product_b.collaborate_function_b(product_a)}", end="")
    print()
    print("=" * 80)


if __name__ == "__main__":
    """
    The client works with any concrete factory class.
    """
    client(ConcreteFactory1())
    client(ConcreteFactory2())
