#
# Name: Reid Dye
#
# This module contains the Dog class (first class in HCS)
#

class Dog:
    """Dog class
       all typical accessor methods"""
    def __init__(self,name:str,breed:str,owner:str):
        """Dog.__init__(name, breed, owner): 
        Constructs a Dog object with the given name, breed, and owner.

        Args:
            name (str): The name of the dog
            breed (str): The breed of the dog
            owner (str): The owner's name
        """
        self.dogName = name
        self.dogBreed = breed
        self.owner = owner

    #getters and setters
    def getBreed(self):
        return self.dogBreed
    def getOwner(self):
        return self.owner
    def getName(self):
        return self.dogName

    def setBreed(self, breed:str):
        self.dogBreed=breed
    def setOwner(self, owner:str):
        self.owner=owner
    def setName(self, name:str):
        self.dogName=name

    #str and repr
    def __repr__(self):
        """Dog.__repr__()

        Returns:
            str: info about this dog, in a way that can be called to make another
        """
        return f'Dog({self.dogName}, {self.dogBreed}, {self.owner})'
    def __str__(self):
        "returns: info about dog, in human-readable format (str)"
        return f'<Dog object> Name: {self.dogName}, Breed: {self.dogBreed}, Owner: {self.owner}'
    


########## END OF DOG CLASS (TEST BELOW) ##########
    
# this function tests the Dog class
def main():
    dog1 = Dog("Chimmy","Whippet","Shin")
    dog2 = Dog("Onyx","Mixed breed","Richardson")
    dog3 = Dog("Chloe","Westie","Kashiwada")

    # expect this
    print(dog1)
    print()
    help(Dog.__init__)
    print()

    # CALL YOUR MUTATOR METHOD ON ONE OF THE DOG OBJECTS AND TEST IT
    

# this line calls the test function only when running this module
if __name__=="__main__":
    main()

    


