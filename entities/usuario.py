class UserEntity:
    def __init__(
        self, nome_usuario, email, password, is_staff=False, is_active=True, cargo=None
    ):
        self.__nome_usuario = nome_usuario
        self.__email = email
        self.__password = password
        self.__is_staff = is_staff
        self.__is_active = is_active
        self.__cargo = cargo

    @property
    def nome_usuario(self):
        return self.__nome_usuario

    @property
    def email(self):
        return self.__email

    @property
    def password(self):
        return self.__password

    @property
    def is_staff(self):
        return self.__is_staff

    @property
    def is_active(self):
        return self.__is_active

    @property
    def cargo(self):
        return self.__cargo
