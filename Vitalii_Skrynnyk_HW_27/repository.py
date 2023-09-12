from pony.orm import db_session, select, commit
from models import Student, Address


class StudentRepo:
    def __init__(self):
        self.model = Student

    @db_session
    def update_name_by_id(self, id, name):
        student = self.get_by_id(id)
        student.email = name

    @db_session
    def create(self, email, name, l_name, address, course):
        self.model(email=email, name=name, l_name=l_name, address=address, course=course)

    @db_session
    def delete_by_id(self, id):
        student = self.get_by_id(id)
        student.delete()

    @db_session
    def get_by_id(self, id):
        student = self.model.get(lambda s: s.id == id)
        return student

    @db_session
    def get_all(self):
        students = Student.select(lambda s: s).prefetch(Address).page(1).to_list()
        return students

    @db_session
    def get_all_by_name(self, name):
        student = self.model.select(lambda s: s.name == name).prefetch(Address).page(1).to_list()
        return student

    @db_session
    def get_all_by_name_using_cycle(self, name):
        students = select(s for s in self.model if s.name == name).prefetch(Address).page(1).to_list()
        return students

    @db_session
    def get_all_by_name_and_sql(self, name):
        students = self.model.select_by_sql(f"SELECT * FROM students WHERE name = '{name}'")
        return students


class AddressRepo:
    def __init__(self):
        self.model = Address

    @db_session
    def get_by_id(self, id):
        address = self.model.get(lambda a: a.address_id == id)
        return address

    @db_session
    def select_all(self):
        addresses = select(address for address in self.model).page(1).to_list()
        return addresses

    @db_session
    def update_address_by_id(self, id, city, country):
        address = self.get_by_id(id)
        address.city = city
        address.country = country

    @db_session
    def create(self, city, country, student):
        self.model(city=city, country=country, student=student)

    @db_session
    def delete_by_id(self, id):
        address = self.get_by_id(id)
        address.delete()

    @db_session
    def get_all_by_city(self, city):
        address = self.model.select(lambda ad: ad.name == city).prefetch(Address).page(1).to_list()
        return address

    @db_session
    def get_all_by_city_using_cycle(self, city):
        addresses = select(ad for ad in self.model if ad.name == city).prefetch(Address).page(1).to_list()
        return addresses

    @db_session
    def get_all_by_city_and_sql(self, city):
        addresses = self.model.select_by_sql(f"SELECT * FROM students WHERE name = '{city}'")
        return addresses


class CourseRepo:
    def __init__(self):
        self.model = Address

    @db_session
    def get_by_id(self, id):
        course = self.model.get(lambda c: c.id == id)
        return course

    @db_session
    def select_all(self):
        courses = select(course for course in self.model).page(1).to_list()
        return courses

    @db_session
    def update_course_by_id(self, id, course_name, start_date, end_date):
        course = self.get_by_id(id)
        course.course_name = course_name
        course.start_date = start_date
        course.end_date = end_date

    @db_session
    def create(self, course_name, start_date, end_date):
        self.model(city=course_name, country=start_date, student=end_date)

    @db_session
    def delete_by_id(self, id):
        course = self.get_by_id(id)
        course.delete()

    @db_session
    def get_all_by_course_name(self, course_name):
        course = self.model.select(lambda c: c.name == course_name).prefetch(Address).page(1).to_list()
        return course

    @db_session
    def get_all_by_course_name_using_cycle(self, course_name):
        courses = select(c for c in self.model if c.name == course_name).prefetch(Address).page(1).to_list()
        return courses

    @db_session
    def get_all_by_course_name_and_sql(self, course_name):
        courses = self.model.select_by_sql(f"SELECT * FROM students WHERE name = '{course_name}'")
        return courses


if __name__ == '__main__':
    repo_student = StudentRepo()
    repo_address = AddressRepo()
    course_repo = CourseRepo()


    student = repo_student.get_by_id(1)
    students = repo_student.get_all_by_name_using_cycle('Vitalii')

    print(f"{student}\n, {students}")

