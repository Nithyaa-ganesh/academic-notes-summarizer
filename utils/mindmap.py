from graphviz import Digraph
import os

def generate_mindmap(summary_text, output_file="mindmap"):
    dot = Digraph(comment="Mindmap")

    # ✅ Layout & size enhancements
    dot.attr(rankdir='LR')            # Left-to-Right layout (better width usage)
    dot.attr(size='12,8')             # Graph size in inches
    dot.attr(dpi='200')               # Higher image resolution for clarity

    # ✅ Styling for nodes
    dot.attr('node', shape='box', style='filled', fillcolor='lightyellow', fontname='Arial', fontsize='12')

    # ✅ Root node
    dot.node("Summary", "Summary")

    # ✅ Add points as nodes and edges
    lines = [line.strip("-• ") for line in summary_text.strip().split("\n") if line.strip()]
    for i, point in enumerate(lines):
        node_id = f"P{i}"
        dot.node(node_id, point)
        dot.edge("Summary", node_id)

    # ✅ Output path
    os.makedirs("downloads", exist_ok=True)  # Make sure folder exists
    file_path = os.path.join("downloads", output_file)
    dot.render(file_path, format="png", cleanup=True)

    return file_path + ".png"
