class Autenticacao:

    def __init__(self):
        self.usuarios = {}

    def cadastrar_usuario(self, usuario, senha):
        self.usuarios[usuario] = senha

    def login(self, usuario, senha):
        return self.usuarios.get(usuario) == senha
  
class Autenticacao:

    def __init__(self):
        self.usuarios = {}

    def cadastrar_usuario(self, usuario, senha):

        if usuario in self.usuarios:
            raise ValueError("Usuário já existe")

        self.usuarios[usuario] = senha

    def login(self, usuario, senha):
        return self.usuarios.get(usuario) == senha  
    

class Autenticacao:

    def __init__(self):
        self.usuarios = {}

    def cadastrar_usuario(self, usuario, senha):

        if usuario in self.usuarios:
            raise ValueError("Usuário já existe")

        if len(senha) < 6:
            raise ValueError("Senha inválida")

        self.usuarios[usuario] = senha

    def login(self, usuario, senha):
        return self.usuarios.get(usuario) == senha
    

class Autenticacao:

    def __init__(self):
        self.usuarios = {}

    def cadastrar_usuario(self, usuario, senha):

        if usuario in self.usuarios:
            raise ValueError("Usuário já existe")

        if len(senha) < 6:
            raise ValueError("Senha deve possuir no mínimo 6 caracteres")

        self.usuarios[usuario] = senha

    def login(self, usuario, senha):
        return self.usuarios.get(usuario) == senha

    def redefinir_senha(self, usuario, nova_senha):

        if usuario not in self.usuarios:
            raise ValueError("Usuário não encontrado")

        if len(nova_senha) < 6:
            raise ValueError("Senha inválida")

        self.usuarios[usuario] = nova_senha