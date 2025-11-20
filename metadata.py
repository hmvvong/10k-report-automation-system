# metadata.py
from datetime import date

def build_ixbrl_header(cik: str, end_of_year: date, unit: str) -> str:
    year = end_of_year.year
    start_of_year = date(year, 1, 1)

    return f"""
<div style="display:none">
  <ix:header>
    <link:schemaRef xlink:href="demo_taxonomy.xsd"/>

    <xbrli:context id="FY{year}">
      <xbrli:entity>
        <xbrli:identifier scheme="http://www.sec.gov/CIK">{cik}</xbrli:identifier>
      </xbrli:entity>
      <xbrli:period>
        <xbrli:startDate>{start_of_year}</xbrli:startDate>
        <xbrli:endDate>{end_of_year}</xbrli:endDate>
      </xbrli:period>
    </xbrli:context>

    <xbrli:unit id="{unit}">
      <xbrli:measure>iso4217:{unit}</xbrli:measure>
    </xbrli:unit>
  </ix:header>
</div>
"""