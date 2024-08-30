from pydantic import BaseModel

class CadastroUsuario(BaseModel):
    nome: str
    telefone: str
    endereco: str
    email: str
    senha: str


class UsuarioResponse(BaseModel):
    id: int
    nome: str
    telefone: str
    endereco: str
    email: str


class UsuarioResponseToken(BaseModel):
    id: int
    nome: str
    telefone: str
    endereco: str
    email: str
    token: dict
