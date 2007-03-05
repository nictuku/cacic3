from turbogears.identity.saprovider import *
from sqlalchemy import select, func
from model import usuarios

db = usuarios.table.engine

class CacicIdentityProvider(SqlAlchemyIdentityProvider):
    def __init__(self):
        super(CacicIdentityProvider, self).__init__()

    def validate_password(self, user, user_name, password):
        encrypted_password = select ([func.PASSWORD(password)], engine=db).execute ().fetchone ()[0]
        return user.password == encrypted_password

