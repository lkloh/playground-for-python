
import unittest

class Employee:
    def __init__(self, firstname, lastname, salary, bonus=0):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.bonus = bonus

    def update_salary(self, new_salary):
        if new_salary > 0:
            self.salary = new_salary
        else:
            raise 'Salary should be a positive number'

    def get_salary(self):
        return self.salary

    def get_bonus(self):
        return self.bonus

    def update_bpnus(self, new_bonus):
        if new_bonus > 0:
            self.bonus = new_bonus
        else:
            raise 'Bonus should be a positive number'

    def __str__(self):
        return 'Employee %s %s has a salary of $%d and bonus of $%d' % (self.firstname, self.lastname, self.salary, self.bonus)


def increase_employees_salary(employees, salary_update_list):
    for id, new_salary in salary_update_list:
        employees[id].update_salary(new_salary)


class TestIncreaseSalary(unittest.TestCase):
    def setUp(self):
        self.test_update_salary_func = increase_employees_salary
        self.alice = Employee('Alice', 'Anderson', 115, bonus=5)
        self.bob = Employee('Bob', 'Brown', 95, bonus=20)
        self.charlie = Employee('Charlie', 'Chaplin', 95, bonus=20)
        self.employees = [self.alice, self.bob, self.charlie]

    def test_update(self):
    	salary_update_list_accurate = [
            (0, 120),
            (2, 100),
        ]
        self.assertEqual(self.employees[0].get_salary(), 115)
        self.assertEqual(self.employees[2].get_salary(), 95)

        self.test_update_salary_func(self.employees, salary_update_list_accurate)

        print self.employees[0]

        self.assertEqual(self.employees[0].get_salary(), 120)
        self.assertEqual(self.employees[2].get_salary(), 100)

    def test_off_by_one(self):
    	salary_update_list_wrong = [
            (1, 120),
            (3, 100),
        ]
        self.assertEqual(self.employees[0].get_salary(), 115)
        self.assertEqual(self.employees[2].get_salary(), 95)

        self.test_update_salary_func(self.employees, salary_update_list_wrong)

        self.assertEqual(self.employees[0].get_salary(), 120)
        self.assertEqual(self.employees[2].get_salary(), 100)

