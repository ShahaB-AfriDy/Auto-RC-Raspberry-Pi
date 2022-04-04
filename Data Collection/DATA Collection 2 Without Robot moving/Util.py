import os

def Create_Dir():
    Total_Files = len(os.listdir(os.getcwd()))-2
    Dir_Name = "IMG_"+str(Total_Files)
    if not os.path.exists(str(Total_Files)):
        os.mkdir(Dir_Name)
    return Dir_Name



def Delete_Folders(Flag=False):

    import shutil
    List = os.listdir(os.getcwd())
    for u in List:
        if '.py' not in u:
            shutil.rmtree(os.getcwd()+'\\'+u)
    if Flag:
        print(List)

if __name__ == "__main__":
    Delete_Folders()
    # ...
