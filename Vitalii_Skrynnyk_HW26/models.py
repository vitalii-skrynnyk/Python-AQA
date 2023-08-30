from sqlalchemy import Column, INTEGER, VARCHAR, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class AddressModel(Base):
    """Data model for "addresses" table"""

    __tablename__ = "addresses"
    address_id = Column(INTEGER, primary_key=True)
    city = Column(VARCHAR)
    country = Column(VARCHAR)
    student = relationship("StudentModel", back_populates="address")

    def __str__(self):
        return (
            f"address_id: {self.address_id}, city: {self.city}, country: {self.country}"
        )

    def __repr__(self):
        return (
            f"address_id: {self.address_id}, city: {self.city}, country: {self.country}"
        )


class StudentModel(Base):
    """Data model for "students" table"""

    __tablename__ = "students"
    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR)
    email = Column(VARCHAR)
    address_id = Column(ForeignKey("addresses.address_id"))
    course_id = Column(ForeignKey("courses.id"))
    address = relationship("AddressModel", back_populates="student")
    course = relationship("CourseModel", back_populates="student")

    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, email: {self.email}, address_id: {self.address_id}, address: {self.address}, course: {self.course}"


class CourseModel(Base):
    """Data model for "courses" table"""

    __tablename__ = "courses"
    id = Column(INTEGER, primary_key=True)
    course_name = Column(VARCHAR)
    start_date = Column(VARCHAR)
    end_date = Column(VARCHAR)
    student = relationship("StudentModel", back_populates="course")

    def __repr__(self):
        return (
            f"id: {self.id}, course_name: {self.course_name}, start_date: {self.start_date},"
            f" end_date: {self.end_date}"
        )
