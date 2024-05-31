import os
import shutil

DESTINE_DIR="C:/Program Files (x86)/GOG Galaxy/Games/Medal of Honor - Allied Assault War Chest"
NEW_ARCHIVE="C:/Program Files (x86)/GOG Galaxy/Games/Medal of Honor - Allied Assault War Chest/mohaa.exe"

def initialize_menu():
    print("+","-".center(40,"-"), end="+\n")
    print("|","MOHAA SELECTION MENU".center(40), end="|\n")
    print("+","-".center(40,"-"), end="+\n")
    print("|", "[1]-MOHAA", " ".center(30), end="|\n")
    print("|", "[2]-Breaktrough", " ".center(24), end="|\n")
    print("|", "[3]-Spearhead", " ".center(26), end="|\n")
    print("+","-".center(40,"-"), end="+\n")

originals_path=("C:/Program Files (x86)/GOG Galaxy/Games/Medal of Honor - Allied Assault War Chest/MOHAA.exe",
"C:/Program Files (x86)/GOG Galaxy/Games/Medal of Honor - Allied Assault War Chest/moh_breakthrough.exe", 
"C:/Program Files (x86)/GOG Galaxy/Games/Medal of Honor - Allied Assault War Chest/moh_Spearhead.exe",)

backup_dir="C:/Program Files (x86)/GOG Galaxy/Games/Medal of Honor - Allied Assault War Chest/backup"

if os.path.isdir(backup_dir):
    print("backup already make")
else:
    os.mkdir(backup_dir)
    shutil.copy(originals_path[0], backup_dir)
    shutil.copy(originals_path[1], backup_dir)
    shutil.copy(originals_path[2], backup_dir)
    print("backup done")

initialize_menu()
option_selected=input("type the digit correspondent of the game you want play: ")

if option_selected=="2":
    #deletar o arquvio MOHAA e renome o atalho correspondente para mohaa

    #verifica se o executável a ser moficado está presente, se não significa que o atalho já está pronto e não precisa ser modificado
    if os.path.isfile(originals_path[1])==False:
        print("executable already modified")
    else:
        if os.path.isfile(originals_path[0]):
            os.remove(originals_path[0])
            os.rename(originals_path[1], NEW_ARCHIVE)
            print("arquivo renomeado...")
    
    if os.path.isfile(originals_path[2])==False:
        shutil.copy(backup_dir+"/moh_Spearhead.exe", DESTINE_DIR)
        print("spearhead restaurado")

elif option_selected=="3":
    if os.path.isfile(originals_path[2])==False:
        print("executable already modified")
    else:
        if os.path.isfile(originals_path[0]):
            os.remove(originals_path[0])
        
        os.rename(originals_path[2], NEW_ARCHIVE)
        print("arquivo renomeado...")
    
    if os.path.isfile(originals_path[1])==False:
        shutil.copy(backup_dir+"/moh_breakthrough.exe", DESTINE_DIR)
        print("breaktrough restaurado")

elif option_selected=="1":
    os.remove(NEW_ARCHIVE)
    shutil.copy(backup_dir+"/MOHAA.exe", DESTINE_DIR)

    if os.path.isfile(originals_path[1])==False:
        shutil.copy(backup_dir+"/moh_breakthrough.exe", DESTINE_DIR)
        print("breaktrough restaurado")
    
    if os.path.isfile(originals_path[2])==False:
        shutil.copy(backup_dir+"/moh_Spearhead.exe", DESTINE_DIR)
        print("spearhead restaurado")

else:
    print("digite uma opção válida")