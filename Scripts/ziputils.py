import os
import shutil
import zipfile
from tqdm import tqdm
from pathlib import Path


def get_zip_path(path):
    """Find the zip file in the folder"""
    zip_files = list(path.glob("*.zip"))
    if len(zip_files) == 0:
        raise FileNotFoundError("No zip file found in the datasets folder.")
    elif len(zip_files) > 1:
        raise ValueError("Multiple zip files found in the datasets folder.")
    return zip_files[0]  # Return the only zip file


def unzip_file(zip_file, dst_dir):
    if zipfile.is_zipfile(zip_file):
        # Create a directory for the extracted files
        extract_dir = os.path.join(dst_dir, zip_file.stem)
        os.makedirs(extract_dir, exist_ok=True)
        # Extract the ZIP file
        with zipfile.ZipFile(zip_file) as zf:
            for member in tqdm(zf.infolist(), desc=rf"Extracting {zip_file.stem}"):
                try:
                    zf.extract(member, extract_dir)
                except zipfile.error as e:
                    print(f"Error extracting {member.filename}: {e}")
    else:
        print(f"{zip_file} is not a valid ZIP file.")
        return


def unzip_all_files(src_dir: Path, dst_dir: Path):
    """_summary_
        unzips all zip file in a folder

    Args:
        src_dir (Path): directory containing zip files

        dst_dir (Path): unzip directory
    """
    # Check if source directory exists
    if not src_dir.exists():
        print(f"Source directory '{src_dir}' does not exist.")
        return

    # Create destination directory if it doesn't exist
    if not dst_dir.exists():
        dst_dir.mkdir()

    # Iterate over all files in the source directory
    for zip_file in src_dir.iterdir():
        # Check if the file is a ZIP file
        unzip_file(zip_file, dst_dir)


def zip_directory(directory_path):
    # Ensure the directory exists
    if not os.path.isdir(directory_path):
        print(f"The directory {directory_path} does not exist.")
        return
    zip_file_path = directory_path
    # Create a zip file from the directory
    shutil.make_archive(zip_file_path, "zip", directory_path)
    print(f"Directory {directory_path} has been zipped into {zip_file_path}.zip")
