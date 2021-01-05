from datetime import datetime as dt


class Pet:
    def __init__(self, name, dob, weight, owner):
        self.__name = name
        self.__dob = dob
        self.__weight = weight
        self.__owner = owner

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def get_weight(self):
        return self.__weight

    def get_owner(self):
        return self.__owner

    def set_name(self, n):
        self.__name = n

    def set_dob(self, d):
        self.__dob = d

    def set_weight(self, w):
        self.__weight = w

    def set_owner(self, o):
        self.__owner = o

    def calage(self):
        age = (dt.now().date() - self.get_dob()).days
        age = int(age)
        return age

    def __str__(self):
        result = 'Pet Name: {0}; Pet DOB: {1}; Birth Weight {2}\n'.format(self.__name, self.__dob, self.__weight )
        result += 'Owner Name: {0}; Owner Address: {1}\n'.format(self.__owner.get_ownername(),self.__owner.get_address())
        return result


class Mammal(Pet):
    def __init__(self, name, dob, weight, owner, size, hasclaws):
        super().__init__(name, dob, weight, owner)
        self.__size = size
        self.__hasclaws = hasclaws

    def get_size(self):
        return self.__size

    def get_hasclaws(self):
        return self.__hasclaws

    def set_size(self, s):
        self.__size = s

    def set_hasclaws(self, h):
        self.__hasclaws = h

    def calweight(self):
        age = self.calage()
        if age < 301:
            self.set_weight(self.get_weight() * (pow((1 + 8 / 100), age//50)))
            return self.get_weight()
        elif age > 300:
            self.set_weight(self.get_weight()*(pow((1 + 8 / 100), 6)))
            return self.get_weight()

    def __str__(self):
        print("Details of this Mammal pet are:")
        result = Pet.__str__(self)
        result += 'Litter Size: {0}; Has Claws? {1}\n'.format(self.__size, 'Yes' if self.__hasclaws == True else 'No')
        return result


class Fish(Pet):
    def __init__(self, name, dob, weight, owner, condition, length):
        super().__init__(name, dob, weight, owner)
        self.__condition = condition
        self.__length = length

    def get_condition(self):
        return self.__condition

    def get_length(self):
        return self.__length

    def set_condition(self, c):
        self.__condition = c

    def set_length(self, le):
        self.__length = le

    def calweight(self):
        age = self.calage()
        if age < 361:
            self.set_weight(self.get_weight() * (pow((1 + 4 / 100), age // 90)))
            return self.get_weight()
        elif age > 360:
            self.set_weight(self.get_weight() * (pow((1 + 4 / 100), 4)))
            return self.get_weight()

    def __str__(self):
        print("Details of this Fish pet are:")
        result = Pet.__str__(self)
        result += 'Scale Condition : {0}; Length: {1}\n'.format(self.__condition, self.__length)
        return result


class Amphibians(Pet):
    def __init__(self, name, dob, weight, owner, isVenomous):
        super().__init__(name, dob, weight, owner)
        self.__isVenomous = isVenomous

    def get_isVenomous(self):
        return self.__isVenomous

    def set_isVenomous(self, i):
        self.__isVenomous = i

    def calweight(self):
        age = self.calage()  # age = (dt.now().date() - self.get_dob()).days
        if age < 361:
            self.set_weight(self.get_weight() * (pow((1 + 5 / 100), age // 120)))
            return self.get_weight()
        elif age > 360 and age <601:
            self.set_weight(self.get_weight() *(pow((1 + 5 / 100), 3)) * (pow((1 + 3 / 100), (age - 360) // 120)))
            return self.get_weight()
        elif age > 600:

            self.set_weight(self.get_weight() * (pow((1 + 5 / 100),3) ) * (pow((1 + 3 / 100),2)))
            return self.get_weight()

    def __str__(self):
        print("Details of this Amphibian pet are:")
        result = Pet.__str__(self)
        result += 'Is Venomous? {0}\n'.format('Yes' if self.__isVenomous == True else 'No')
        return result


class Person:
    def __init__(self, ownername, address):
        self.__ownername = ownername
        self.__address = address

    def get_ownername(self):
        return self.__ownername

    def get_address(self):
        return self.__address

    def set_ownername(self, on):
        self.__ownername = on

    def set_address(self, a):
        self.__address = a