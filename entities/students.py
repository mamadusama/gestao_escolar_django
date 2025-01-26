class StudentEntity:
    def __init__(
        self,
        usuario,
        first_name,
        last_name,
        date_of_birth,
        gender,
        nationality,
        phone_number,
        email,
        address,
        city,
        neighborhood,
        postal_code,
        profile_img,
        parent,
        is_active=True,
        
        

    ):
        self.__usuario= usuario
        self.__parent = parent
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__gender = gender
        self.__nationality = nationality
        self.__phone_number = phone_number
        self.__email = email
        self.__address = address
        self.__city = city
        self.__neighborhood = neighborhood
        self.__postal_code = postal_code
        self.__profile_img = profile_img
        self.__is_active = is_active

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, parent):
        self.__parent = parent

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.__gender = gender

    @property
    def nationality(self):
        return self.__nationality

    @nationality.setter
    def nationality(self, nationality):
        self.__nationality = nationality

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        self.__phone_number = phone_number

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = city

    @property
    def neighborhood(self):
        return self.__neighborhood

    @neighborhood.setter
    def neighborhood(self, neighborhood):
        self.__neighborhood = neighborhood

    @property
    def postal_code(self):
        return self.__postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        self.__postal_code = postal_code


    @property
    def profile_img(self):
        return self.__profile_img

    @profile_img.setter
    def profile_img(self, profile_img):
        self.__profile_img = profile_img

    @property
    def is_active(self):
        return self.__is_active

    @is_active.setter
    def is_active(self, is_active):
        self.__is_active = is_active




"""     @property
    def student_number(self):
        return self.__student_number

    @student_number.setter
    def student_number(self, student_number):
        self.__student_number = student_number 
"""