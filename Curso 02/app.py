from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_mexicano = Restaurante('mexicano Food', 'mexicano')
restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_japones.alternar_estado()
restaurante_japones.receber_avaliacao('Gui', 10)
restaurante_japones.receber_avaliacao('Mãe', 9)
restaurante_japones.receber_avaliacao('Pai', 9)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()