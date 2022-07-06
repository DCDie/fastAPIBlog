import databases
import orm

database = databases.Database("sqlite:///db")
models = orm.ModelRegistry(database=database)


class User(orm.Model):
    tablename = "users"
    registry = models
    fields = {
        "id": orm.Integer(primary_key=True, allow_null=True),
        "username": orm.Email(max_length=25),
        "email": orm.Email(max_length=25),
        "password": orm.String(max_length=256)
    }
