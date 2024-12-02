from pathlib import Path
from YOLO_utils.scripts.ziputils import unzip_file, get_zip_path, zip_directory
from abc import ABC, abstractmethod
from typing import Optional
import logging
import zipfile
from pathlib import Path


class CollabWorkspaceManager:

    def __init__(
        self, expirement_priority_text_file: str, working_directory: str = "/content"
    ):
        self.priority_text_path = Path(expirement_priority_text_file)
        self.get_expirement_to_run()
        self.experiment_name = self.experiment_name
        self.working_directory: Path = Path(working_directory) / self.experiment_name
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

    def _get_expirement_to_run(self):
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
        # remove experiment from priority list
        self._mark_expirement_as_completed()
        # save model
        zip_directory(self.model, dest_path , fr"{self.experiment_name}_model" )
        # save results
        zip_directory(self.results, dest_path , rf"{self.experiment_name}_results")

    def _mark_expirement_as_completed(self):
        self.priority_lst.remove(self.current_experiment)
        with open(self.priority_text_path, "w") as f:
            for line in self.priority_lst:
                f.write(line + "\n")
