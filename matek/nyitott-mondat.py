import random
import argparse
from fpdf import FPDF

def generate_open_statement(max_result, max_valid_numbers):
    symbols = ['◆', '◇', '◉', '●', '◯', '★', '✦', '✧', '☀', '☼']  # Add your desired symbols here
    chosen_symbol = random.choice(symbols)
    """Generate a valid open statement with an inequality."""
    while True:
        a1 = random.randint(1, max_result)
        b1 = random.randint(1, max_result)
        op1 = random.choice(['+', '-'])
        if op1 == '+':
            left_result = a1 + b1
        elif op1 == '-':
            if a1 < b1:
                continue
            left_result = a1 - b1

        if left_result > max_result:
            continue

        a2 = random.randint(1, max_result)
        b2 = random.randint(1, max_result)
        op2 = random.choice(['+', '-'])
        if op2 == '+':
            right_result = a2 + b2
        elif op2 == '-':
            if a2 < b2:
                continue
            right_result = a2 - b2

        if right_result > max_result:
            continue

        constant = random.randint(1, max_result - 1)
        if right_result - constant <= left_result:
            continue

        relation = random.choice(['<', '>'])

        if relation == '<' and left_result < right_result - constant:
            valid_numbers = [x for x in range(left_result + 1, right_result - constant)]
            if 0 < len(valid_numbers) <= max_valid_numbers:
                return f"{a1} {op1} {b1} < {chosen_symbol} + {constant} < {a2} {op2} {b2}", valid_numbers
        elif relation == '>' and left_result > right_result + constant:
            valid_numbers = [x for x in range(right_result + constant + 1, left_result)]
            if 0 < len(valid_numbers) <= max_valid_numbers:
                return f"{a1} {op1} {b1} > {chosen_symbol} + {constant} > {a2} {op2} {b2}", valid_numbers

def generate_problems(n, max_result, max_valid_numbers):
    """Generate n problems based on max result."""
    problems = []
    for _ in range(n):
        statement, valid_numbers = generate_open_statement(max_result, max_valid_numbers)
        problems.append((statement, valid_numbers))
    return problems

class PDF(FPDF):
    def header(self):
        self.set_font('FreeSans', '', 12)
        self.cell(0, 10, 'Nyitott mondatok', 0, 1, 'C')
        self.ln(10)

def create_pdf(problems, filename="nyitott-mondat.pdf"):
    """Create a PDF with the given problems in two columns."""
    # Register the FreeSans font
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
        pdf.cell(90, 10, txt=col1[i][0], border=0)
        pdf.cell(90, 10, txt=col2[i][0], border=0)
        pdf.ln(25)

    pdf.output('generatedPdfs/' + filename)

def main():
    parser = argparse.ArgumentParser(description='Nyitott mondatokat gyakorló PDF generálása')
    parser.add_argument('--max_result', type=int, default=20, help='A részeredmények maximális összege.')
    parser.add_argument('--num_problems', type=int, default=50, help='Generálandó feladatok száma.')
    parser.add_argument('--max_valid_numbers', type=int, default=4, help='Helyes eredmények maximális száma.')

    args = parser.parse_args()

    max_result = args.max_result
    num_problems = args.num_problems
    max_valid_numbers = args.max_valid_numbers

    # Generate problems
    problems = generate_problems(num_problems, max_result, max_valid_numbers)

    # Create PDF
    create_pdf(problems)

    # Optionally, print solutions for reference
    print("Megoldások:")
    for statement, valid_numbers in problems:
        print(f"{statement}: {valid_numbers}")

if __name__ == "__main__":
    main()