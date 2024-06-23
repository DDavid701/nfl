def format_number(type, number):
    if type == 'simple':
        if len(str(number)) == 4:
            number_parts = str(number).strip()
            number_formatted = f'{number_parts[0]}.{number_parts[1]}k'
            return number_formatted
        elif len(str(number)) == 5:
            number_parts = str(number).strip()
            number_formatted = f'{number_parts[0]}{number_parts[1]}.{number_parts[2]}k'
            return number_formatted
        elif len(str(number)) == 6:
            number_parts = str(number).strip()
            number_formatted = f'{number_parts[0]}{number_parts[1]}{number_parts[2]}.{number_parts[3]}k'
            return number_formatted
        elif len(str(number)) == 7:
            number_parts = str(number).strip()
            number_formatted = f'{number_parts[0]}.{number_parts[1]}m'
            return number_formatted
        elif len(str(number)) == 8:
            number_parts = str(number).strip()
            number_formatted = f'{number_parts[0]}{number_parts[1]}.{number_parts[2]}m'
            return number_formatted
        elif len(str(number)) == 9:
            number_parts = str(number).strip()
            number_formatted = f'{number_parts[0]}{number_parts[1]}{number_parts[2]}.{number_parts[3]}m'
            return number_formatted
        elif len(str(number)) == 10:
            number_parts = str(number).strip()
            number_formatted = f'{number_parts[0]}.{number_parts[1]}b'
            return number_formatted
        elif len(str(number)) == 11:
            number_parts = str(number).strip()
            number_formatted = f'{number_parts[0]}{number_parts[1]}.{number_parts[2]}b'
            return number_formatted
        elif len(str(number)) == 12:
            number_parts = str(number).strip()
            number_formatted = f'{number_parts[0]}{number_parts[1]}{number_parts[2]}.{number_parts[3]}b'
            return number_formatted
        elif len(str(number)) == 13:
            number_parts = str(number).strip()
            number_formatted = f'{number_parts[0]}.{number_parts[1]}t'
            return number_formatted
        elif len(str(number)) == 14:
            number_parts = str(number).strip()
            number_formatted = f'{number_parts[0]}{number_parts[1]}.{number_parts[2]}t'
            return number_formatted
        elif len(str(number)) == 15:
            number_parts = str(number).strip()
            number_formatted = f'{number_parts[0]}{number_parts[1]}{number_parts[2]}.{number_parts[3]}t'
            return number_formatted
        else: return number

print(format_number(type='simple', number=2440))