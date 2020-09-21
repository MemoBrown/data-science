
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print('Ando caminando')


class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print('Ando moviendome en mi bicicleta')

def main():
    persona = Persona('Guillermo')
    persona.avanza()

    ciclista = Ciclista('Gaby')
    ciclista.avanza()

if __name__ == "__main__":
    main()