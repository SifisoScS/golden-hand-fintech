from flask_login import LoginManager

login_manager = LoginManager()

class GoldenHandUserContext:
    def __init__(self, user_id, roles, permissions, session_id, metadata=None):
        self.user_id = user_id
        self.roles = roles or []
        self.permissions = permissions or []
        self.session_id = session_id
        self.metadata = metadata or {}