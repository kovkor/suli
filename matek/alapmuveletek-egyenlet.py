import random
import argparse
from fpdf import FPDF


def generate_operation(max_result, allowed_operations):
    """Generate a valid operation and missing term position based on allowed operations and max result."""
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
            break

    pos = random.choice(['a', 'b', 'result'])
    if pos == 'a':
        equation = f"__ {op} {b} = {int(result)}"
        solution = a
    elif pos == 'b':
        equation = f"{a} {op} __ = {int(result)}"
        solution = b
    else:
        equation = f"{a} {op} {b} = __"
        solution = int(result)

    return equation, solution


def generate_problems(n, max_result, allowed_operations):
    """Generate n problems based on max result and allowed operations."""
    problems = []
    solutions = []
    for _ in range(n):
        equation, solution = generate_operation(max_result, allowed_operations)
        problems.append(equation)
        solutions.append(solution)
    return problems, solutions


class PDF(FPDF):
    def header(self):
        self.set_font('FreeSans', '', 12)
        self.cell(0, 10, 'Írd be a hiányzó számokat!', 0, 1, 'C')
        self.ln(10)


def create_pdf(problems, filename="alapmuveletek-egyenlet.pdf"):
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
    parser = argparse.ArgumentParser(description='Generate math problems PDF.')
    parser.add_argument('--max_result', type=int, default=20, help='Maximum result of the operations.')
    parser.add_argument('--num_problems', type=int, default=50, help='Number of problems to generate.')
    parser.add_argument('--operations', type=str, default='+,-,*,/', help='Allowed operations separated by commas.')

    args = parser.parse_args()

    max_result = args.max_result
    num_problems = args.num_problems
    allowed_operations = args.operations.split(',')

    # Generate problems
    problems, solutions = generate_problems(num_problems, max_result, allowed_operations)

    # Create PDF
    create_pdf(problems)

    # Optionally, print solutions for reference
    print("Solutions:")
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()