# simplest match statements
def http_error(status):
    match status:
        case 400:
            return 'Bad request'
        case 404:
            return 'Not found'
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

print(http_error(404))

from enum import Enum
class Color (Enum):
    RED='red'
    GREEN='green'
    BLUE='blue'
color=Color(input("Enter your choice of 'red','blue', or 'green':"))
match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green!")
    case Color.BLUE:
        print("I'm feeling the blues!:(")