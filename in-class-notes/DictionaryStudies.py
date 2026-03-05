from dataclasses import dataclass
import dummy as Dummy

#

@dataclass
class MyType:

    def __init__(self, age : int, name: str):
        self._assert_age(age)
        self._assert_name(name)
        self._age = age
        self._name = name

    def __repr__(self):
        return f"MyType(age={self._age}, name='{self._name}')"

    @property
    def age(self):
        return self._age

    @property
    def name(self):
        return self._name

    @age.setter
    def age(self, age):
        self._assert_age(age)
        self._age = age

    @name.setter
    def name(self, name):
        self._assert_name(name)
        self._name = name

    @staticmethod
    def _assert_age(age : int) -> None:
        if not isinstance(age, int):
                raise TypeError("Age should be a integer.")

        if age < 0:
            raise ValueError("Age can't be less than 0.")

    @staticmethod
    def _assert_name(name : str) -> None:
        if not isinstance(name, str):
            raise TypeError("Name should be a string.")

        if not name:
            raise ValueError("Name can't be empty")

# Testing

def main() -> int:

    #

    correct_dict = {"2320813" : MyType(22, "Matheus")}
    print("Correct usage!")

    print(correct_dict)

    correct_dict["2320813"].age = 23
    correct_dict["2320813"].name = "Matthew"

    print(correct_dict)

    try:
        incorrect_dict = {"2320813" : MyType("Matheus", 22)}
    except Exception as error:
        print(f"Incorrect usage: {error}")

    # Lamba test

    calculate = lambda a, b : a + b
    print(f"Using lambda for 2+3: {calculate(2, 3)}")

    # Module test

    Dummy.DoYourThing()

    return 0

#

if __name__ == "__main__":
    main()