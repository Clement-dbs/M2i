class InvalidLogException(Exception):
    def __init__(self, message, log):
        self.message = message
        self.log = log

    def display_exception(self):
        print(f"{self.message} : {self.log}")

class InvalidPasswordException(Exception):
    pass


def input_log():
    log = input("Veuillez entrer un login SVP (celui-ci ne doit posséder que des lettres minuscules) : ")

    if log.isalpha():
        if log.islower():
            return log
        else:
            raise InvalidLogException("Il ne dois y avoir que des minuscules dans le login !", log)
    else:
        raise InvalidLogException("Il ne doit y avoir que des lettres dans le login !", log)
    
def input_password():
    password = input("Veuillez entrer un mot de passe SVP (celui-ci ne doit posséder que des chiffres) : ")
    if password.isdigit():
        return password
    else:
        raise InvalidPasswordException("Le mot de passe ne dois posséder que des nombres !")
    
def login():
    while True: 
        try:
            log = input_log()
            password = input_password()
        except InvalidLogException as e:
            print(e)
        except InvalidPasswordException as e: 
            print(e)
        else: 
            return (log, password)
        

log, password = login()
print(f"Bienvenue à {log}, votre mot de passe est {password}")