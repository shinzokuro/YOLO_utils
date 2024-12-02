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
    zip_file = Path(zip_file)
    dst_dir = Path(dst_dir)
    if zipfile.is_zipfile(zip_file):
        # Create a directory for the extracted files
        extract_dir = dst_dir/ zip_file.stem
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

def zip_directory(source_dir, dest, zip_file_name):
    # Get all files in the directory, including subdirectories
    dest_zip = Path(dest) / fr"{zip_file_name}.zip"
    file_paths = []
    for dirpath, _, filenames in os.walk(source_dir):
        for filename in filenames:
            file_paths.append(os.path.join(dirpath, filename))

    # Create a zip file with progress bar
    with zipfile.ZipFile(dest_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in tqdm(file_paths, desc="Zipping files", unit="file"):
            zipf.write(file, os.path.relpath(file, source_dir))

    logging(f"Directory {source_dir} has been zipped to {dest_zip}")


# Example usage:
# source_directory = "/path/to/your/directory"  # Replace with your directory path
# output_zip = "output.zip"  # Output zip file name
# zip_directory_with_progress(source_directory, output_zip)
