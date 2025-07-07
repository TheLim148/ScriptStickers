import ImageStickers as IS
import os
import shutil

def clearDirectory(dir_path):
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        
        if os.path.isfile(item_path) or os.path.islink(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)

if __name__ == "__main__":
    try:
        deleteFiles = 0
        deleteFiles = int(input("\nDo you want to delete your files after 30 minutes?" \
                                "\n1 - Yes; 0 - No" \
                                "\nP.S No by default" \
                                "\n~$ "))
    except Exception as e:
        print(f"Error: {e}")

    while True:
        choose = int(input( "\n1 - сделать стикеры" \
                            "\n2 - сделать аватар" \
                            "\n3 - переименовать файлы" \
                            "\n4 - выход" \
                            "\n~$ "))

        match(choose):
            case 1:
                option = int(input("\nВы инициализируете стикеры или добавляете их уже к существующим?" \
                                "\n(1 - новые стикеры, 2 - добавление к старым)" \
                                "\n~$ "))
                match(option):
                    case 1: # New stickers
                        try:
                            dir_from = input("\nВведите название исходной папки: ")
                            dir_to = input("Введите название итоговой папки: ")

                            if(os.listdir(dir_to)):
                                wantToDeleteStickers = int(input("\nВаша выходная директория не пустая, если вы продолжите, то её содержимое будет удалено" \
                                                                 "\nВы хотите продолжить?" \
                                                                 "\n1 - Yes; 2 - No" \
                                                                 "\n~$ "))
                                match(wantToDeleteStickers):
                                    case 1:
                                        clearDirectory(dir_to)
                                    case 2:
                                        break
                                IS.rename(dir_from, dir_to, option)
                                IS.changePhotos(dir_from, dir_to)

                            if (deleteFiles == 1):
                                IS.tempFiles(dir_to)
                                print("Стикеры успешно созданы!\nОни будут автоматически удалены через 30 минут")
                            print("Стикеры успешно созданы!")
                        except Exception as e:
                            print(f"Error: {e}")
                        break

                    case 2: # Addition to old stickers
                        try:
                            dir_from = input("\nВведите название исходной папки: ")
                            dir_to = input("Введите название итоговой папки: ")
                        
                            IS.rename(dir_from, dir_to, option)
                            IS.changePhotos(dir_from, dir_to)
                            if (deleteFiles == 1):
                                IS.tempFiles(dir_to)
                                print("Стикеры успешно добавлены!\nОни будут автоматически удалены через 30 минут")
                            print("Стикеры успешно добавлены!")
                        
                        except Exception as e:
                            print(f"Error: {e}")
                        break

                    case _:
                        print("Bruh")
                        break

            case 2:
                avatar_path = input("\nВведите путь до директории с файлом-аватаром: ")
                file = input("Введите имя файла-аватара: ")
                try:
                    IS.makeAvatar(avatar_path, file)
                    if (deleteFiles == 1):
                        IS.tempFiles(avatar_path)
                        print("Аватарка готова!\nОна будут автоматически удалены через 30 минут")
                    print("Аватарка готова!")
                except FileNotFoundError:
                    print("There is no file or folder")

            case 3:
                input_dir = input("Введите директорию, где хотите переименовать файлы: ")
                IS.rename(input_dir, None, option=1)
                print("Переименование прошло успешно")

            case 4:
                print("Поки!")
                break