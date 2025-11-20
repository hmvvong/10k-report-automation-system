# tagging ixbrl body

from datetime import date
from typing import List

def build_ixbrl_body(w, e, date: date, unit: str):
    y = date.year
    contextRef = f"FY{y}"
    unitRef = f"{unit}"
    lines: List[str] = []

    for i in w:
        name = None

        if i == '10-K':
            name = "dei:DocumentType"
        elif i == 'FOCUS UNIVERSAL INC.':
            name = "dei:EntityRegistrantName"
        else:
            lines.append(f"<p>{i}</p>")
            continue

        line = (
            f'<p><ix:nonNumeric '
            f'name="{name}" '
            f'contextRef="{contextRef}">'
            f'{i}'
            f'</ix:nonNumeric></p>'
        )
        lines.append(line)
        # 自动识别文字部分

    for key, value in e.items():
        line = (
            f'<p>{key}:<ix:nonFraction '
            f'name="us-gaap:{key}" '
            f'contextRef="{contextRef}" '
            f'unitRef="{unitRef}">'
            f'{value}'
            f'</ix:nonFraction></p>'
        )
        lines.append(line)
        # 自动识别表格部分

    return "\n".join(lines)