# Пример !!!


from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT


class VacationReportGenerator:
    def __init__(self):
        self.doc = Document()
        self.doc.add_heading('Рапорт на отпуск', level=1)

    def set_font_size(self, size):
        self.doc.styles['Normal'].font.size = Pt(size)

    def set_paragraph_spacing(self, before=None, after=None):
        for paragraph in self.doc.paragraphs:
            paragraph.paragraph_format.space_before = Inches(before) if before else None
            paragraph.paragraph_format.space_after = Inches(after) if after else None

    def set_paragraph_alignment(self, alignment):
        if alignment == 'left':
            self.doc.styles['Normal'].paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT
        elif alignment == 'right':
            self.doc.styles['Normal'].paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT
        elif alignment == 'center':
            self.doc.styles['Normal'].paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

    def set_line_spacing(self, value):
        self.doc.styles['Normal'].paragraph_format.space_between = Pt(value)

    def set_page_margins(self, top=None, bottom=None, left=None, right=None):
        if top is not None:
            self.doc.sections[0].top_margin = Inches(top)
        if bottom is not None:
            self.doc.sections[0].bottom_margin = Inches(bottom)
        if left is not None:
            self.doc.sections[0].left_margin = Inches(left)
        if right is not None:
            self.doc.sections[0].right_margin = Inches(right)

    def add_section(self, title, text):
        self.doc.add_heading(title, level=2)
        paragraph = self.doc.add_paragraph(text)
        run = paragraph.runs[0]
        run.bold = True

    def add_information(self, employee_name, department, vacation_start, vacation_end, reason):
        self.doc.add_heading('Информация', level=2)
        table = self.doc.add_table(rows=5, cols=2)
        table.style = 'Table Grid'

        cells = table.rows[0].cells
        cells[0].text = 'Сотрудник'
        cells[1].text = employee_name

        cells = table.rows[1].cells
        cells[0].text = 'Отдел'
        cells[1].text = department

        cells = table.rows[2].cells
        cells[0].text = 'Период отпуска'
        cells[1].text = f'{vacation_start} - {vacation_end}'

        cells = table.rows[3].cells
        cells[0].text = 'Причина отпуска'
        cells[1].text = reason

    def add_list(self, items):
        self.doc.add_heading('Список дел', level=2)
        for item in items:
            p = self.doc.add_paragraph()
            p.add_run(u'\u2022').bold = True  
            p.add_run(' ' + item)

    def save_report(self, filename):
        self.doc.save(filename)


#  использование класса VacationReportGenerator. Пример !!!
report_generator = VacationReportGenerator()
report_generator.set_font_size(12)
report_generator.set_paragraph_spacing(before=0.5, after=0.5)
report_generator.set_paragraph_alignment('left')
report_generator.set_line_spacing(1.5)
report_generator.set_page_margins(top=1, bottom=1, left=1, right=1)

report_generator.add_section('Важное сообщение', 'Прошу рассмотреть мою заявку на отпуск.')
report_generator.add_information('Иванов Иван Иванович', 'Отдел продаж', '01.11.2023', '15.11.2023',
                                'Необходим отдых для восстановления энергии.')

tasks = ['Закончить проект', 'Подготовить отчет', 'Вернуться в указанное время']
report_generator.add_list(tasks)

report_generator.save_report('рапорт_на_отпуск.docx')