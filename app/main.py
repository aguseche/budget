#generate pdf
from fpdf import FPDF
import datetime as dt
from pathlib import Path

from data.clean_data import get_clean_data
from visualization.plot_types import plot_types_charts
from visualization.plot_users import plot_users_charts
from core.utils import create_folder

WIDTH = 210
HEIGHT = 297
#set height for 3 graphs per page
H1 = 50
H2 = 170
#H3 =

def create_title(day, pdf):
    pdf.set_font('Arial', '', 24)  
    pdf.ln(30)
    pdf.write(5, f"Budget Analytics Report")
    pdf.ln(10)
    pdf.set_font('Arial', '', 16)
    pdf.write(4, f'{day}')
    pdf.ln(5)

def create_subtitle(text, pdf, y):
    pdf.set_font('Arial', '', 20)
    pdf.ln(y)
    pdf.cell(200, 4, text, align='C')

def create_analytics_report(day, path, filename = "report.pdf"):
    pdf = FPDF() # A4 (210 by 297 mm)

    '''First Page'''
    pdf.add_page()
    #pdf.image()
    create_title(day, pdf)
    
    '''Second Page'''
    pdf.add_page()
    create_subtitle("First Analysis: money spent per user", pdf, 20)
    pdf.image("./results/users_barchart.jpg", 5, H1, WIDTH/2-10)
    pdf.image("./results/users_piechart.jpg", WIDTH/2, H1, WIDTH/2-10)

    create_subtitle("Second Analysis: money spent per type", pdf, 120)
    pdf.image("./results/types_barchart.jpg", 5, H2, WIDTH/2-10)
    pdf.image("./results/types_piechart.jpg", WIDTH/2, H2, WIDTH/2-10)

    '''Third Page'''
    pdf.add_page()
    create_subtitle("Third Analysis: difference between months", pdf, 20)
    file_path = path / filename
    pdf.output(file_path, 'F')


if __name__ == '__main__':
    today = dt.date.today()
    path = create_folder()  

    plot_users_charts(path)
    plot_types_charts(path)

    create_analytics_report(today, path)