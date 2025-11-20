# 读word，excel
# 转为dict

from typing import Dict
import pandas as pd
from docx import Document

def read_word(wordPath: str) -> Dict[str, str]:
    word = Document(wordPath)
    paragraphs = [p.text.strip() for p in word.paragraphs]

    return paragraphs

    # output = {10-K, FOCUS UNIVERSAL INC., ... 所有文字段汇总}

def read_excel(excelPath: str) -> Dict[str, float]:
    income_sheet = pd.read_excel(excelPath, sheet_name="IncomeStatement")
    balance_sheet = pd.read_excel(excelPath, sheet_name="BalanceSheet")

    def excel_to_dict(sheet):
        return {str(r["Item"]): float(r["Value"]) for _, r in sheet.iterrows()}

    income = excel_to_dict(income_sheet)
    balance = excel_to_dict(balance_sheet)

    return {**income, **balance}

    # output = {"Revenues": 5000000, "Assets": 8000000, ... 所有excel里的key-value pair汇总 }


