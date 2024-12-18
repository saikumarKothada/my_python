import os

def list_files(folder):
   try:
     files=os.listdir(folder)
     return files,None
   except FileNotFoundError:
     return None, "files not found"
   except PermissionError:
     return None, "permission denied"# PermissionError is raised when you don't have permission to access the folder

def main():
 
 folder_paths=input("Hey user enter folder paths seperated by space: ").split()
 for folder in folder_paths:
  files,error_message = list_files(folder)
  if files:
    for file in files:
      print(file)
  else:
    print(f"Error in Folder {folder} path: {error_message}")

    
if __name__=="__main__":
  main()