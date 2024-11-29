from pathlib import Path
import yaml


def write_yaml(data, file_path):
    with open(Path(file_path), "w") as file:
        yaml.safe_dump(data, file, default_flow_style=False, sort_keys=False)


def create_dataset_yamlfile(path, classes={0: "person"}):
    data = {
        "path": rf"{path}",
        "train": "images/train",  # train images (relative to 'path') 128 images
        "val": "images/val",  # val images (relative to 'path') 128 images
        "test": "images/val",  # test images (optional)
        "names": classes,
    }
    write_yaml(data, path)


def read_yaml(file_path):
    data = None
    with open(Path(file_path), "r") as file:
        data = yaml.safe_load(file)
    return data
