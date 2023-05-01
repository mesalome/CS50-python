from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 16)
        self.cell(200, 20, "CS50 Shirtificate", align="C")
        self.ln(20)

def main():
    userInput = input("What is the graduate's name?: ")
    pdf = PDF()
    pdf.add_page()
    pdf.image("shirtificate.png", x=20, y=60, w=180, h=280)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", "B", 20)
    pdf.cell(190, 180, f"{userInput} took CS50", align="C")
    pdf.output("shirtificate.pdf")

if __name__=="__main__":
    main()