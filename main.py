import random

class Die:

    def __init__(self) -> None:
        self._value = None

    @property
    def value(self):
        return self._value

    def roll(self) -> int:
        new_value = random.randint(1,6)
        self._value = new_value
        return new_value

#Test Die Class

#my_die = Die()
#my_die.roll()
#print(my_die.value)