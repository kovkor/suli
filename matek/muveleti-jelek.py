import random
import argparse
from fpdf import FPDF


def generate_operation(max_result, allowed_operations):
    """Generate a valid operation based on allowed operations and max result."""
    while True:
        a = random.randint(1, max_result)
        b = random.randint(1, max_result)
        op = random.choice(allowed_operations)
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            if b == 0 or a % b != 0:
                continue
            result = a / b
        if 0 <= result <= max_result:
            return a, op, b, result


def generate_problems(n, max_result, allowed_operations):
    """Generate n problems based on max result and allowed operations."""
    problems = []
    for _ in range(n):
        a, op, b, result = generate_operation(max_result, allowed_operations)
        problems.append(f"{a} __ {b} = {int(result)}")
    return problems


class PDF(FPDF):
    def header(self):
        self.set_font('FreeSans', '', 12)
        self.cell(0, 10, 'Válaszd ki a megfelelő műveleti jelet!', 0, 1, 'C')
        self.ln(10)


def create_pdf(problems, filename="muveleti-jelek.pdf"):
    """Create a PDF with the given problems in two columns."""
    pdf = PDF()
    pdf.add_font('FreeSans', '', 'fonts/freesans/FreeSans.ttf', uni=True)
    pdf.add_page()
    pdf.set_font('FreeSans', '', 12)

    # Define the number of problems per column
    problems_per_column = len(problems) // 2

    # Generate the columns
    col1 = problems[:problems_per_column]
    col2 = problems[problems_per_column:]

    # Add problems to PDF in two columns
    for i in range(problems_per_column):
        pdf.cell(90, 10, txt=col1[i], border=0)
        pdf.cell(90, 10, txt=col2[i], border=0)
        pdf.ln(10)

    pdf.output('generatedPdfs/'+filename)


def main():
    parser = argparse.ArgumentParser(description='Műveleti jeleket gyakorló PDF generálása')
    parser.add_argument('--max_result', type=int, default=20, help='Eredmények maximális összege.')
    parser.add_argument('--num_problems', type=int, default=50, help='Generálandó feladatok száma.')
    parser.add_argument('--operations', type=str, default='+,-,*,/', help='Lehetséges alapműveletek vesszővel elválasztva (+,-,*,/).')

    args = parser.parse_args()

    max_result = args.max_result
    num_problems = args.num_problems
    allowed_operations = args.operations.split(',')

    # Generate problems
    problems = generate_problems(num_problems, max_result, allowed_operations)

    # Create PDF
    create_pdf(problems)


if __name__ == "__main__":
    main()