from pathlib import Path
from yolov5 import val
from YOLO_utils.scripts.YOLOv5.config import create_val_config
from YOLO_utils.scripts.utils.yaml_utils import create_val_yaml
from YOLO_utils.scripts.YOLOv5.save_data import save_pr_curve_data, save_mc_curve_data
import utils.metrics as metrics
from utils.metrics import (
    plot_pr_curve as original_plot_pr_curve,
    plot_mc_curve as original_plot_mc_curve,
)




def modified_plot_pr_curve(px, py, ap, save_dir="pr_curve.png", names=()):
    # save the results
    save_pr_curve_data(px, py, ap, save_dir, names)
    # Call the original plot_pr_curve function
    original_plot_pr_curve(px, py, ap, save_dir, names)


# Confidence-F1 Curve, Confidence-Precision Curve, Confidence-Recall Curve
def modified_plot_mc_curve(
    px, py, save_dir="mc_curve.png", names=(), xlabel="Confidence", ylabel="Metric"
):
    # flatten the results
    save_mc_curve_data(px, py, save_dir, names, xlabel, ylabel)
    # Call the original plot_pr_curve function
    original_plot_mc_curve(px, py, save_dir, names, xlabel, ylabel)


metrics.plot_pr_curve = modified_plot_pr_curve
metrics.plot_mc_curve = modified_plot_mc_curve


def run_validation(save_path: Path, test_data_path, pt_files: dict):
    test_data = [
        directory for directory in Path(test_data_path).iterdir() if directory.is_dir()
    ]
    for data_path in test_data:
        data_yaml = create_val_yaml(data_path)
        project_path = save_path / data_path.stem
        for model_name, pt_file_path in pt_files.items():
            opt = create_val_config(
                weights_path=pt_file_path,
                data_path=data_yaml,
                project_path=project_path,
                name=model_name,
            )
            val.main(opt)
