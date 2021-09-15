#todo anotações
#1
#usar tabela da evelyn
#2
#pesquisar tutorial no yt
#ter loop principal e classes nesse arquivo e metodos em outro(por enquando)
#3
#primeira informação lida sera se é funcionario ou não
#caso for funcionario criar tanto a classe de cliente como funcionario
#4
#ler informações la
#ter forma de acessar a area de administrador por ela
#ter como apagar seu cadastro por ela
#5
#usar for com o clientes para verificar
#6
#a pensar
#7
#nescessita do sistema de excluir cadastros... para mudar informações
#8
#criar sistema de read no arquivo e armazenar cada linha em uma lista
#excluir o login requisitado pelo indice dele nos cadastros
#ter verificação para saber se não é um cadastro novo
#excluir da lista de cadastros
#dar write no texto msm
#9
#fazer engenharia reversa no metodo de armazernar
#imports
#todo outras ideias
#poder mudar informações pela area de cadastrado
#explicar to-do codigo pra raissa pra ela poder entender tudin
#mudar a senha de verdade no esqueci minha senha
import time as t
import datetime as dt


# classe - armazena e printa o nome senha e cpf de um usuario
class Usuario:
    # construtor
    # coloca argumentos que você vai usar pra criar(instanciar a classe) a classe
    def __init__(self, fNome, fDtNasc, fEmail, fTelefone, fSenha, fCpf,funcionario = False,hasChanged = False):
        self.hasChanged = hasChanged
        self.funcionario = funcionario
        # variaveis
        # pode ser qualquer coisa
        self.email = ""
        # deve ser um numero com 10 ou 11 caracteres
        self.hasTel = False
        self.tel = 0
        if fTelefone != "":
            self.hasTel = True
            self.tel = int(fTelefone)
        self.email = fEmail
        # pode ser qualquer coisa
        self.nome = fNome
        # deve ter entre 8 e 16 caracteres
        self.senha = fSenha
        # deve ter 11 caracteres numericos
        self.cpf = int(fCpf)
        yyyy = int(fDtNasc[4:8])
        mm = int(fDtNasc[2:4])
        dd = int(fDtNasc[0:2])
        # consiste da data atual formatada para o usuario
        self.dtNasc = fDtNasc
        self.prtDtNasc = f"{dd}/{mm}/{yyyy}"
        today = dt.date.today()
        # datetime do aniversario
        self.dtn = dt.date(yyyy, mm, dd)
        # idade
        self.age = today.year - self.dtn.year - ((today.month, today.day) < (self.dtn.month, self.dtn.day))

    def primeroNome(self):
        nomeList = self.nome.split()
        return nomeList[0]

    def ultimoNome(self):
        nomeList = self.nome.split()
        return nomeList[-1]

    def printUsuario(self, nUsuario = -1):
        if nUsuario == -1:
            print(f"informações de {self.primeroNome()}")
        else:
            print("informações do usuario {}:".format(nUsuario + 1))
        # chamo as variaveis da classe
        # uso as do metodo self pois as outras so existem dentro do construtor
        print("nome: {}\ndata de nascimento: {}".format(self.nome, self.dtNasc, ))
        if self.hasTel:
            print("telefone: {}".format(self.tel))
        if self.email != "":
            print("email: {}".format(self.email))
        print("senha: {}\ncpf: {}".format(self.senha, self.cpf))
        t.sleep(0.5)

class Empregado(Usuario):
    def __init__(self, cargo, dataDeContratacao, Salario, fNome, fDtNasc, fEmail, fTelefone, fSenha, fCpf):
        super().__init__(fNome, fDtNasc, fEmail, fTelefone, fSenha, fCpf)
        self.cargo = cargo
        self.salario = int(Salario)
        self.dtDC = dataDeContratacao
        yyyy = int(dataDeContratacao[4:8])
        mm = int(dataDeContratacao[2:4])
        dd = int(dataDeContratacao[0:2])
        ddc = dt.date(yyyy, mm, dd)
        self.ddc = ddc
    def salarioComImposto(self,taxaInss):
        pass
        #todo metodo que cacula o salario com imposto
#variaveis inicias
# armazenar os objetos de uma determinada classe
# todos os cadastros criados
cadastros = []
# cadastros que devem ser armazenados
cadastrosNovos = []
#cadastros de funcionarios
cadastrosFunc = []
#armazena os cargos possiveis
cargos = ["adm","caixista"]
# armazena as classes criadas
#todo levar para outro arquivo os metodos


