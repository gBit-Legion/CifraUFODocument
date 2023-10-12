import convertapi
import aspose.words as aw
from pathlib import Path

convertapi.api_secret = 'GsF3yw5vjYHRScRs'


class Converter():
    def __init__(self, file):
        self.file = file

    def pdf_to_doc(self):
        doc = aw.Document(self.file)
        doc.save('save/' + self.file.rsplit(".", 1)[0] + '.doc')

    def pdf_to_docx(self):
        doc = aw.Document(self.file)
        doc.save('save/' + self.file.rsplit(".", 1)[0] + '.docx')

    def pdf_to_txt(self):
        doc = aw.Document(self.file)
        doc.save('save/' + self.file.rsplit(".", 1)[0] + '.txt')

    def pdf_to_odt(self):
        doc = aw.Document(self.file)
        doc.save('save/' + self.file.rsplit(".", 1)[0] + '.odt')

    def pdf_to_rtf(self):
        doc = aw.Document(self.file)
        doc.save('save/' + self.file.rsplit(".", 1)[0] + '.rtf')

    def doc_to_pdf(self):
        convertapi.convert('pdf',
                           {'File': self.file},
                           from_format='doc').save_files('save')

    def doc_to_docx(self):
        convertapi.convert('docx',
                           {'File': self.file},
                           from_format='doc').save_files('save')

    def doc_to_odt(self):
        convertapi.convert('odt',
                           {'File': self.file},
                           from_format='doc').save_files('save')

    def doc_to_txt(self):
        convertapi.convert('txt',
                           {'File': self.file},
                           from_format='doc').save_files('save')

    def doc_to_rtf(self):
        convertapi.convert('rtf',
                           {'File': self.file},
                           from_format='doc').save_files('save')

    def docx_to_doc(self):
        convertapi.convert('doc',
                           {'File': self.file},
                           from_format='docx').save_files('save')

    def docx_to_odt(self):
        convertapi.convert('odt',
                           {'File': self.file},
                           from_format='docx').save_files('save')

    def docx_to_pdf(self):
        convertapi.convert('pdf',
                           {'File': self.file},
                           from_format='docx').save_files('save')

    def docx_to_rtf(self):
        convertapi.convert('rtf',
                           {'File': self.file},
                           from_format='docx').save_files('save')

    def docx_to_txt(self):
        convertapi.convert('txt',
                           {'File': self.file},
                           from_format='docx').save_files('save')

    def odt_to_doc(self):
        convertapi.convert('doc',
                           {'File': self.file},
                           from_format='odt').save_files('save')

    def odt_to_docx(self):
        convertapi.convert('docx',
                           {'File': self.file},
                           from_format='odt').save_files('save')

    def odt_to_pdf(self):
        convertapi.convert('pdf',
                           {'File': self.file},
                           from_format='odt').save_files('save')

    def odt_to_rtf(self):
        convertapi.convert('rtf',
                           {'File': self.file},
                           from_format='odt').save_files('save')

    def odt_to_txt(self):
        convertapi.convert('txt',
                           {'File': self.file},
                           from_format='odt').save_files('save')

    def rtf_to_doc(self):
        convertapi.convert('doc',
                           {'File': self.file},
                           from_format='rtf').save_files('save')

    def rtf_to_docx(self):
        convertapi.convert('docx',
                           {'File': self.file},
                           from_format='rtf').save_files('save')

    def rtf_to_odt(self):
        convertapi.convert('odt',
                           {'File': self.file},
                           from_format='rtf').save_files('save')

    def rtf_to_pdf(self):
        convertapi.convert('pdf',
                           {'File': self.file},
                           from_format='rtf').save_files('save')

    def rtf_to_txt(self):
        convertapi.convert('txt',
                           {'File': self.file},
                           from_format='rtf').save_files('save')

    def txt_to_pdf(self):
        convertapi.convert('pdf',
                           {'File': self.file},
                           from_format='txt').save_files('save')

    def txt_to_doc(self):
        convertapi.convert('doc',
                           {'File': self.file},
                           from_format='txt').save_files('save')

    def txt_to_docx(self):
        convertapi.convert('docx',
                           {'File': self.file},
                           from_format='txt').save_files('save')

    def txt_to_odt(self):
        convertapi.convert('odt',
                           {'File': self.file},
                           from_format='txt').save_files('save')

    def txt_to_rtf(self):
        convertapi.convert('rtf',
                           {'File': self.file},
                           from_format='txt').save_files('save')



