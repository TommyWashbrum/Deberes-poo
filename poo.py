class Persona:
    def __init__(self, nombre, genero, edad, direccion):
        self._nombre = nombre
        self._genero = genero
        self._edad = edad
        self._direccion = direccion

    # Encapsulamiento de nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    # Encapsulamiento de genero
    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, value):
        self._genero = value

    # Encapsulamiento de edad
    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, value):
        self._edad = value

    # Encapsulamiento de direccion
    @property
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, value):
        self._direccion = value

    # Representación en cadena de texto
    def __str__(self):
        return f'Nombre: {self.nombre}, Género: {self.genero}, Edad: {self.edad}, Dirección: {self.direccion}'

# Ejemplo de uso
persona = Persona('Jose Antonio', 'Masculino', 30, 'Urdesa central')
print(persona)


class Empleado:
    def __init__(self, id_empleado, sueldo):
        self._id_empleado = id_empleado
        self._sueldo = sueldo

    @property
    def id_empleado(self):
        return self._id_empleado

    @id_empleado.setter
    def id_empleado(self, value):
        if isinstance(value, int) and value > 0:
            self._id_empleado = value
        else:
            raise ValueError("El ID del empleado debe ser un entero positivo.")

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self._sueldo = value
        else:
            raise ValueError("El sueldo debe ser un número positivo o cero.")

    def __str__(self):
        return f"Empleado[ID: {self._id_empleado}, Sueldo: {self._sueldo}]"

# Ejemplo de uso:
empleado = Empleado(1, 2500)
print(empleado)


class Cliente:
    def __init__(self, id_cliente, email):
        self._id_cliente = id_cliente
        self._email = email

    @property
    def id_cliente(self):
        return self._id_cliente

    @id_cliente.setter
    def id_cliente(self, value):
        if isinstance(value, int) and value > 0:
            self._id_cliente = value
        else:
            raise ValueError("El ID del cliente debe ser un entero positivo.")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if isinstance(value, str) and '@' in value:
            self._email = value
        else:
            raise ValueError("El email debe ser una dirección de correo válida.")

    def __str__(self):
        return f"Cliente[ID: {self._id_cliente}, Email: {self._email}]"

# Ejemplo de uso:
cliente = Cliente(789, 'cliente1@gmail.ec')
print(cliente)