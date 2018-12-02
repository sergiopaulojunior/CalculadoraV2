import operacoes as op


def menuRelatorios():
    print('-------------------------------')
    print('----- MENU DE RELATORIOS ------')
    print('-------------------------------')
    print('----- [1] RELATORIO SOMA ------')
    print('--- [2] RELATORIO SUBTRACAO ---')
    print('[3] RELATORIOS DE MULTIPLICACAO')
    print('-- [4] RELATORIOS DE DIVISAO --')
    print('-------- [5] RETORNAR ---------')
    opc = input('\n''Entre com a opcao desejada: ')
    if opc.isdigit():
        if int(opc) == 1:
            op.relatorioSoma()
            x = input('Pressione [1] para tetornar ou [2] para MENU: ')
            if x.isdigit():
                if int(x) == 1:
                    menuRelatorios()
                elif int(x) == 2:
                    menu()
                else:
                    print('Opcao invalida você sera redirecionado ao menu principal ! ''\n')
                    menu()
            else:
                print('Opcao invalida você sera redirecionado para o menu pricipal !' '\n')
                menu()
        elif int(opc) == 2:
            op.relatorioSubtriar()
            x = input('Pressione [1] para retornar ou [2] para MENU: ')
            if x.isdigit():
                if int(x) == 1:
                    menuRelatorios()
                elif int(x) == 2:
                    menu()
                else:
                    print('Opcao invalida você sera redirecionado para o menu principal ! ''\n')
                    menu()
            else:
                print('Opcao invalida você sera redirecionado para o menu principal ! ''\n')
                menu()
        elif int(opc) == 3:
            op.relatorioMultiplicar()
            x = input('Pressione [1] para retornar ou [2] para MENU: ')
            if x.isdigit():
                if int(x) == 1:
                    menuRelatorios()
                elif int(x) == 2:
                    menu()
                else:
                    print('Opcao invalida você sera redirecionado para o menu principal ! ''\n')
                    menu()
            else:
                print('Opcao invalida você sera redirecionado para o menu principal ! ''\n')
                menu()
        elif int(opc) == 4:
            op.relatorioDividir()
            x = input('Pressione [1] para retornar ou [2] para MENU: ')
            if x.isdigit():
                if int(x) == 1:
                    menuRelatorios()
                elif int(x) == 2:
                    menu()
                else:
                    print('Opcao invalida você sera redirecionado para o menu principal ! ''\n')
                    menu()
            else:
                print('Opcao invalida você sera redirecionado para o menu principal ! ''\n')
                menu()
        elif int(opc) == 5:
            menu()
        else:
            print('Opcao invalida')
            menuRelatorios()
    else:
        print('Opcao invalida')
        menuRelatorios()

def menu():
    print('--------------------')
    print('- CALCULADORA MENU -')
    print('--------------------')
    print('---- [1] SOMAR -----')
    print('--- [2] SUBTRAIR ---')
    print('- [3] MULTIPLICAR --')
    print('--- [4] DIVIDIR ----')
    print('-- [5] RELATORIOS --')
    print('\n')
    opc = input('Entre com a opcao desejada: ')
    if opc.isdigit():
        if int(opc) == 1:
            print('\n''Você entrou na função SOMA''\n')
            x = input('Entre com o primeiro valor: ')
            if x.isdigit():
                y = input('Entre com o segundo valor: ')
                if y.isdigit():
                    op.soma(int(x), int(y))
                    print('\n''Operacao realizada com sucesso', '\n')
                    menu()
                else:
                    print('Entre com um valor numerico''\n')
                    menu()
            else:
                print('Entre com um valor numerico''\n')
                menu()
        elif int(opc) == 2:
            print('\n''Você entrou na função SUBTRAIR''\n')
            x = input('Entre com o primeiro valor: ')
            if x.isdigit():
                y = input('Entre com o segundo valor: ')
                if y.isdigit():
                    op.subtrair(int(x), int(y))
                    print('\n''Operacao realizada com sucesso', '\n')
                    menu()
                else:
                    print('Entre com um valor numerico''\n')
                    menu()
            else:
                print('Entre com um valor numerico''\n')
                menu()
        elif int(opc) == 3:
            print('\n''Você entrou na função MULTIPLICAR''\n')
            x = input('Entre com o primeiro valor: ')
            if x.isdigit():
                y = input('Entre com o segundo valor: ')
                if y.isdigit():
                    op.multiplicar(int(x), int(y))
                    print('\n''Operacao realizada com sucesso', '\n')
                    menu()
                else:
                    print('Entre com um valor numerico''\n')
                    menu()
            else:
                print('Entre com um valor numerico''\n')
                menu()
        elif int(opc) == 4:
            print('\n''Você entrou na função DIVIDIR''\n')
            x = input('Entre com o primeiro valor: ')
            if x.isdigit():
                y = input('Entre com o segundo valor: ')
                if y.isdigit():
                    if int(y) > 0:
                        op.dividir(int(x), int(y))
                        print('\n''Operacao realizada com sucesso', '\n')
                        menu()
                    else:
                        print('\n''Não é possivel realizar divizão por 0', '\n')
                        menu()
                else:
                    print('Entre com um valor numerico''\n')
                    menu()
            else:
                print('Entre com um valor numerico''\n')
                menu()
        elif int(opc) == 5:
            menuRelatorios()
        else:
            print('Valor invalido')
            menu()
    else:
        print('Entre com um valor numerico')
        menu()


menu()


