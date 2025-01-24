from graphviz import Digraph
from wbs_items import wbs_structure


def wrap_text(text, max_width):
    """
    Wraps the given text to a specified max_width by inserting newlines
    at space boundaries.
    """
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        if (len(current_line) + len(word) + 1) <= max_width:
            if current_line:
                current_line += " "
            current_line += word
        else:
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    return "\n".join(lines)


def find_subdictionary(structure, path):
    """
    Takes a slash-delimited path (e.g., 'Development/Software') and returns
    that sub-dictionary if it exists, otherwise returns None.
    """
    keys = path.split("/")
    sub_dict = structure
    for key in keys:
        if isinstance(sub_dict, dict) and key in sub_dict:
            sub_dict = sub_dict[key]
        else:
            return None
    return {keys[-1]: sub_dict}


def add_nodes_edges(graph, parent_id, structure, max_width):
    """
    Recursively traverse the nested dictionary 'structure' and add nodes/edges
    to the Graphviz Digraph, wrapping text to a specified max_width.
    """
    for task_name, sub_tasks in structure.items():
        wrapped_label = wrap_text(task_name, max_width)
        current_id = str(hash(task_name))
        graph.node(current_id, wrapped_label)
        if parent_id is not None:
            graph.edge(parent_id, current_id)
        if isinstance(sub_tasks, dict) and sub_tasks:
            add_nodes_edges(graph, current_id, sub_tasks, max_width)


def generate_wbs_graph(
    wbs_dict, top_task=None, output_filename="wbs_graph", max_width=15
):
    """
    Generate a top-down (TB) graph from a nested dictionary describing the WBS.
    If 'top_task' (e.g., 'Development/Software') is provided, only generate the
    graph for that path's sub-dictionary.
    """
    if top_task:
        sub_dict = find_subdictionary(wbs_dict, top_task)
        if not sub_dict:
            raise ValueError(f"Path '{top_task}' not found in the WBS.")
        wbs_dict = sub_dict

    dot = Digraph("WBS", format="png")
    dot.attr("graph", rankdir="TB", splines="ortho", ranksep="1.5", nodesep="0.3")

    add_nodes_edges(dot, None, wbs_dict, max_width)
    dot.render(output_filename, view=False)


if __name__ == "__main__":
    # Example: generate only the 'Development/Software' portion of the WBS.
    generate_wbs_graph(wbs_structure, top_task="T.A.I.L.S/Design", max_width=20)
