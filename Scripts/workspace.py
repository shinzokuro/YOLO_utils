from pathlib import Path
from ziputils import unzip_file


class DriveIO:
    """Manage the uploading and dowloading to and from a drive folder.
    currently only supports unzipping the dataset from drive and uploading any data"""

    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.dataset_zip_file = self._get_zip_path(base_dir)

    def _get_zip_path(self):
        """Find the zip file in the datasets folder."""
        zip_files = list(self.datasets.glob("*.zip"))
        if len(zip_files) == 0:
            raise FileNotFoundError("No zip file found in the datasets folder.")
        elif len(zip_files) > 1:
            raise ValueError("Multiple zip files found in the datasets folder.")
        return zip_files[0]  # Return the only zip file

    def upload_data():
        pass

    def download_dataset(self, dest_dir):
        unzip_file(self._get_zip_path, Path(dest_dir))
        pass

class CollabWorkspaceManager:

    def __init__(
        self,
        drive_workspace: DriveIO,
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
    drive_workspace = DriveIO()
    workspace_manager = CollabWorkspaceManager()
    workspace_manager.setup()
