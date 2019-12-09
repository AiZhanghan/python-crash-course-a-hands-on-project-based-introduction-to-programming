if __name__ == '__main__':
    # 2_3
    name = 'Eric'
    print("Hello {}, would you like to learn some Python today?".format(name))
    # 2_4
    print("Hello {}, would you like to learn some Python today?".format(name.lower()))
    print("Hello {}, would you like to learn some Python today?".format(name.upper()))
    print("Hello {}, would you like to learn some Python today?".format(name.title()))
    # 2_5
    print('Albert Einstein once said, "A person who never mada a mistake never tried anything new."')
    # 2_6
    name = 'Albert Einstein'
    message = name + ' once said, "A person who never mada a mistake never tried anything new."'
    print(message)
    # 2_7
    name = '  Albert Einstein   '
    message = name + ' once said, \n"A person who never mada a mistake never tried anything new."'
    print(message)

    name = '  Albert Einstein   '
    message = name.rstrip() + ' once said, \n"A person who never mada a mistake never tried anything new."'
    print(message)

    name = '  Albert Einstein   '
    message = name.lstrip() + ' once said, \n"A person who never mada a mistake never tried anything new."'
    print(message)

    name = '  Albert Einstein   '
    message = name.strip() + ' once said, \t"A person who never mada a mistake never tried anything new."'
    print(message)