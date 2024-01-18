class Ex(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg + msg)
        self.args = (msg,)

    def __str__(self):
        return self.args[0]

print(Ex('ex'))