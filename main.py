import os
from datetime import date

from converters import read_word, read_excel
from tagging import build_ixbrl_body
from metadata import build_ixbrl_header
from validation import validate_financials, validate_ixbrl_basic

def main():
    base = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(base, "input")
    output_dir = os.path.join(base, "output")
    os.makedirs(output_dir, exist_ok=True)

    w = read_word(os.path.join(input_dir, "sample_word.docx"))
    e = read_excel(os.path.join(input_dir, "sample_excel.xlsx"))

    # html_lines = []
    # for i in w:
    #     html_lines.append(f'<p>{i}</p>')
    # for key, value in e.items():
    #     html_lines.append(f'<p>{key}: {value}<p>')

    # html_body = "\n".join(html_lines)
    # html_full = f"""
    # <html>
    #     <head>
    #         <title>10-K</title>
    #     </head>

    #     <body>
    #         {html_body}
    #     </body>
    # </html>
    # """

    # with open(os.path.join(output_dir, "html.html"), "w") as o: 
    #     o.write(html_full)

    body = build_ixbrl_body(w, e, date(2024,12,31), 'USD')
    header = build_ixbrl_header("0001234567", date(2024,12,31), 'USD')

    ixbrl_full = f"""
    <html
        xmlns="http://www.w3.org/1999/xhtml"
        xmlns:ix="http://www.xbrl.org/2013/inlineXBRL"
        xmlns:xbrli="http://www.xbrl.org/2003/instance"
        >
        <head>
            <title>10-K</title>
        </head>

        <body>
            {header}
            {body}
        </body>
    </html>
    """
    with open(os.path.join(output_dir, "10-k.html"), "w") as o: 
        o.write(ixbrl_full)

    errors = validate_financials(e) + validate_ixbrl_basic(ixbrl_full)
    with open(os.path.join(output_dir, "validation_check.txt"), "w") as r:
        r.write("Validation Check Pass!" if not errors else "\n".join(errors))

if __name__ == "__main__":
    main()
