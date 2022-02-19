import argparse
book = {"Masha": 89778881539, "Pasha": 89778081476, "Natasha": 89771231536}

parser = argparse.ArgumentParser(description='Telephon book')
parser.add_argument('-a', "--add", dest="param1")
parser.add_argument('-d', "--delete", dest="param2")
parser.add_argument('-s', "--show", dest="param3", default="all")

args = parser.parse_args()

if args.param1:
    name, tele = args.param1.split(":")
    if name in book:
        book[name] = [book.get(name), int(tele)]
        print("Контакт ", name, " обновлен")
        print(name, ":", book[name])
    else:
        book[name] = int(tele)
        print("Контакт", name, " добавлен")
        print(name, ":", book[name])

elif args.param2:
    name = args.param2
    if name in book:
        print("Контакт ", name, " удален")
        del name 
        print(book)
    elif name == "all":
        print("Телефонная книга очищена")
        book.clear()
        print(book)
    else:
        print("Ошибка, контакт", name, " не найден")


