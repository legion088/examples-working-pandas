import pandas as pd


def get_dataframes_from_file(filename: str) -> dict:
    df = dict()
    for sheet_name in pd.ExcelFile(filename).sheet_names:
        df.setdefault(sheet_name, pd.read_excel(filename, sheet_name=sheet_name))
    return df


def write_data_in_sheets_file(filename: str, data: dict) -> None:
    with pd.ExcelWriter(filename) as f_w:
        for sheet_name, sub_data_dict in data.items():
            df = pd.DataFrame(sub_data_dict)
            df.to_excel(f_w, sheet_name=sheet_name, index=False)