''' Course Class for Project 4 of CS 2420 '''

class Course:
    ''' Course object '''
    def __init__(self, number: int = 0, name: str = "", credit_hr: float = 0.0, grade: float = 0.0):
        self._number = number
        self._name = name
        self._credit_hr = credit_hr
        self._grade = grade

        if not isinstance(number, int):
            raise ValueError("Number must be an integer")
        if number < 0:
            raise ValueError("Number cannot be negative")
        if not isinstance(grade, float):
            raise ValueError("Grade must be a decimal number")
        if not isinstance(credit_hr, float):
            raise ValueError("Credit hours must be decimal number")
        if credit_hr < 0.0:
            raise ValueError("Credit hours must be positive")
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not 0.0 <= grade <= 4.0:
            raise ValueError("Grade must be between 0.0 and 4.0")
        if grade < 0.0:
            raise ValueError("Grade must be positive")

    def number(self):
        return int(self._number)

    def name(self):
        return self._name

    def credit_hr(self):
        return self._credit_hr

    def grade(self):
        return self._grade

    def __str__(self):
        return f"cs{self._number} {self._name} Grade: {self._grade} Credit Hours: {self._credit_hr}"

    def __eq__(self, other):
        if isinstance(other, Course):
            return self._number == other._number
        return False

    def __lt__(self, other):
        other_course = other
        if isinstance(other, Course):
            other_course = other.number()
        return other_course < self.number()

    def __gt__(self, other):
        other_course = other
        if isinstance(other, Course):
            other_course = other.number()
        return other_course > self.number()

    def __le__(self, other):
        other_course = other
        if isinstance(other, Course):
            other_course = other.number()
        return other_course <= self.number()

    def __ge__(self, other):
        other_course = other
        if isinstance(other, Course):
            other_course = other.number()
        return other_course >= self.number()
