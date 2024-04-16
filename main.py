import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import networkx as nx

def validate_string():
    input_string = entry_string.get().lower()
    if input_string.startswith('ac') or input_string.endswith('ab'):
        if set(input_string[:-2]).issubset({'a', 'b', 'c'}):
            result_label.config(text="Cadena válida", foreground='green')
            generate_diagram(input_string)
        else:
            result_label.config(text="La cadena solo debe contener las letras a, b y c", foreground='red')
    else:
        result_label.config(text="La cadena debe empezar con 'ac' o terminar con 'ab'", foreground='red')

def generate_diagram(input_string):
    G = nx.DiGraph()

    states = []
    for i in range(len(input_string) + 1):
        states.append('q{}'.format(i))
    G.add_nodes_from(states)

    for i, char in enumerate(input_string):
        G.add_edge('q{}'.format(i), 'q{}'.format(i + 1), label=char)

    pos = nx.spring_layout(G, seed=42)
    pos = {k: (v[1], -v[0]) for k, v in pos.items()}
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue', edgecolors='black')
    nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, arrowsize=20)
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.title("Autómata")
    plt.axis('off')
    plt.show()

window = tk.Tk()
window.title("Validador de Cadenas")

window_width = 500
window_height = 300

pos_x = (window.winfo_screenwidth() // 2) - (window_width // 2)
pos_y = (window.winfo_screenheight() // 2) - (window_height // 2)
window.geometry('{}x{}+{}+{}'.format(window_width, window_height, pos_x, pos_y))

title_label = ttk.Label(window, text="Ingresa una cadena:", font=("Helvetica", 12))
title_label.pack(pady=(50, 10), anchor='center')

entry_string = tk.Entry(window, font=("Helvetica", 12))
entry_string.pack(pady=5, anchor='center')

validate_button = ttk.Button(window, text="Validar Cadena", command=validate_string)
validate_button.pack(pady=5, anchor='center')

result_label = ttk.Label(window, text="", font=("Helvetica", 12))
result_label.pack(pady=5, anchor='center')

window.mainloop()
