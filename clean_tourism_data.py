import pandas as pd
import numpy as np

RAW_DATA_FILE = 'Travel_test_file.xlsx'
CLEANED_DATA_FILE = 'cleaned_tourism_data_for_powerbi.csv'

def clean_tourism_data(input_path, output_path):
    print(f"เริ่มต้น Clean ข้อมูลจาก: {input_path}")
    try:
        df = pd.read_excel(input_path)
        print("โหลดข้อมูล Excel สำเร็จ")
        print(f"ข้อมูลดิบมี {df.shape[0]} แถว, {df.shape[1]} คอลัมน์")
        # df_original_cols = df.columns.tolist() # เก็บชื่อคอลัมน์เดิมไว้ดู (ถ้าต้องการ)

    except FileNotFoundError:
        print(f"Error: ไม่พบไฟล์ '{input_path}'")
        return
    except Exception as e:
        print(f"Error: ไม่สามารถอ่านไฟล์ Excel ได้: {e}")
        return
