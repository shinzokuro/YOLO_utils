from pathlib import Path
from YOLO_utils.Scripts.ziputils import unzip_file
from abc import ABC, abstractmethod

class DriveIOZip:
    """Manage the uploading and dowloading to and from a drive folder.
    currently only supports unzipping the dataset from drive and uploading any data"""
    def upload_data(self, input_dir, dest_dir):
        """Zips and uploads the input folder """
        pass
    def download_data(self, input_dir, dest_dir):
        """unzips and download the input folder"""
        pass
    


class CollabWorkspaceManager:

    def __init__(
        self,
        working_directory="/content/workspace",
    ):
        self.working_directory = Path(working_directory)
        self.dataset = self.base_dir / "dataset"
        self.model = self.base_dir / "model"
        self.test_data = self.base_dir / "test_data"
        self.results = self.base_dir / "results"
        # Store all directories in a dictionary for easier management
        self.structure = {
            "datasets": self.datasets,
            "models": self.models,
            "test_data": self.test_data,
            "results": self.results,
        }

    def setup(self):
        """Create the workspace directories if they don't exist."""
        for name, path in self.structure.items():
            path.mkdir(parents=True, exist_ok=True)
            print(f"Created or verified folder: {path}")


def main():
    # driveIo = DriveIO()
    workspace_manager = CollabWorkspaceManager()
    workspace_manager.setup()
