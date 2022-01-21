import json
import sys
import argparse


def create_file():
    file = open("users.json", 'w')
    file.write(json.dumps([]))
    file.close()
    return open("users.json", 'r')


def create_user(users):
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help="username", required=True)
    parser.add_argument("-e", "--email", help="email", required=True)
    parser.add_argument("-s", "--status", help="status", required=True)
    args = parser.parse_args()

    try:
        users['username'] = args.username
        users['email'] = args.email
        users['status'] = args.status
    except IndexError:
        raise Exception('wrong data')


def check_user_exists(users_data, user):
    for users in users_data:
        if user['username'] == users['username'] or \
                user['email'] == users['email']:
            return True

    return False


def add_user(user):
    # reading from file, if not exists then create
    try:
        read_file = open('users.json', 'r')
    except FileNotFoundError:
        read_file = create_file()
    finally:
        pass

    # loading data from json file
    try:
        users_data = json.loads(read_file.read())
    except ValueError:
        with open('users.json', "w") as write_to_file:
            write_to_file.write(json.dumps([]))
        users_data = []
    finally:
        pass

    read_file.close()

    # check whether user already exists. If no then add new user
    if not check_user_exists(users_data, user):
        users_data.append(user)
        with open('users.json', 'w') as write_to_file:
            write_to_file.write(json.dumps(users_data, indent=4, sort_keys=True))
    else:
        raise ("User with username {user['username']} or"
               " email {user['email']} already exist!")


if __name__ == "__main__":
    new_user = {}
    create_user(new_user)
    add_user(new_user)
