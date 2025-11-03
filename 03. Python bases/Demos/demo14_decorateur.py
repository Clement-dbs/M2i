# Un décorateur simple se présente de la sorte
# Il s'agit d'une fonction qui accepte en paramètre une fonction
def mon_decorateur(fonction):
    def wrapper():
        print("je fais des choses avant")
        # instructions effectuées avant

        fonction()

        #instruction effectuées après
        print("je fais des choses après")

    return wrapper

@mon_decorateur
def hello_world():
    print("Hello world!")

@mon_decorateur
def hello_world2():
    print("Hello world 2!")

hello_world()  # Ici on appelle la fonction qui se verra décorée

hello_world2()
