#generate pdf
from fpdf import FPDF
import datetime as dt
from pathlib import Path

from data.clean_data import get_clean_data
from visualization.plot_types import plot_types_charts
from visualization.plot_users import plot_users_charts
from core.utils import create_folder
from core.config import TITLE_FONT_SIZE, SUBSUBTITLE_FONT_SIZE, SUBTITLE_FONT_SIZE

WIDTH = 210
HEIGHT = 297
#set height for 3 graphs per page
H1 = 70
H2 = 170

W1 = 5 #standard
#H3 =

def create_title(day, pdf):
    pdf.set_font('Arial', '', 24)  
    pdf.ln(30)
    pdf.write(5, f"Budget Analytics Report")
    pdf.ln(10)
    pdf.set_font('Arial', '', 16)
    pdf.write(4, f'{day}')
    pdf.ln(5)

def create_subtitle(text, y, pdf, font_size):
    pdf.set_font('Arial', '', font_size)
    pdf.ln(y)
    pdf.cell(200, 4, text, align='C')

def create_analytics_report(day, path, directories, filename = "budget_report.pdf"):
    pdf = FPDF() # A4 (210 by 297 mm)

    '''Presentation Page'''
    pdf.add_page()
    #pdf.image()
    create_title(day, pdf)
    
    '''First Page -- Last Month'''
    pdf.add_page()
    last_month = directories[0]#not the one
    create_subtitle(f"Budget for month {last_month}", 20, pdf, SUBTITLE_FONT_SIZE)
    create_subtitle(f"First Analysis: money spent per user", 25, pdf, SUBSUBTITLE_FONT_SIZE)
    #Gastos x usuario
    pdf.image(f"{path}/users/barcharts/{last_month}.jpg", W1, H1, WIDTH/2-10)
    pdf.image(f"{path}/users/piecharts/{last_month}.jpg", WIDTH/2, H1, WIDTH/2-10)
    #Gastos x tipo
    create_subtitle(f"Second Analysis: money spent per type", 100, pdf, SUBSUBTITLE_FONT_SIZE)
    pdf.image(f"{path}/types/barcharts/{last_month}.jpg", W1, H2, WIDTH/2-10)
    pdf.image(f"{path}/types/piecharts/{last_month}.jpg", WIDTH/2, H2, WIDTH/2-10)

    '''Second page'''
    pdf.add_page()
    create_subtitle("Third Analysis: difference between months", 20, pdf, SUBTITLE_FONT_SIZE)



    file_path = path / filename
    pdf.output(file_path, 'F')


if __name__ == '__main__':
    today = dt.date.today()
    path = create_folder()  

    directories = plot_users_charts(path)
    #directories2
    plot_types_charts(path)
    create_analytics_report(today, path, directories)