def armazenar():
    with open("e:\supermercado.txt", "w") as arq:
        adicionar = ""
        for a in range(len(textoList)):
            adicionar += textoList[a] + "\n"
        for a in range(len(cadastrosNovos)):
            if cadastrosNovos[a].funcionario:
                for b in range(len(cadastrosFunc)):
                    if cadastrosNovos[a].nome == cadastrosFunc[b].nome:
                        break
                userInfo = str(cadastrosNovos[a].funcionario)
                userInfo += ";" + cadastrosNovos[a].nome
                userInfo += "," + str(cadastrosNovos[a].dtNasc)
                userInfo += "," + cadastrosNovos[a].email
                if cadastrosNovos[a].tel != 0:
                    userInfo += "," + str(cadastrosNovos[a].tel)
                else:
                    userInfo += ","
                userInfo += "," + cadastrosNovos[a].senha
                userInfo += "," + str(cadastrosNovos[a].cpf)
                userInfo += "," + str(cadastrosFunc[b].salario)
                userInfo += "," + cadastrosFunc[b].cargo
                userInfo += "," + cadastrosFunc[b].dtDC
                print(userInfo)
                adicionar += userInfo
            else:
                userInfo = str(cadastrosNovos[a].funcionario)
                userInfo += "," + cadastrosNovos[a].nome
                userInfo += "," + str(cadastrosNovos[a].dtNasc)
                userInfo += "," + cadastrosNovos[a].email
                if cadastrosNovos[a].tel != 0:
                    userInfo += "," + str(cadastrosNovos[a].tel)
                else:
                    userInfo += ","
                userInfo += "," + cadastrosNovos[a].senha
                userInfo += "," + str(cadastrosNovos[a].cpf)
                adicionar += userInfo
        arq.write(adicionar)


def area_cadastrado(a):
    while True:
        # todo criar algo na area cadastrada
        pass
        ###ideias###
        # entrar na area de funcionario
        # criar formas de pagamento (deve ser possivel colocar mais que uma)
        if cadastros[a].funcionario:
            acaoCadastrado = input(f"bem vindo {cadastros[a].nome}\n o que você deseja fazer?\ni = ver minhas informações\ns-sair\n")

            if acaoCadastrado.lower() == "s":
                print("adeus")
                break
            elif acaoCadastrado.lower() == "i":
                cadastros[a].printUsuario()
            else:
                print("digite uma opção valida")
        else:
            acaoCadastrado = input(
                f"bem vindo {cadastros[a].nome}\n o que você deseja fazer?\ni = ver minhas informações\ns-sair\n")

            if acaoCadastrado.lower() == "s":
                print("adeus")
                break
            elif acaoCadastrado.lower() == "i":
                cadastros[a].printUsuario()
            else:
                print("digite uma opção valida")


def processoCad():
    while True:
        nome = ""
        while nome == "":
            nome = input("digite seu nome\n")
        t.sleep(0.1)
        while True:
            dtNasc = input("digite sua data de nascimento\n")
            if dtNasc == "":
                pass
            elif len(dtNasc) != 8:
                print("a data de nascimento deve ter 8 digitos seguindo o padrão ddmmaaaa")
            elif not dtNasc.isnumeric():
                print("a data deve ser numerica")
            else:
                break
        t.sleep(0.1)
        while True:

            email = input(
                "coloque um email ou um telefone\ndigite um email\ncaso não queira colocar um email aperte enter\n")
            t.sleep(0.1)
            while True:
                telefone = input("digite um telefone\ncaso não queira colocar um telefone aperte enter\n")
                t.sleep(0.1)
                if telefone == "":
                    break
                elif not telefone.isnumeric():
                    print("o telefone deve ser composto apenas de numeros ")
                elif len(telefone) > 11 or len(telefone) < 10:
                    print("o telefone deve ter entre 11 e 10 numeros")
                else:
                    break
            if email == "" and telefone == "":
                print("voce deve inserir ou um telefone ou um email")
            else:
                break
        while True:
            while True:
                senha = input("digite sua senha\n")
                if senha == "":
                    pass
                elif len(senha) > 16 or len(senha) < 8:
                    print("a senha deve ter entre 8 e 16 caracteres")
                else:
                    break
            t.sleep(0.1)
            senhaV = input("confirme a sua senha\n")
            t.sleep(0.1)
            if senhaV == senha:
                break
        while True:
            cpf = input("digite seu cpf\n")
            if cpf == "":
                pass
            elif not cpf.isnumeric():
                print("o cpf deve conter apenas numeros")
            elif len(cpf) != 11:
                print("digite o cpf apenas com 11 numeros")
            else:
                break
        t.sleep(0.1)
        #todo verificar se existem outros com o mesmo: nome, email e telefone
        conf = input("confirma essas informações?\ns=sim\nn=não\n")
        if conf.lower() == "s":
            print("cadastro feito com sucesso")
            novoCadastro = Usuario(nome, dtNasc, email, telefone, senha, cpf)
            cadastros.append(novoCadastro)
            cadastrosNovos.append(novoCadastro)
            break
        else:
            print("informações deletadas")
            cont = input("deseja fazer o cadastro novamente?\ns= sim\nqlqr outra coisa = não\n")
            if cont.lower() == "s":
                pass
            else:
                break


