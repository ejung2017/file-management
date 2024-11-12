# file-management

Whatever file that gets downloaded, it will be sorted directly into the designated folder instead of the default Downloads folder. 

Steps: 
1. We need to allow python code to access the files (use os, shutil, watchdog libraries)
2. Destination folders are all created and the paths are defined
3. When any files gets downloaded to the default 'Downloads' folder, I moved to the new folder by using move() - changed the name of the file to destination_filename(entity)
4. Categorizing different file type happened based on the logic under the MovingFiles class.
5. Writing one correct function (ie. check_pdf_files()) allowed Copilot to suggest correct code snippets for the rest of the functions needed

Creating venv python environment: 

```
python3 -m venv .venv
```

Create a virtual environment to download packages and dependencies needed 
