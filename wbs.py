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


def add_nodes_edges(graph, parent_id, structure, max_width, current_depth, max_depth):
    """
    Recursively traverse the nested dictionary 'structure' and add nodes/edges
    to the Graphviz Digraph, wrapping text to a specified max_width.
    Traversal stops once the current depth reaches max_depth.
    The top-level node is considered at depth 1.
    """
    for task_name, sub_tasks in structure.items():
        wrapped_label = wrap_text(task_name, max_width)
        # Incorporate current_depth into the node id to reduce potential hash collisions
        current_id = str(hash(task_name + str(current_depth)))
        graph.node(current_id, wrapped_label)
        if parent_id is not None:
            graph.edge(parent_id, current_id)
        if isinstance(sub_tasks, dict) and sub_tasks and (current_depth < max_depth):
            add_nodes_edges(
                graph, current_id, sub_tasks, max_width, current_depth + 1, max_depth
            )


def generate_wbs_graph(
    wbs_dict,
    top_task=None,
    output_filename="wbs_graph",
    max_width=15,
    max_depth=float("inf"),
):
    """
    Generate a top-down (TB) graph from a nested dictionary describing the WBS.
    If 'top_task' (e.g., 'Development/Software') is provided, only generate the
    graph for that path's sub-dictionary.
    The graph will only display nodes up to 'max_depth' levels deep (with the top node at depth 1).
    """
    if top_task:
        sub_dict = find_subdictionary(wbs_dict, top_task)
        if not sub_dict:
            raise ValueError(f"Path '{top_task}' not found in the WBS.")
        wbs_dict = sub_dict

    dot = Digraph("WBS", format="png")
    dot.attr("graph", rankdir="TB", ranksep="1.5", nodesep="0.3")

    add_nodes_edges(
        dot, None, wbs_dict, max_width, current_depth=1, max_depth=max_depth
    )
    dot.render(output_filename, view=False)


if __name__ == "__main__":
    # Example: generate only the 'T.A.I.L.S' portion of the WBS up to 3 levels deep.
    generate_wbs_graph(
        wbs_structure,
        top_task="T.A.I.L.S/Development/Hardware",
        max_width=20,
        max_depth=3,
    )
