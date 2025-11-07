#!/usr/bin/env python3
"""
Export `report_SHL_GenAI.md` to a simple two-page PDF using ReportLab.

This script uses reportlab to create a plain PDF from the markdown content. It doesn't
render full markdown styling but preserves the text and basic headings. The goal is a
clean, 2-page PDF suitable for submission.

Usage:
  pip install reportlab
  python tools/export_report_pdf.py
"""
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MD = ROOT / 'report_SHL_GenAI.md'
OUT = ROOT / 'report_SHL_GenAI.pdf'

def split_lines(text, max_chars=100):
    # naive line splitter to avoid very long lines
    lines = []
    for raw in text.splitlines():
        while len(raw) > max_chars:
            # break at last space
            idx = raw.rfind(' ', 0, max_chars)
            if idx == -1:
                idx = max_chars
            lines.append(raw[:idx])
            raw = raw[idx:].lstrip()
        lines.append(raw)
    return lines

def main():
    if not MD.exists():
        print('report_SHL_GenAI.md not found')
        return
    text = MD.read_text(encoding='utf-8')
    lines = split_lines(text, max_chars=100)

    c = canvas.Canvas(str(OUT), pagesize=A4)
    width, height = A4
    margin = 50
    y = height - margin
    line_height = 14
    max_lines_per_page = int((height - 2*margin) / line_height)

    page = 1
    i = 0
    while i < len(lines) and page <= 2:
        y = height - margin
        c.setFont('Helvetica', 11)
        lines_on_page = 0
        while i < len(lines) and lines_on_page < max_lines_per_page:
            line = lines[i]
            # render headings bolder
            if line.startswith('# '):
                c.setFont('Helvetica-Bold', 14)
                c.drawString(margin, y, line[2:])
                c.setFont('Helvetica', 11)
            elif line.startswith('## '):
                c.setFont('Helvetica-Bold', 12)
                c.drawString(margin, y, line[3:])
                c.setFont('Helvetica', 11)
            else:
                c.drawString(margin, y, line)
            y -= line_height
            i += 1
            lines_on_page += 1
        c.showPage()
        page += 1

    c.save()
    print(f"✅ Wrote PDF to {OUT}")

if __name__ == '__main__':
    main()
