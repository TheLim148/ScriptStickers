from PIL import Image
import shutil
import subprocess
import os

def tempFiles(dir_to):
    bat_path = os.path.join(dir_to, "delete_all.bat")

    with open(bat_path, "w") as f:
        f.write("timeout /t 1800 >nul\n")
        f.write(f"del /f /q \"{dir_to}\\*.png\"\n")
        f.write(f"del /f /q \"{bat_path}\"\n")

    subprocess.Popen([bat_path], creationflags=subprocess.CREATE_NO_WINDOW)

def only_name(file_path):
    extension = "." + file_path.split('.')[-1]
    return file_path.replace(extension,"")

def make_avatar(avatar_path, file):
    rename(avatar_path)
    avatar = Image.open(f"{avatar_path}/{file}")
    if(avatar.width == avatar.height):
        avatar = avatar.convert("RGBA")
        avatar = avatar.resize((100, 100))
        avatar = avatar.save(f"{avatar_path}/{only_name(file)}.png", optimize = True)
    else:
        try:
            avatar1 = avatar.copy()
            avatar1.save(f"{avatar_path}/{only_name(file)}_original.jpg")
            avatar.close()
            os.mkdir(f"{avatar_path}/temp1")
            os.mkdir(f"{avatar_path}/temp2")

            os.rename(f"{avatar_path}/{file}", f"{avatar_path}/temp1/{file}")
            dir_from = f"{avatar_path}/temp1"
            dir_to = f"{avatar_path}/temp2"
            change(dir_from, dir_to)
            os.rename(f"{avatar_path}/temp2/{only_name(file)}.png", f"{avatar_path}/{only_name(file)}.png")
            
            shutil.rmtree(f"{avatar_path}/temp1")
            shutil.rmtree(f"{avatar_path}/temp2")

            avatar = Image.open(f"{avatar_path}/{only_name(file)}.png")
            avatar = avatar.resize((100, 100))
            avatar = avatar.save(f"{avatar_path}/{only_name(file)}.png", optimize = True)
        except FileExistsError:
            pass

def rename(input_dir):
    files = sorted(os.listdir(input_dir))
    for i, file in enumerate(files):
        os.rename(f"{input_dir}/{file}", f"{input_dir}/temp_{i}.jpg")

    temp_files = sorted(os.listdir(input_dir))
    for i, file in enumerate(temp_files):
        os.rename(f"{input_dir}/{file}", f"{input_dir}/{i}.jpg")

def change_one_file(dir_from, file, dir_to):
    image = Image.open(f"{dir_from}/{file}")
    canvas = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
    if (image.width <= image.height):
        coef = 512/image.height
        image = image.resize((round(image.width*coef), round(image.height*coef)))
        canvas.paste(image, (256-round(image.width/2), 0))
    elif (image.height <= image.width):
        coef = 512/image.width
        image = image.resize((round(image.width*coef), round(image.height*coef)))
        canvas.paste(image, (0, 256-round(image.height/2)))
    
    canvas = canvas.save(f"{dir_to}/{only_name(file)}.png", optimize = True)

def change(dir_from, dir_to):
    rename(dir_from)
    files = sorted(os.listdir(dir_from))
    for file in files:
        image = Image.open(f"{dir_from}/{file}")
        canvas = Image.new("RGBA", (512, 512), (0, 0, 0, 0))

        if (image.width <= image.height):
            coef = 512/image.height
            image = image.resize((round(image.width*coef), round(image.height*coef)))
            canvas.paste(image, (256-round(image.width/2), 0))
        elif (image.height <= image.width):
            coef = 512/image.width
            image = image.resize((round(image.width*coef), round(image.height*coef)))
            canvas.paste(image, (0, 256-round(image.height/2)))
        
        canvas = canvas.save(f"{dir_to}/{only_name(file)}.png", optimize = True)

        if(os.path.getsize(f"{dir_to}/{only_name(file)}.png") >= 524_288):
            temp_image = Image.open(f"{dir_from}/{file}")
            temp_image.save(f"{dir_from}/{file}", optimize = True, quality = 20)
            change_one_file(dir_from, file, dir_to)
