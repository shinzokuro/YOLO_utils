import pandas as pd
import numpy as np
import os

# AP, PR Curve
def save_pr_curve_data(px, py, ap, save_dir="pr_curve.png", names=()):
    """_summary_
    saves the pr_curve data in excel
    """
    # Convert px, py, ap to numpy arrays if they are not already
    px = np.array(px)
    py = np.array(py)
    ap = np.array(ap)

    # Flatten the results
    precision = px.flatten()
    recall = py.flatten()
    ap_flat = ap.flatten()

    # Get the save paths
    save_path = os.path.dirname(save_dir)
    pr_excel_path = os.path.join(save_path, "Precision-Recall_Curve.xlsx")
    ap_excel_path = os.path.join(save_path, "IOU_AP.xlsx")

    # Create their respective dataframes
    ap_data = {"ap": ap_flat}
    pr_data = {"Precision": precision, "Recall": recall}
    pr_df, ap_df = pd.DataFrame(pr_data), pd.DataFrame(ap_data)

    # Save the recall, precision, and ap data to Excel files
    pr_df.to_excel(pr_excel_path, index=False)
    ap_df.to_excel(ap_excel_path, index=False)


# Confidence-F1 Curve, Confidence-Precision Curve, Confidence-Recall Curve
def save_mc_curve_data(
    px, py, save_dir="mc_curve.png", names=(), xlabel="Confidence", ylabel="Metric"
):
    """_summary_
    saves the mc_curve data in excel
    """
    px = np.array(px)
    py = np.array(py)
    # flatten the results
    x_values = px.flatten()
    y_values = py.flatten()
    # get the save paths
    path = os.path.dirname(save_dir)
    path = os.path.join(path, rf"{xlabel}-{ylabel}_Curve.xlsx")
    # create their respective dataframes
    data = {rf"{xlabel}": x_values, rf"{ylabel}": y_values}
    df = pd.DataFrame(data)
    # Save the recall and precision data to an Excel file
    df.to_excel(path, index=False)
