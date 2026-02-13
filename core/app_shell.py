# core/app_shell.py
from PyQt5.QtWidgets import QStackedWidget
from ui.login_view import LoginView
from ui.admin_view import AdminView
from ui.student_view import StudentView
from ui.teacher_view import TeacherView
from services.auth_service import AuthService
from presenters.login_presenter import LoginPresenter

class AppShell(QStackedWidget):
    LOGIN = 0
    ADMIN = 1
    STUDENT = 2
    TEACHER = 3

    def __init__(self):
        super().__init__()

        self.login_view = LoginView()
        self.admin_view = AdminView()
        self.student_view = StudentView()
        self.teacher_view = TeacherView()

        self.auth_service = AuthService()
        
        self.login_presenter = LoginPresenter(
            view=self.login_view,
            auth=self.auth_service,
            on_success=self._go_view
        )
        self.addWidget(self.login_view)
        self.addWidget(self.admin_view)
        self.addWidget(self.student_view)
        self.addWidget(self.teacher_view)
        

        self.setCurrentIndex(self.LOGIN)
        
        self.setWindowTitle("PyQt5 - MVP")
        self.resize(640, 400)

    def _go_view(self, username: str, role):

        if role == "admin":
            self.admin_view.set_welcome(username)
            self.setCurrentIndex(self.ADMIN)
        
        if role == "student":
            self.admin_view.set_welcome(username)
            self.setCurrentIndex(self.STUDENT)
        
        if role == "teacher":
            self.admin_view.set_welcome(username)
            self.setCurrentIndex(self.TEACHER)
        
        
        