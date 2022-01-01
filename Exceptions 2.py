class accident(Exception):
    def __init__(self,msg):
        self.msg = msg
    def print_msg(self):
        print(f"user define Exception:",self.msg)

try:
    raise accident('Car crash')
    x = 1/0
except accident as e:
    e.print_msg()
finally:
    print('I learned')