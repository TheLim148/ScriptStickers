import ImageStickers as IS

if __name__ == "__main__":
    deleteFiles = False
    try:
        deleteFiles = int(input("Do you want to delete your files after 30 minutes?" \
                                "\n1 == True | 0 == False" \
                                "\nP.S False by default" \
                                "\n~$ "))
        if (deleteFiles == 1):
            deleteFiles = True
        elif (deleteFiles == 0):
            deleteFiles = False
    except ValueError:
        print("It's not a number!")

    while True:
        choose = int(input("\n1 - сделать стикеры" \
                            "\n2 - сделать аватар" \
                            "\n3 - переименовать файлы" \
                            "\n4 - выход" \
                            "\n~$ "))

        match(choose):
            case 1:
                dir_from = input("\nВведите название исходной папки: ")
                dir_to = input("Введите название итоговой папки: ")
                try:
                    IS.change(dir_from, dir_to)
                    if (deleteFiles == True):
                        IS.tempFiles(dir_to)
                        print("Стикеры успешно созданы!\nОни будут автоматически удалены через 30 минут")
                    print("Стикеры успешно созданы!")
                except FileNotFoundError:
                    print("There is no folder or file")
            case 2:
                avatar_path = input("\nВведите путь до директории с файлом-аватаром: ")
                file = input("Введите имя файла-аватара: ")
                try:
                    IS.make_avatar(avatar_path, file)
                    if (deleteFiles == True):
                        IS.tempFiles(dir_to)
                        print("Аватарка готова!\nОна будут автоматически удалены через 30 минут")
                    print("Аватарка готова!")
                except FileNotFoundError:
                    print("There is no file or folder")
            case 3:
                input_dir = input("Введите директорию, где хотите переименовать файлы: ")
                IS.rename(input_dir)
                print("Переименование прошло успешно")
            case 4:
                print("Поки!")
                break