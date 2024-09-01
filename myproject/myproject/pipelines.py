from fpdf import FPDF

class PdfPipeline:

    def open_spider(self, spider):
        # Initialize the PDF
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=12)

    def close_spider(self, spider):
        # Save the PDF
        self.pdf.output("scraped_content.pdf")

    def process_item(self, item, spider):
        # Add the URL as a header
        self.pdf.set_font("Arial", style='B', size=12)
        self.pdf.cell(200, 10, txt=item['url'], ln=True, align='L')

        # Add the text content
        self.pdf.set_font("Arial", size=12)
        self.pdf.multi_cell(0, 10, item['text'])

        return item
