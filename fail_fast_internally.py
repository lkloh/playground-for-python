
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

    def update_bpnus(self, new_bonus):
        if new_bonus > 0:
            self.bonus = new_bonus
        else:
            raise 'Bonus should be a positive number'

    def __str__(self):
        return 'Employee %s %s has a salary of $%d and bonus of $%d' % (self.firstname, self.lastname, self.salary, self.bonus)

_employees = [
    Employee('Alice', 'Anderson', 115, bonus=5),
    Employee('Bob', 'Brown', 95, bonus=20),
    Employee('Charlie', 'Chaplin', 95, bonus=20),
];

def print_employees():
    print '\nEMPLOYEES:'
    for e in _employees:
        print str(e)
    print '\n'

def get_existing_ids(id_list):
    return list(filter(lambda id: id in xrange(len(_employees)), id_list))

def increase_employees_salary_by_five(salary_update_list):
    for id, new_salary in salary_update_list:
        _employees[id].update_salary(new_salary)

if __name__ == '__main__':
    print_employees()
    salary_update_list = [
        (0, 120),
        (2, 100),
    ]
    increase_employees_salary_by_five(salary_update_list)
    print_employees()

