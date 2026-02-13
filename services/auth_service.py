# services/auth_service.py
from dataclasses import dataclass

@dataclass(frozen=True)
class AuthResult:
    ok: bool
    message: str = ""
    role: str = ""

class AuthService:
    """
    Servicio de autenticación. Hoy: validación estática.
    Mañana: cambiar por BD/API.
    """
    def login(self, username, password):

        if username == "" or password == "":
            return AuthResult(False, "Campos vacíos", "")

        if username == "admin" and password == "1234":
            return AuthResult(True, "Login correcto", "admin")

        if username == "student" and password == "1111":
            return AuthResult(True, "Login correcto", "student")

        if username == "teacher" and password == "2222":
            return AuthResult(True, "Login correcto", "teacher")

        return AuthResult(False, "Usuario o contraseña incorrectos", "")