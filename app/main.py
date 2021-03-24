#generate pdf
from fpdf import FPDF
import datetime as dt

from data.clean_data import get_clean_data
from visualization.plot_charts import plot_charts


WIDTH = 210
HEIGHT = 297

def create_title(day, pdf):
    pdf.set_font('Arial', '', 24)  
    pdf.ln(30)
    pdf.write(5, f"Budget Analytics Report")
    pdf.ln(10)
    pdf.set_font('Arial', '', 16)
    pdf.write(4, f'{day}')
    pdf.ln(5)

def create_subtitle(text, pdf, x):
    pdf.set_font('Arial', '', 20)
    pdf.ln(x)
    pdf.cell(200, 4, text, align='C')

def create_analytics_report(day,  filename = "report.pdf"):
    pdf = FPDF() # A4 (210 by 297 mm)
    
    '''First Page'''
    pdf.add_page()
    #pdf.image()
    create_title(day, pdf)
    
    '''Second Page'''
    pdf.add_page()
    plot_charts()
    create_subtitle("First Analysis: money spent per user", pdf, 20)
    pdf.image("./results/users_barchart.jpg", 5, 50, WIDTH/2-10)
    pdf.image("./results/users_piechart.jpg", WIDTH/2, 50, WIDTH/2-10)

    create_subtitle("Second Analysis: money spent per type", pdf, 120)
    pdf.image("./results/types_barchart.jpg", 5, 170, WIDTH/2-10)
    pdf.image("./results/types_piechart.jpg", WIDTH/2, 170, WIDTH/2-10)


    pdf.output(filename, 'F')


if __name__ == '__main__':
    today = dt.date.today()
    create_analytics_report(today)