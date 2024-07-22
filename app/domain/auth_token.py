class AuthToken:
    def __init__(self, token: str):
        if not token:
            raise ValueError("トークンないよ")
        self.token = token
    
    def __str__(self):
        return self.token