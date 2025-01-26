class ParentEntity:
    def __init__(
        self,
        first_name,
        last_name,
        phone_number,
        email,
        relationship,
        profile_img,
        usuario,
    
    
    ):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__phone_number = phone_number
        self.__email = email
        self.__relationship = relationship
        self.__profile_img = profile_img
        self.__usuario = usuario

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
    def relationship(self):
        return self.__relationship

    @relationship.setter
    def relationship(self, relationship):
        self.__relationship = relationship

    @property
    def profile_img(self):
        return self.__profile_img

    @profile_img.setter
    def profile_img(self, profile_img):
        self.__profile_img = profile_img

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

  
