# Name: Tianyu Han
# Student ID: 260890959

import doctest
import copy
import numpy as np
import matplotlib.pyplot as plt
########################################
numbers = "0123456789"

########################################


def gender_switch(sex):
    ''' (str) -> str
    This function takes a string indicating a gender as input and returns a
    string M, F or X indicating male, female and non-binary respectively.

    >>> gender_switch("Homme")
    'M'
    >>> gender_switch("femme")
    'F'
    '''
    # use string.upper() to convert the sex into upper case
    sex = sex.upper()

    # create helpers lists to simplify the codes
    male = ["HOMME", "MALE", "H", "BOY", "MAN", "M"]
    female = ["FEMME", "FEMALE", "GIRL", "WOMAN", "F"]
    
    if sex in male:
        sex = "M"
    elif sex in female:
        sex = "F"
    else:
        sex = "X"
    return sex


def postal_code_switch(postal):
    ''' (str) -> str
    This function takes a string indicating a postal code as input and return
    the first three characters of the postal. If it's not applicable, return '000'.

    >>> postal_code_switch("H2X 1T6")
    'H2X'
    >>> postal_code_switch("N.A")
    '000'
    '''
    
    new_postal = "000"

    # since all postal codes start with 'H', if it's not, it's not a valid
    # postal code
    if postal[0] == "H":
        new_postal = postal[0:3]
    return new_postal


def temperature_switch(temps):
    ''' (list) -> list
    This function takes a list of temperatures as input and returns a list
    of floats which contains only the number part of each temperature.
    (If it's in Fahrenheit, convert it to Celsius.)

    >>> temperature_switch(['102.2'])
    [39.0]
    >>> temperature_switch(['102.2', '42 C'])
    [39.0, 42.0]
    '''

    # create a new list
    temp_list = []

    # use a nested loop to make changes to the temperatures in the input list
    # and add the processed temperatures to the empty list
    for temp in temps:
        new_temp = temp
        if type(new_temp) == str:
            if temp[0] not in numbers:
                temp_list.append(0.0)
            else:
                if "," in temp:
                    new_temp = new_temp.replace(",", ".")
                if new_temp[-1] == "C":
                    while new_temp[-1] not in numbers:
                    # use while loop to get rid of the non-number characters

                        new_temp = new_temp[:-1]
                    new_temp = float(new_temp)
                else:
                    while new_temp[-1] not in numbers:
                        new_temp = new_temp[:-1]
                    new_temp = float(new_temp)
                    if new_temp > 45:
                        new_temp = round(((new_temp - 32) / 1.8) , 1)
                temp_list.append(new_temp)
        else:
            new_temp = float(new_temp)
            if new_temp > 45:
                new_temp = round(((new_temp - 32) / 1.8) , 1)
            temp_list.append(new_temp)
    return temp_list

            
class Patient:
    def __init__(self, number, day_diagnosed, age, sex, postal, state, temps, days_symptomatic):
        self.num = int(number)
        self.day_diagnosed = int(day_diagnosed)
        self.age = int(age)
        self.sex_gender = gender_switch(sex)
        self.postal = postal_code_switch(postal)
        self.state = state
        if type(temps) == str:
            self.temps = temperature_switch([temps])
        elif type(temps) == list:
            self.temps = temperature_switch(temps)
        self.days_symptomatic = int(days_symptomatic)

    def __str__(self):
        ''' (object) -> string
        This function takes a object as input and return a string of the attributes
        in different order (compared to input), and separated by tabs.

        >>> p = Patient('0', '0', '42', 'Woman', 'H3Z2B5', 'I', '102.2', '12')
        >>> str(p)
        '0\\t42\\tF\\tH3Z\\t0\\tI\\t12\\t39.0'
        
        '''
        if type(self.temps) == list:
            self.temps_string = map(str, self.temps)
            self.temps_string = ";".join(self.temps_string)
        info = [str(self.num), str(self.age), self.sex_gender, self.postal, str(self.day_diagnosed), self.state, \
                str(self.days_symptomatic), self.temps_string]
        info = "\t".join(info)
        return info

    def update(self, other):
        ''' (object, object) -> object
        This function takes another patient as input and if this other object's
        numer, sex/gender, and postal code are all the same as the current patient,
        upadte the symptomatic days and the state to the newer one and append the
        new temperatures.
        
        >>> p = Patient('0', '0', '42', 'Woman', 'H3Z2B5', 'I', '102.2', '12')
        >>> p1 = Patient('0', '1', '42', 'F', 'H3Z', 'I', '40,0 C', '13')
        >>> str(p.update(p1))
        '0\\t42\\tF\\tH3Z\\t0\\tI\\t13\\t39.0;40.0'
        '''

        # use if to tell if their number, gender and postal code are the same
        if other.num == self.num and other.sex_gender == self.sex_gender and other.postal == self.postal:
            self.days_symptomatic = other.days_symptomatic
            self.state = other.state
            self.temps.extend(other.temps)

        # raise an exception
        else:
            raise AssertionError("These are two different patients.")
        
        return self
        


