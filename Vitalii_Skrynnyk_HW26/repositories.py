from models import AddressModel, CourseModel, StudentModel
from session import session


class AddressRepository:
    """Class with base quires for the "addresses" table"""

    def __init__(self):
        self.__session = session
        self.__model = AddressModel

    def get_all(self) -> AddressModel:
        """
        Get all data from the "addresses" table
        :return: addresses: all data from the "addresses" table
        """
        addresses: AddressModel | None | list = self.__session.query(self.__model).all()
        return addresses

    def get_by_id(self, address_id: int) -> AddressModel:
        """
        Get only one row from the "addresses" table by provided address_id
        :param address_id: identifier for a row in "addresses" table
        :return: address: one row from the "addresses" table
        """
        address: AddressModel | None = self.__session.get(
            self.__model, {"address_id": address_id}
        )
        return address

    def create_new(self, address_model: AddressModel) -> bool:
        """
        Create new row in the "addresses" table
        :param address_model: Data model for a new row in "addresses" table
        :return: bool
        """
        try:
            self.__session.add(address_model)
            return True
        except:
            return False

    def delete(self, id: int) -> bool:
        """
        Delete a row in "addresses" table by provided id
        :param id: identifier for a row
        :return: bool
        """
        try:
            address = self.get_by_id(id)
            self.__session.delete(address)
            return True
        except:
            return False

    def update(self, address_model: AddressModel) -> None:
        """
        Update a row in "addresses" table with provided data
        :param address_model: data model for updating a row in "addresses" table
        :return: None
        """
        self.__session.query(self.__model).filter(
            AddressModel.address_id == address_model.address_id
        ).update(
            {
                AddressModel.city: address_model.city,
                AddressModel.country: address_model.country,
            }
        )


class CoursesRepository:
    """Class with base quires for the "courses" table"""

    def __init__(self):
        self.__session = session
        self.__model = CourseModel

    def get_all(self) -> CourseModel:
        """
        Get all data from the "courses" table
        :return: courses: all data from the "courses" table
        """
        courses: CourseModel | None | list = self.__session.query(self.__model).all()
        return courses

    def get_by_id(self, id: int) -> CourseModel:
        """
        Get only one row from the "courses" table by provided id
        :param id: identifier for a row in "courses" table
        :return: courses: one row from the "courses" table
        """
        courses: CourseModel | None = self.__session.get(self.__model, {"id": id})
        return courses

    def create_new(self, course_model: CourseModel) -> bool:
        """
        Create new row in the "courses" table
        :param course_model: Data model for a new row in "courses" table
        :return: bool
        """
        try:
            self.__session.add(course_model)
            return True
        except:
            return False

    def delete(self, id: int) -> bool:
        """
        Delete a row in "courses" table by provided id
        :param id: identifier for a row
        :return: bool
        """
        try:
            course = self.get_by_id(id)
            self.__session.delete(course)
            return True
        except:
            return False

    def update(self, course_model: CourseModel) -> None:
        """
        Update a row in "courses" table with provided data
        :param course_model: data model for updating a row in "courses" table
        :return: None
        """
        self.__session.query(self.__model).filter(
            CourseModel.id == course_model.id
        ).update(
            {
                CourseModel.course_name: course_model.course_name,
                CourseModel.start_date: course_model.start_date,
                CourseModel.end_date: course_model.end_date,
            }
        )


class StudentsRepository:
    """Class with base quires for the "students" table"""

    def __init__(self):
        self.__session = session
        self.__model = StudentModel

    def get_all(self) -> StudentModel:
        """
        Get all data from the "students" table
        :return: students: all data from the "students" table
        """
        students: StudentModel | None | list = self.__session.query(self.__model).all()
        return students

    def get_by_id(self, id: int) -> StudentModel:
        """
        Get only one row from the "students" table by provided id
        :param id: identifier for a row in "students" table
        :return: courses: one row from the "students" table
        """
        students: StudentModel | None = self.__session.get(self.__model, {"id": id})
        return students

    def create_new(self, student_model: StudentModel) -> bool:
        """
        Create new row in the "students" table
        :param student_model: Data model for a new row in "students" table
        :return: bool
        """
        try:
            self.__session.add(student_model)
            return True
        except:
            return False

    def delete(self, id: int) -> bool:
        """
        Delete a row in "students" table by provided id
        :param id: identifier for a row
        :return: bool
        """
        try:
            student = self.get_by_id(id)
            self.__session.delete(student)
            return True
        except:
            return False

    def update(self, student_model: StudentModel) -> None:
        """
        Update a row in "students" table with provided data
        :param student_model: data model for updating a row in "students" table
        :return: None
        """
        self.__session.query(self.__model).filter(
            StudentModel.id == student_model.id
        ).update(
            {
                StudentModel.name: student_model.name,
                StudentModel.email: student_model.email,
                StudentModel.address_id: student_model.address_id,
                StudentModel.course_id: student_model.course_id,
            }
        )


if __name__ == "__main__":
    # courses: get_all, get_by_id
    course_repo = CoursesRepository()
    print(course_repo.get_all())
    print((course_repo.get_by_id(1)))

    # courses: create
    new_course = CourseModel()
    new_course.id = 6
    new_course.course_name = "Python advanced"
    new_course.start_date = "10.10"
    new_course.end_date = "12.29"
    new_course.student_id = 1
    course_repo.create_new(new_course)
    print(course_repo.get_all())

    # courses: delete
    course_repo.delete(2)
    print(course_repo.get_all())

    # courses: update
    course_update = CourseModel()
    course_update.id = 3
    course_update.course_name = "C#"
    course_update.start_date = "11.11"
    course_update.end_date = "12.12"
    course_repo.update(course_update)
    print(course_repo.get_all())

    ###########################################################

    # student: get_all, get_by_id
    student_repo = StudentsRepository()
    print(student_repo.get_all())
    print((student_repo.get_by_id(1)))

    # students: create
    new_student = StudentModel()
    new_student.id = 4
    new_student.name = "Vitalii 2"
    new_student.email = "email"
    new_student.address_id = 1
    new_student.course_id = 1
    student_repo.create_new(new_student)
    print(student_repo.get_all())

    # students: delete
    student_repo.delete(2)
    print(student_repo.get_all())

    # students: update
    student_update = StudentModel()
    student_update.id = 3
    student_update.name = "V"
    student_update.email = "email 2"
    student_update.address_id = 1
    student_update.course_id = 5
    student_repo.update(student_update)
    print(student_repo.get_all())

    ################################################

    # addresses: get_all, get_by_id
    address_repo = AddressRepository()
    print(address_repo.get_all())
    print((address_repo.get_by_id(1)))

    # addresses: create
    new_address = AddressModel()
    new_address.address_id = 4
    new_address.city = "Kyiv"
    new_address.country = "Ukraine"
    address_repo.create_new(new_address)
    print(address_repo.get_all())

    # addresses: delete
    address_repo.delete(2)
    print(address_repo.get_all())

    # addresses: update
    address_update = AddressModel()
    address_update.address_id = 3
    address_update.city = "Lviv"
    address_update.country = "Ukraine"
    address_repo.update(address_update)
    print(address_repo.get_all())
