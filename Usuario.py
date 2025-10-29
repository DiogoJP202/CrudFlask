class Usuario:
    _contador = 0

    def __init__(self, nome, email):
        Usuario._contador += 1
        self._id = Usuario._contador
        self.nome = nome
        self.email = email

    def to_dict(self):
        return {"id": self._id, "nome": self.nome, "email": self.email}
