from PIL import Image
import imagehash
from pathlib import Path
import os
import win32com.client
from win32com.client import Dispatch
from tqdm import tqdm

dir_path = r"F:\Aditya\Studies\College\01 Projects\00 Self\04 similar images detection\test data"
# dir_path = input("Enter the directory path : ")
duplicates_dir = Path(dir_path) / "duplicates"
if not duplicates_dir.exists():
    duplicates_dir.mkdir()

img_hashes = {}

for img_filename in tqdm(list(Path(dir_path).rglob('*'))):
    if img_filename.suffix.lower() not in ('.bmp', '.gif', '.jpeg', '.jpg', '.png', '.tiff'):
        continue

    try:
        with Image.open(img_filename) as image:
            img_hash = imagehash.dhash(image)  # use dhash instead of average_hash

        if img_hash in img_hashes:
            duplicate_file_path = duplicates_dir / img_filename.name
            os.rename(img_filename, duplicate_file_path)
            print(f"Duplicate image file found and moved: {img_filename} -> {duplicate_file_path}")

            file_path = img_hashes[img_hash]
            path = str(file_path)

            new_path = str(img_filename.with_suffix('.lnk'))

            shell = win32com.client.Dispatch("WScript.Shell")
            shortcut = shell.CreateShortCut(new_path)
            shortcut.Targetpath = path
            shortcut.save()

        else:
            img_hashes[img_hash] = img_filename
            print(f"Image file processed: {img_filename}")
    except Exception as e:
        print(f"Error processing image file {img_filename}: {str(e)}")










# from PIL import Image
# import os
# import imagehash
# from pathlib import Path
# from tqdm import tqdm
# import win32com.client


# # image1 = Image.open("image1.jpg")
# # image2 = Image.open("image2.jpg")

# dir_path = input("Enter directory path : ")
# duplicates_dir = os.path.join(dir_path, "duplicates")
# if not os.path.exists(duplicates_dir):
#     os.makedirs(duplicates_dir)

# img_hashes = {}

# for img_filename in tqdm(list(Path(dir_path).rglob('*'))):
#     if img_filename.suffix.lower() in ('bmp', 'gif', 'jpeg', 'jpg', 'png', 'tiff'):
#         try:
#              with Image.open(img_filename) as image:
                    # img_hash = imagehash.dhash(image) 

#             if img_hash in img_hashes:
#                 duplicate_file_path = os.path.join(duplicates_dir, img_filename.name)
#                 os.rename(img_filename, duplicate_file_path)
#                 print(f"Duplicate image file found and moved: {img_filename} -> {duplicate_file_path}")

#                 file_path = img_hashes[img_hash]
#                 path=str(img_filename)
#                 if img_filename.suffix.lower() in ('bmp', 'gif', 'jpg', 'png'):
#                     new_path = f"{path[:-3]}lnk"
#                 if img_filename.suffix.lower() in ('jpeg','tiff'):
#                     new_path = f"{path[:-4]}lnk"
#                 shell = win32com.client.Dispatch("WScript.Shell")
#                 shortcut = shell.CreateShortCut(new_path)
#                 shortcut.Targetpath = file_path
#                 shortcut.save()
#             else:
#                 img_hashes[img_hash] = str(img_filename)
#                 print(f"Audio file processed: {img_filename}")
#         except Exception as e:
#             print(f"Error processing audio file {img_filename}: {str(e)}")