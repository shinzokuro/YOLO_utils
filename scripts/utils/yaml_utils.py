from pathlib import Path
import yaml


def write_yaml(data, file_path):
    with open(Path(file_path), "w") as file:
        yaml.safe_dump(data, file, default_flow_style=False, sort_keys=False)


def create_dataset_yamlfile(dataset_path, classes={0: "person"}, file_name=r"data"):
    data = {
        "path": rf"{dataset_path}",
        "train": "images/train",  # train images (relative to 'path') 128 images
        "val": "images/val",  # val images (relative to 'path') 128 images
        "test": "images/val",  # test images (optional)
        "names": classes,
    }
    data_yaml_file = Path(dataset_path) / rf"{file_name}.yaml"
    write_yaml(data, data_yaml_file)


def read_yaml(file_path):
    data = None
    with open(Path(file_path), "r") as file:
        data = yaml.safe_load(file)
    return data
