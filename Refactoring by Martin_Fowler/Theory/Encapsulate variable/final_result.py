default_owner = {'first_name': 'John', 'last_name': 'Smith'}


def get_default_owner():
    return default_owner


spaceship = {'owner': get_default_owner()}


# Creating a setter
def set_default_owner(owner):
    global default_owner
    default_owner = owner


default_owner = {'first_name': 'Jane', 'last_name': 'Smith'}
