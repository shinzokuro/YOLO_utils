from pathlib import Path
from YOLO_utils.scripts.utils.ziputils import unzip_file, get_zip_path, zip_directory
from abc import ABC, abstractmethod
from typing import Optional
import logging
import zipfile
from pathlib import Path
import os
import shutil
class ExperimentTracker:

    def __init__(self, expirement_priority_text_file: str):
        self.priority_text_path = Path(expirement_priority_text_file)

    def get_experiment_to_run(self):
        """
        returns the current expirement, or None if no expirement is available
        """
        with open(self.priority_text_path, "r") as f:
            priority_str = f.readlines()
        self.priority_lst = [line.strip() for line in priority_str]
        if len(self.priority_lst) == 0:
            return
        self.current_experiment = priority_str[0]
        return self.current_experiment
    def _mark_expirement_as_completed(self):
        self.priority_lst.remove(self.current_experiment)
        with open(self.priority_text_path, "w") as f:
            for line in self.priority_lst:
                f.write(line + "\n")


class CollabWorkspaceManager:
    def __init__(
        self, current_experiment: str, working_directory: str = "/content"
    ):
        self.current_experiment: str = current_experiment
        self.working_directory: Path = Path(working_directory) / self.current_experiment
        self.dataset: Path = self.working_directory / "dataset"
        self.model: Path = self.working_directory / "model"
        self.test_data: Path = self.working_directory / "test_data"
        self.results: Path = self.working_directory / "results"
        self.structure: dict[str, Path] = {
            "datasets": self.dataset,
            "models": self.model,
            "test_data": self.test_data,
            "results": self.results,
        }

    def setup(self, dataset_zip, test_data_zip):
        """Create workspace directories and optionally extract ZIPs."""
        for name, path in self.structure.items():
            path.mkdir(parents=True, exist_ok=True)
            logging.info(f"Created or verified folder: {path}")

        if dataset_zip:
            unzip_file(dataset_zip, self.dataset)

        if test_data_zip:
            unzip_file(test_data_zip, self.test_data)

    def save_results(self, dest_path):
        # save model
        zip_directory(self.model, dest_path, rf"{self.current_experiment}_model")
        # save results
        zip_directory(self.results, dest_path, rf"{self.current_experiment}_results")
    def clear_model_directory(self):
        if os.path.exists(self.model) and os.path.isdir(self.model):
        # List all the files and subdirectories
            for item in os.listdir(self.model):
                item_path = os.path.join(self.model, item)
                # Check if it is a file or directory
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.unlink(item_path)  # Remove the file or symlink
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)  

# Example usage
