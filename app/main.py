#generate pdf
from fpdf import FPDF
import datetime as dt

from data.clean_data import get_clean_data
from visualization.plot_data import plot_users

WIDTH = 210
HEIGHT = 297

def create_title(day, pdf):
    pdf.set_font('Arial', '', 24)  
    pdf.ln(60)
    pdf.write(5, f"Budget Analytics Report")
    pdf.ln(10)
    pdf.set_font('Arial', '', 16)
    pdf.write(4, f'{day}')
    pdf.ln(5)


def create_analytics_report(day,  filename = "report.pdf"):
    pdf = FPDF() # A4 (210 by 297 mm)
    
    '''First Page'''
    pdf.add_page()
    #pdf.image()
    create_title(day, pdf)


    pdf.output(filename, 'F')


if __name__ == '__main__':
    date = dt.date.today()
    plot_users()