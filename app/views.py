from django.shortcuts import render


def equation(a,b,c):
    if c == "+":
        return int(a) + int(b)
    elif c == "-":
        return int(a) - int(b)
    elif c == "x":
        return int(a) * int(b)
    elif c == "/":
        if b == "0":
            return "Cant divide by 0"
        return int(a) / int(b)
    else:
        return "HELP"

def stringify(a,b,c):
    return a + b + c +" ="


def index_view(request):
    numbers = request.GET
    if request.GET:
        number1 = numbers["number1"]
        number2 = numbers["number2"]
        operation = numbers["operation"]
    else:
        number1 = 1
        number2 = 1
        operation = "+"

    context = {
    "answer" : equation(number1, number2, operation),
    "EQ" : stringify(number1, operation, number2)
    }
    return render(request, "index.html", context)
