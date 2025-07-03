# class that validates on the name and breed of a dog

# These are the global list approved dog breeds;
# APPROVED_BREEDS = [
  #  "Mastiff",
   # "Chihuahua",
    #"Corgi",
   # "Shar Pei",
    #"Beagle",
    #"French Bulldog",
   # "Pug",
    #"Pointer"
# ]

class Dog:
    approved_breeds = [
        "Mastiff", "Chihuahua", "Corgi", "Shar Pei", 
        "Beagle", "French Bulldog", "Pug", "Pointer"
    ]
    #class attributes

    def __init__(self, name="Dog", breed="Corgi"): # Default values for name and breed are "Dog" and "Corgi"
        self.name = name # instance attributes
        self.breed = breed # instance attributes

    @property
    def name(self):
        return self._name
    # Allows us to access name like an attribute    

    @name.setter # Validates name
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25: # Sets condition where name is between 1 & 25 characters.
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed
    # Allows us to access breed like an attribute

    @breed.setter
    def breed(self, value):
        if value in Dog.approved_breeds: # You can call the class with the class variable
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")

    
