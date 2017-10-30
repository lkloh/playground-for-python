import unittest
from fail_fast_test_helper import increase_employees_salary, Employee, TestIncreaseSalary





def get_existing_ids(employees, id_list):
    return list(filter(lambda id: id in xrange(len(employees)), id_list))

def increase_employees_salary_sanitize(employees, salary_update_list):
    id_list = get_existing_ids(employees, map(lambda p : p[0], salary_update_list))
    salary_update_list = [pair for pair in salary_update_list if pair[0] in id_list]
    if salary_update_list > 0:
        for id, new_salary in salary_update_list:
            employees[id].update_salary(new_salary)


class TestIncreaseSalarySanitize(TestIncreaseSalary):
    def setUp(self):
        self.test_update_salary_func = increase_employees_salary_sanitize
        self.alice = Employee('Alice', 'Anderson', 115, bonus=5)
        self.bob = Employee('Bob', 'Brown', 95, bonus=20)
        self.charlie = Employee('Charlie', 'Chaplin', 95, bonus=20)
        self.employees = [self.alice, self.bob, self.charlie]

if __name__ == '__main__':
    unittest.main()
