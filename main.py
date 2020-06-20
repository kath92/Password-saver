import pickle
from password_saver import *
from getpass import getpass


def save_to_bin(source, password):
    with open("passwords.bin", "rb") as file:
        data = pickle.load(file)
    with open("passwords.bin", 'wb') as file:
        if not is_duplicate(source, data):
            data.append({source: password})
            pickle.dump(data, file)
            print("Successfully added the entry!")


def is_duplicate(key, data):
    for dictionary in data:
        if key in dictionary:
            print("The source already exists!")
            return True


def retrieve_from_bin(source):
    with open("passwords.bin", "rb") as file:
        data = pickle.load(file)
        for dictionary in data:
            if source in dictionary:
                return dictionary[source]
        print(f"Retrieving the password for {source}...")


def encode_user_input():
    source = input("Enter source: ")
    password = input("Enter password: ")
    user_key = getpass("Enter user_key: ")
    save_to_bin(source, encode(password, user_key))
    return "Password was saved!"


def decode_user_input():
    source = input("Enter source name: ")
    user_key = getpass("Enter user_key: ")
    password = retrieve_from_bin(source)
    if password:
        return decode(password, user_key)
    return "Key doesn't exist!"


def main():
    while True:
        user_input = input("Press 'g' to get a password, 's' to save one or 'q' to quit: ")
        if user_input == "g":
            print(decode_user_input())
        elif user_input == "s":
            print(encode_user_input())
        elif user_input == "q":
            print("Quitting the program.")
            break
        else:
            print("Invalid input")
            continue
            

if __name__ == '__main__':
    main()
