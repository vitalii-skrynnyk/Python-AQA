from pony.orm import Database, PrimaryKey, Required, Set

db = Database()
db.bind(provider='postgres', user='postgres', password='admin', host='127.0.0.1', database='postgres')


class Address(db.Entity):
    _table_ = 'addresses'
    address_id = PrimaryKey(int, auto=True)
    city = Required(str, 100)
    country = Required(str, 100)
    student = Set("Student")

    def __str__(self):
        return f"{self.address_id}-{self.country}-{self.city}"

    def __repr__(self):
        return f"{self.address_id}-{self.country}-{self.city}"


class Student(db.Entity):
    _table_ = "students"
    id = PrimaryKey(int, auto=True)
    email = Required(str, 100)
    name = Required(str, 100)
    l_name = Required(str, 100)
    address = Required(Address, column='address_id')
    course = Required('Course', column='course_id')

    def __str__(self):
        return f"{self.id}-{self.email}-{self.name}-{self.l_name}"

    def __repr__(self):
        return f"{self.id}-{self.email}-{self.name}-{self.l_name}"


class Course(db.Entity):
    _table_ = "courses"
    id = PrimaryKey(int, auto=True)
    course_name = Required(str, 100)
    star_date = Required(str, 100)
    end_date = Required(str, 100)
    student = Set("Student")

    def __str__(self):
        return f"{self.id}-{self.course_name}-{self.star_date}-{self.end_date}"

    def __repr__(self):
        return f"{self.id}-{self.course_name}-{self.star_date}-{self.end_date}"

db.generate_mapping(create_tables=True)