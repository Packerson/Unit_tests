from datetime import datetime


def div(a, b):
    if isinstance(a, str):
        a = float(a)

    if isinstance(b, str):
        b = float(b)

    if b == 0:
        raise ZeroDivisionError("Nie dziel przez 0!")
    return a / b


def analyze_pesel(pesel):
    """This function checks if PESEL is valid"""
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    weight_index = 0
    digits_sum = 0

    # Wyliczanie wagi
    for digit in pesel[:-1]:
        digits_sum += int(digit) * weights[weight_index]
        weight_index += 1

    # Obliczanie liczby kontrolnej
    pesel_modulo = digits_sum % 10
    validate = 10 - pesel_modulo
    if validate == 10:
        validate = 0

    # Sprawdzanie płci
    gender = "male" if int(pesel[-2]) % 2 == 1 else "female"  # 1

    # Obliczanie daty urodzeniaq
    year, month, day = pesel[0:2], int(pesel[2:4]), int(pesel[4:6])  # 2
    if month > 12:  # If year > 2000, subtract 20 from month
        month -= 20
        year = int("20" + str(year))
    else:
        year = int("19" + str(year))

    return {
        "pesel": pesel,
        "valid": validate == int(pesel[-1]),
        "gender": gender,
        "birth_date": datetime(year, month, day)
    }


def calculate_vat(price, vat_rate):
    return price * vat_rate / 100


def hash_password(password):
    from hashlib import md5
    if (
            len(password) >= 8
            and any(char for char in password if char.isupper())
            and any(char for char in password if char.islower())
            and any(char for char in password if char.isdigit())
            and any(char for char in password if char in "!@#$%^&*()_+-={}[]|\:;'<>?,./\"")
    ):
        return md5(password.encode("utf-8")).hexdigest()
    return None


def fizz_buzz(x):
    writing = ''
    for i in range(1, x + 1):
        if i % 3 == 0 and i % 5 == 0:
            writing = writing + 'FizzBuzz'
        elif i % 5 == 0:
            writing = writing + 'Buzz'
        elif i % 3 == 0:
            writing = writing + "Fizz"
        else:
            writing = writing + str(i)
    return writing


# Aby ustalić, czy rok jest rokiem przestępnym, wykonaj następujące kroki:
#
# Jeśli rok jest równomiernie podzielny przez 4, przejdź do kroku 2. Jeśli nie, przejdź do kroku 5.
# Jeśli rok jest równomiernie podzielny przez 100, przejdź do kroku 3. Jeśli nie, przejdź do kroku 4.
# Jeśli rok jest równomiernie podzielny przez 400, przejdź do kroku 4. Jeśli nie, przejdź do kroku 5.
# Rok jest rokiem przestępnym (ma 366 dni).
# Rok nie jest rokiem przestępnym (ma 365 dni).
def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False


def word_wrap(string, length):
    marks = ["!", ",", ".", "?", " "]
    i = 0
    while True:
        # if string[length] in marks:
        #     string = string[0:length] + "..."
        #     print(string)
        #     return string
        if string[length + i] in marks:
            string = string[0:length + i] + "..."
            print(string)
            return string
        i = i + 1


lorem_ipsum = "Lorem! ipsum dolor sit amet, consectetur adipiscing elit. " \
              "Etiam tincidunt consequat lacus vel vestibulum. Vestibulum id " \
              "vestibulum lacus. Suspendisse sollicitudin arcu sit amet blandit " \
              "blandit. Fusce congue erat ac felis iaculis, sit amet sagittis est " \
              "tincidunt. Proin tincidunt eros sit amet ligula mattis, a laoreet sem " \
              "mollis. Maecenas quis fermentum ex. Aenean in scelerisque tortor. " \
              "Pellentesque congue lectus ac condimentum vulputate. "

word_wrap(lorem_ipsum, 7)
print(lorem_ipsum[7])
# def aaa(a):
#     marks = ["!", ",", ".", "?"]
#     if a in marks:
#         print("Ok")
#     else:
#         print("nie")
#
# aaa('a')
