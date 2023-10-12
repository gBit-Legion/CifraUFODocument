import convertapi
import pdf2docx

convertapi.api_secret = 'GsF3yw5vjYHRScRs'


class Converter():
    def __init__(self, file):
        self.file = file

    def pdf_to_doc(self):
        pass

    def pdf_to_docx(self):
        pass

    def pdf_to_txt(self):
        pass

    def pdf_to_odt(self):
        pass

    def pdf_to_rtf(self):
        pass

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

