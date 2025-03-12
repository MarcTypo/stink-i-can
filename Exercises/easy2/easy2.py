def prompt(message):
    print(f'==> {message}')


prompt('What is your name?')
name = input() 

if name[-1] == '!':
    prompt(f'HELLO {name.upper()} WHY ARE YOU YELLING AT ME?')
else:
    prompt(f'Hello {name}')




def greetings(name):
    normal_greeting = f'Hello {name}.'
    loud_greeting = f'hello {name} why are we yelling?'.upper()
    return loud_greeting if '!' in name else normal_greeting