def entrar():
    Break = False
    while True:
        if Break:
            Break = False
            break
        usuario = input("digite seu nome")
        senha = input("digite sua senha")
        entrou = False
        for a in range(len(cadastros)):
            if cadastros[a].nome == usuario and cadastros[a].senha == senha:
                area_cadastrado(a)
                entrou = True
        if not entrou:
            while True:
                Break = False
                erro = input(
                    "nenhum cadastro encontrado\nvoce deseja:\nt = tentar novamente\ne = esqueci minha senha\nc = criar um cadastro\ns = sair para o menu principal\n")
                if erro.lower() == "t":
                    break
                elif erro.lower() == "e":
                    # todo adicionar passos a mais quando a conta for de funcionario
                    while True:
                        ET = input("você deseja usar o email ou o telefone?\nt = telefone\ne = email\ns = sair do esqueci minha senha")
                        if ET.lower() == "t":
                            while True:
                                entrouT = False
                                telefone = input("digite o telefone\n")
                                for a in range(len(cadastros)):
                                    if cadastros[a].tel == telefone:
                                        while True:
                                            #todo mudar a senha
                                            novaSenha = input("digite uma nova senha para essa conta")
                                            senhaRep = input("repita a senha")
                                            if novaSenha == senhaRep:
                                                print("nova senha cadastrada com sucesso\n obs: essa senha apenas vai contar para um cadastro")
                                                break
                                            else:
                                                print("as senhas não confizem")
                                        cadastros[a].senha = novaSenha
                                        entrouT = True
                                if entrouT:
                                    break
                                else:
                                    Break = False
                                    while True:
                                        cont =input("nenhum cadastro com esse telefone\ndeseja entrar novamente\ns=sim\nn=não")
                                        if cont.lower() == "s":
                                            break
                                        elif cont.lower() == "n":
                                            Break = True
                                            break
                                        else:
                                            print("digite uma alternativa correta")
                                    if Break:
                                        Break = False
                                        break
                            break
                        elif ET.lower() == "e":
                            while True:
                                entrouE = False
                                email = input("digite o email\n")
                                for a in range(len(cadastros)):
                                    if cadastros[a].email == email:
                                        while True:
                                            novaSenha = input("digite uma nova senha para essa conta")
                                            senhaRep = input("repita a senha")
                                            if novaSenha == senhaRep:
                                                print("nova senha cadastrada com sucesso")
                                                break
                                            else:
                                                print("as senhas não confizem")
                                        cadastros[a].senha = novaSenha
                                        entrouE = True
                                if entrouE:
                                    break
                                else:
                                    Break = False
                                    while True:
                                        cont = input(
                                            "nenhum cadastro com esse email\ndeseja tentar novamente\ns=sim\nn=não")
                                        if cont.lower() == "s":
                                            break
                                        elif cont.lower() == "n":
                                            Break = True
                                            break
                                        else:
                                            print("digite uma alternativa correta")
                                    if Break:
                                        Break = False
                                        break
                        elif ET.lower() == "s":
                            break
                        else:
                            print("digite uma opção valida")
                        if Break:
                            Break = False
                            break
                elif erro.lower() == "c":
                    processoCad()
                    print("agora você pode entrar na sua conta")
                    break
                elif erro.lower() == "s":
                    Break = True
                    break
                else:
                    print("digite uma opção valida")
        else:
            break


