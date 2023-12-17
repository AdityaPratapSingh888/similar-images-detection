# Duplicate Image Detection Script

## Introduction

This Python script is designed to identify and move duplicate images within a specified directory. It utilizes the `imagehash` library to generate perceptual hashes of images and compares them to identify duplicates. Duplicate images are moved to a separate "duplicates" directory, and shortcuts to the original files are created in the original location.

## Usage

1. **Installation of Dependencies:**
    - Ensure you have the necessary dependencies installed. You can install them using the following:
        ```
        pip install Pillow imagehash tqdm
        ```

2. **Script Configuration:**
    - Update the `dir_path` variable with the path of the directory containing images you want to process.

3. **Running the Script:**
    - Execute the script in a Python environment:
        ```
        python script_name.py
        ```
    - The script will process images, identify duplicates, move them to the "duplicates" directory, and create shortcuts to the original files.

## Notes

- The script supports various image formats such as BMP, GIF, JPEG, JPG, PNG, and TIFF.
- Duplicate images are identified based on perceptual hashing using the `dhash` algorithm.
- In case of a processing error for any image, an error message will be displayed.

## Additional Information

- This script utilizes the `win32com.client` library to create shortcuts in Windows.
- The `tqdm` library provides a progress bar to track the processing of images.

## Disclaimer

- Use this script responsibly and ensure you have a backup of your data before running it.
- The script may not handle all edge cases, and it is recommended to review the results in the "duplicates" directory.

Feel free to customize the script based on your specific requirements or contribute to its improvement.
