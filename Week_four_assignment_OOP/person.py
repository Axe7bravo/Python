class Person:
  #Represents a person with name, age, and gender

  def __init__(self, name, age, gender):
    """Initializes a new Person object.

    Args:
      name (str): The person's name.
      age (int): The person's age.
      gender (str): The person's gender.
    """
    self.name = name
    self.age = age
    self.gender = gender

  def introduce(self):
    #Introduces the person with their name, age, and gender.
    print(f"Hello, my name is {self.name}. I am {self.age} years old and I am a {self.gender}.")

# Create an instance of the Person class
person = Person("Teboho", 34, "male")

# Call the introduce method
person.introduce()