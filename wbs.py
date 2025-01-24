from graphviz import Digraph
from wbs_items import wbs_structure

def add_nodes_edges(graph, parent_id, structure):
    """
    Recursively traverse the nested dictionary 'structure' and add nodes/edges to the Graphviz Digraph.
    """
    for task_name, sub_tasks in structure.items():
        current_id = str(hash(task_name))  # Create a unique ID for each node
        graph.node(current_id, task_name)
        if parent_id is not None:
            graph.edge(parent_id, current_id)
        # If there are sub tasks, recurse
        if isinstance(sub_tasks, dict) and sub_tasks:
            add_nodes_edges(graph, current_id, sub_tasks)

def generate_wbs_graph(wbs_dict, output_filename='wbs_graph'):
    """
    Generate a top-down (TB) graph from a nested dictionary describing the WBS.
    """
    dot = Digraph('WBS', format='png')
    dot.attr(rankdir='TB')  # top to bottom layout

    # Each top-level entry has no parent, so parent_id = None
    add_nodes_edges(dot, None, wbs_dict)

    dot.render(output_filename, view=False)

if __name__ == "__main__":
    # Example WBS structure
    # Replace this dictionary with your own nested tasks.

    generate_wbs_graph(wbs_structure)
