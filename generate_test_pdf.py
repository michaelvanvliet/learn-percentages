# script to generate a test in PDF
import fpdf

# import libs
import numpy as np

# show answer yes/no
answers = True
question_type = "btw"

# number range
maxnum = 10
countnum = 15
numbers = np.random.randint(1, maxnum, size=countnum)

# set pdf properties
pdf = fpdf.FPDF(format="A4")
pdf.add_page()
pdf.set_font("Arial", size=12)

answers = []
for vraag, number in enumerate(numbers):
    pdf.set_font("Arial", "B", size=12)
    pdf.write(7, f"Vraag {vraag + 1}")
    pdf.ln()
    pdf.set_font("Arial", size=10)

    if question_type == "btw":
        # variables
        price = np.random.randint(1, maxnum, size=1)[0] * 10
        btw = np.random.randint(10, 50, size=1)[0]
        question_text = f"{price} euro + {btw}% B.T.W"

        pdf.write(
            5,
            f"De prijs van het product is: {price:.2f} Euro, wat kost het als er {btw}% B.T.W. bij komt? ({question_text})",
        )
        pdf.ln()

        # keep track of answers
        answer = (price / 100 * btw) + price
        answer_text = f"{question_text} = {answer:.2f} > "
        answer_text += (
            f"({price} / 100) x {btw} = {round((price/100) * btw,2)} Euro  >  "
        )
        answer_text += f"{price} + {round((price/100) * btw,2)} = {answer:.2f} Euro\n"
        answers.append(answer_text)

    # next exercise
    pdf.ln()

pdf.add_page()
pdf.set_font("Arial", "B", size=12)
pdf.write(10, "Antwoorden")
pdf.ln()
pdf.set_font("Arial", size=10)
for answer in answers:
    pdf.write(5, answer)
    pdf.ln()

# save to disk
pdf.output("test.pdf")
