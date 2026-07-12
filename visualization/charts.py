import os
import matplotlib.pyplot as plt

def create_gc_chart(gc_content, at_content):
    print("GC chart function called")

    os.makedirs("charts", exist_ok=True)

    labels = ["GC Content", "AT Content"]
    values = [gc_content, at_content]

    plt.figure(figsize=(6, 4))
    plt.bar(labels, values)

    filename = "charts/gc_content.png"

    plt.savefig(filename)

    print("Saved at:", os.path.abspath(filename))
    print("File exists:", os.path.exists(filename))

    plt.close()

    return filename
def create_nucleotide_chart(a, t, g, c):
    os.makedirs("charts", exist_ok=True)

    labels = ["A", "T", "G", "C"]
    values = [a, t, g, c]

    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, autopct="%1.1f%%")

    plt.title("Nucleotide Composition")

    filename = "charts/nucleotide_composition.png"

    plt.savefig(filename)
    plt.close()

    return filename