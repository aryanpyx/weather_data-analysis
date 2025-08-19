import os
from ydata_profiling import ProfileReport
import pandas as pd

df = pd.read_csv("openaq_lalbagh.csv")
profile = ProfileReport(df)
output_file_path = os.path.join(os.getcwd(), "ydata_profiling_report.html")
profile.to_file(output_file=output_file_path)