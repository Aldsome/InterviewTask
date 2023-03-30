from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
users = []

    # check if the id parameter is provided and include the user with that id
    if 'id' in args:
        for user in USERS:
            if user['id'] == args['id']:
                users.append(user)
                return users

    for user in USERS:
        # check if the name parameter is provided and partially matched
        if 'name' in args and args['name'].lower() in user['name'].lower():
            users.append(user)
            continue
        
        # check if the age parameter is provided and matched with the range of age - 1 to age + 1
        if 'age' in args and int(args['age'])-1 <= user['age'] <= int(args['age'])+1:
            users.append(user)
            continue
        
        # check if the occupation parameter is provided and partially matched
        if 'occupation' in args and args['occupation'].lower() in user['occupation'].lower():
            users.append(user)

    # remove duplicates from the users list
    users = list({user['id']: user for user in users}.values())

    return USERS
