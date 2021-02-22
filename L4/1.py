# почему-то не смог выполнить программу через терминал, сначала было Permission Denied,
# но через sudo тоже не сработало, выводит: command not found

from sys import argv
script_name, hours, wage, bonus = argv

def salary(hours, wage, bonus):
    print(hours * wage + bonus)

salary()