def area_adm():
    print("logado como administrador como sucesso")
    while True:
        acaoAdm = input("o que você deseja fazer?\nm = mostrar cadastros\nc = dar cargos a algum funcionario\ns = sair do modo administrador")
        if acaoAdm.lower() == "m":
            if len(cadastros) != 0:
                for a in range(len(cadastros)):
                    # chamo a função dessa classe
                    # argumentos da função
                    cadastros[a].printUsuario(a)
            else:
                print("não ha cadastros")
        elif acaoAdm.lower() == "c":
            while True:
                cadN = 0
                funcN = 0
                entrouP = False
                pessoa = input("coloque o nome da pessoa que você quer dar um cargo\n")
                for a in range(len(cadastros)):
                    if pessoa == cadastros[a].nome:
                        entrouP = True
                        cadN = a
                        break
                if entrouP:
                    for b in range(len(cadastrosFunc)):
                        if cadastrosFunc[b].nome == pessoa:
                            funcN = b
                            break

                    while True:
                        cargo = input("selecione o cargo que você quer dar para a pessoa\n")
                        if cargo.lower() == "caixista" or cargo.lower() == "adm":
                            break
                        else:
                            print("digite um cargo valido")
                    while True:
                        novSal = input("digite o novo salario")
                        if novSal.isnumeric():
                            break
                        else:
                            print("digite um salario numerico")
                    if funcN == 0:
                        while True:
                            diaCont = input("qual o dia da contratação?\n")
                            cadastros[cadN].funcionario = True
                            if len(diaCont) >= 8:
                                if diaCont.isnumeric():
                                    break
                                else:
                                    print("deve apenas ter numeros")
                            else:
                                print("a data deve ter 8 digitos")
                    else:
                        cadastrosFunc[funcN].cargo = cargo
                        cadastrosFunc[funcN].salario = novSal
                    #todo permitir apenas inputs desejados
                    print()
                    novo_f = Empregado(cargo,diaCont,novSal,cadastros[cadN].nome,cadastros[cadN].dtNasc,cadastros[cadN].email,cadastros[cadN].tel,cadastros[cadN].senha,cadastros[cadN].cpf)
                    novo_n = Usuario(cadastros[cadN].nome,cadastros[cadN].dtNasc,cadastros[cadN].email,cadastros[cadN].tel,cadastros[cadN].senha,cadastros[cadN].cpf,funcionario = True)
                    cadastrosFunc.append(novo_f)
                    cadastrosNovos.append(novo_n)
                    print("funcionario atualizado com exito")
                    break
                else:
                    print("nenhuma pessoa com esse nome")
        elif acaoAdm.lower() == "s":
            print("saindo do modo administrador")
            break
        else:
            print("digite corretamente")

# armazena e cria objetos da classe Usuario no cadastros[] os cadastros armazenados no banco de dados
textoList = []
with open("e:\supermercado.txt", "r") as arq:
    textoList = arq.readlines()
    for a in range(len(textoList)):
        textoAdicionado = textoList[a].split(",")
        if textoAdicionado[0] == "0":
            cadastroRegistrado = Usuario(textoAdicionado[1], textoAdicionado[2], textoAdicionado[3], textoAdicionado[4],
                                         textoAdicionado[5], textoAdicionado[6])
            cadastros.append(cadastroRegistrado)
        else:
            cadastroRegistrado = Usuario(textoAdicionado[1], textoAdicionado[2], textoAdicionado[3], textoAdicionado[4],textoAdicionado[5], textoAdicionado[6])
            cadastros.append(cadastroRegistrado)
            cadastroRegistrado = Empregado(textoAdicionado[1],textoAdicionado[7],textoAdicionado[8],textoAdicionado[9], textoAdicionado[2], textoAdicionado[3], textoAdicionado[4],textoAdicionado[5], textoAdicionado[6])
            cadastrosFunc.append(cadastroRegistrado)
#loop principal
while True:
    iniciarCad = input(
        "você deseja entrar em uma conta ou cadastrar uma conta\nc = cadastrar\ne = entrar\na = entrar como admin\ns = fechar o progama\n")
    if iniciarCad.lower() == "a":
        user = input("digite o usuario do administrador")
        senha = input("digite a senha do administrador")
        if user == "admin" and senha == "admin":
            area_adm()
    elif iniciarCad.lower() == "c":
        processoCad()
    elif iniciarCad.lower() == "e":
        entrar()
    elif iniciarCad.lower() == "s":
        print("adeus")
        armazenar()
        break
    else:
        print("digite uma alternativa valida")
#todo se livrar de while True e break