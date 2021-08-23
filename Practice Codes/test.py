import datetime
class Cat:

    number_of_cats = 0
    def __init__(self, name, age = 0):
        self.name = name
        self.age = age
        Cat.number_of_cats += 1

    def __str__(self):
        info = "Name: " + self.name + ' ' + "Age: " + str(self.age)
        return info

    def __eq__(self, other):
        if self.name == other.name:
            if self.age == other.age:
                return True
            else:
                return False
        else:
            return False

    def is_older_than(self, other):
        return self.age > other.age

    @staticmethod
    def find_oldest(cats):
        '''
        ages = []
        if len(cats) == 0:
            return -1
        else:
            for i in range(len(cats)):
                ages.append(cats[i].age)
            index = ages.index(max(ages))
            return index
        '''

        if len(cats) == 0:
            return -1
        else:
            index = 0
            oldest = cats[0]
            for i, c in enumerate(cats):
                if c.is_older_than(oldest):
                    oldest = c
                    index = i
            return index

    @classmethod
    def from_birthdate(cls, name, birthday):
        now = datetime.date.today()
        diff = now - birthday # the minus operator is overloaded in the date class
        age = diff.days // 365
        return cls(name, age)

cat1 = Cat("Tiger", 2)
cat2 = Cat("Jimmy", 3)
cat3 = Cat("Mary", 12)
c = [cat1, cat2, cat3]
print(type(c[0]))
birth = datetime.date(2010, 9, 21)
cat4 = Cat.from_birthdate("Jess", birth)

        
