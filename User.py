import datetime


class UserDate:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        self.file = open(self.filename, "r")
        self.users = {}

        for line in self.file:
            username, passowrd, email, created = line.strip().split(",")
            self.users[username] = (passowrd, email, created)

        self.file.close()

    def get_user(self, username):
        if username in self.users:
            return self.users[username]
        else:
            return -1

    def get_password(self, username):
        if username in self.users:
            return self.users[username][0]
        else:
            return -1

    def get_email(self, username):
        if username in self.users:
            return self.users[username][1]
        else:
            return -1

    def find_password(self, username, email):
        if self.get_user(username) !=-1:
            if self.users[username][1] == email:
                return self.get_password(username)
            else:
                return False
        else:
            return False

    def add_user(self, username, password, email):
        if username.strip() not in self.users:
            self.users[username.strip()] = (password.strip(), email.strip(), UserDate.get_date())
            self.save()
            return 1
        else:
            return -1

    def validata(self, username, password):
        if self.get_user(username) != -1:
            return self.users[username][0] == password
        else:
            return False

    def save(self):
        with open(self.filename, "w") as fb:
            for user in self.users:
                fb.write(user+"," + self.users[user][0] + "," + self.users[user][1] + "," + self.users[user][2] + "\n")

    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]