def stage_four(input_filename, output_filename):
    ''' (file, file) -> dict
    This function takes two files as input and will open the file with the name
    input_filename and read it line by line. Then create a new Patient object for
    each line. Then convert every Patient to a string and sorted by patient number,
    writes it into the out file. This function will return a dictionary of Patients.

    >>> p = stage_four("stage3.tsv", "stage4.tsv")
    >>> len(p)
    1894
    >>> str(p[0])
    '0\\t67\\tF\\tH1E\\t0\\tD\\t4\\t103.0;0.0'
    '''

    # open the two files
    in_file = open(input_filename, 'r', encoding = 'utf-8')
    out_file = open(output_filename, 'w+', encoding = 'utf-8')

    # use file.readlines() to create a list containing every line of the input file
    content = in_file.readlines()
    in_file.close()

    # create some helper variables
    result = {}
    patient_numbers = []
    keys = []

    # append the patient numbers to the empty list
    for item in content:
        item = item.strip()
        item = item.split("\t")
        if item[1] not in patient_numbers:
            patient_numbers.append(item[1])
            
    # use for loop to create a dictionary
    for item in content:
        item = item.strip()
        item = item.split("\t")
        element = copy.deepcopy(item)
        number = element[1]
        day_diagnosed = element[2]
        age = element[3]
        sex = element[4]
        postal = element[5]
        state = element[6]
        temps = element[7]
        days_symptomatic = element[8]
        patient = Patient(number, day_diagnosed, age, sex, postal, state, temps, days_symptomatic)
        if patient.num in keys:
            existing_patient = result.get(patient.num)
            result[int(patient.num)] = existing_patient.update(patient)
        else:
            keys.append(patient.num)
            result[int(patient.num)] = patient
    
    new_result = {}
    keys = list(result.keys())
    new_keys = copy.deepcopy(keys)
    
    # use list.sort() to sort the list, which will be the keys
    # in the dictionary, new_result
    new_keys.sort()
    
    values = list(result.values())
    for i in new_keys:
        new_result[i] = values[keys.index(i)]
    new_values = list(new_result.values())


    for item in new_values:
        out_file.write(str(item)+'\n')
    out_file.close()
    return new_result

            
def fatality_by_age(patient_dictionary):
    ''' (dict) -> list
    This function takes a dictionary as input and returns a list of probabilities
    of death by age group.
    
    >>> p = stage_four("stage3.tsv", "stage4.tsv")
    >>> fatality_by_age(p)
    [1.0, 1.0, 0.8888888888888888, 0.9230769230769231, 0.9230769230769231, 1.0, \
1.0, 1.0, 0.9, 0.92, 0.8666666666666667, 0.7647058823529411, 0.9411764705882353, \
0.9285714285714286, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    '''

    # create two dictionaried indicating people who have recovered and
    # who are dead respectively
    new_dict = {}
    new_dict_dead = {}

    # use for loop to determine the age group and add them to the
    # recovered dictionary or dead dictionary
    for i in patient_dictionary:
        value = patient_dictionary[i]
        age = value.age
        difference = age % 5
        if difference < 2.5:
            age = age - difference
        elif difference > 2.5:
            age = age + (5 - difference)
        if age not in new_dict:
            new_dict[age] = 0
        if age not in new_dict_dead:
            new_dict_dead[age] = 0
        if value.state == 'R':
            new_dict[age] += 1
        elif value.state == 'D' or value.state == 'M':
            new_dict_dead[age] += 1

    # this part is to transfer the values from the dictionaries into two lists
    # and sorts them according to their age group
    keys = list(new_dict.keys())
    keys.sort()
    recovered_list = []
    dead_list = []
    for key in keys:
        recovered_list.append(new_dict[key])
        dead_list.append(new_dict_dead[key])

    
    fatality = []
    for i in range(len(dead_list)):
        if dead_list[i] != 0 or recovered_list[i] != 0:
            fatality.append(dead_list[i]/(dead_list[i]+recovered_list[i]))
        elif dead_list[i] == 0 and recovered_list[i] == 0:
            fatality.append(1.0)

    # use numpy and matplotlib to generate the plot
    x_lable = np.array(keys)
    y_lable = np.array(fatality)
    plt.title("Probabilty of death vs age by Tianyu Han")
    plt.xlabel("Age")
    plt.ylabel("Deaths / (Deaths+Recoveries)")
    plt.plot(x_lable, y_lable)
    plt.ylim((0, 1.2))
    plt.savefig('fatality_by_age')
    return fatality


################################
if __name__ == "__main__":
    doctest.testmod()
        
        
