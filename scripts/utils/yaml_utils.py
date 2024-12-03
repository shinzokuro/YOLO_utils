from pathlib import Path
import yaml


def write_yaml(data, file_path):
    with open(Path(file_path), "w") as file:
        yaml.safe_dump(data, file, default_flow_style=False, sort_keys=False)


def create_dataset_yamlfile(
    dataset_path,
    file_name=r"data",
    train="images/train",
    val="images/val",
    test="images/val",
    classes={0: "person"},
):
    data = {
        "path": dataset_path,
        "train": train,  # train images (relative to 'path') 128 images
        "val": val,  # val images (relative to 'path') 128 images
        "test": test,  # test images (optional)
        "names": classes,
    }
    data_yaml_file = Path(dataset_path) / rf"{file_name}.yaml"
    write_yaml(data, data_yaml_file)
    return data_yaml_file

def read_yaml(file_path):
    data = None
    with open(Path(file_path), "r") as file:
        data = yaml.safe_load(file)
    return data


def create_val_yaml(
    dataset_path, new_val=r"images", new_test=r"images", file_name="test"
):
    # Read the YAML file
    return create_dataset_yamlfile(
        dataset_path, file_name=file_name, val=new_val, test=new_test
    )
