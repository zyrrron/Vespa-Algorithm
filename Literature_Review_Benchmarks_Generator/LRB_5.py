import matplotlib.pyplot as plt
import networkx as nx
import os
from networkx.drawing.nx_pydot import write_dot

g_flow = nx.DiGraph()
g_control = nx.DiGraph()

flow_node_list = []
for i in range(25):
    ss = f"f{i+1}"
    flow_node_list.append(ss)
for i in range(51):
    ss = f"fo{i+1}"
    flow_node_list.append(ss)

control_node_list = []
for i in range(16):
    ss = f"c{i+1}"
    control_node_list.append(ss)
for i in range(66):
    ss = f"v{i+1}"
    control_node_list.append(ss)
for i in range(4):
    ss = f"co{i+1}"
    control_node_list.append(ss)

flow_edge_list = [("f1", "fo1", 2), ("f2", "fo2", 2), ("f3", "fo3", 2), ("f4", "fo4", 2), ("f5", "fo5", 2),
                  ("f6", "fo6", 2), ("f7", "fo7", 2), ("f8", "fo8", 2), ("f9", "fo9", 2), ("f10", "fo10", 2),
                  ("f11", "fo11", 2), ("f12", "fo12", 2), ("f13", "fo13", 2), ("f14", "fo14", 2), ("f15", "fo15", 2),
                  ("f16", "fo16", 2), ("f17", "fo17", 2), ("fo2", "fo1", 2), ("fo3", "fo2", 2), ("fo3", "fo4", 2),
                  ("fo4", "fo5", 2), ("fo5", "fo6", 2), ("fo6", "fo7", 2), ("fo7", "fo8", 2), ("fo8", "fo9", 2),
                  ("fo1", "fo40", 20), ("fo9", "fo41", 20), ("fo40", "fo18", 20), ("fo19", "fo41", 20), ("fo18", "fo23", 2),
                  ("fo19", "fo25", 2), ("fo5", "fo22", 2), ("fo23", "fo32", 2), ("fo23", "fo24", 2), ("fo24", "fo33", 2),
                  ("fo25", "fo26", 2), ("fo25", "fo34", 2), ("fo26", "fo35", 2), ("fo24", "fo22", 2), ("fo26", "fo22", 2),
                  ("fo22", "fo27", 2), ("fo27", "fo28", 2), ("fo28", "fo29", 2), ("fo28", "fo36", 2), ("fo29", "fo37", 2),
                  ("fo27", "fo30", 2), ("fo30", "fo38", 2), ("fo30", "fo31", 2), ("fo31", "fo39", 2), ("fo27", "fo14", 2),
                  ("fo10", "fo11", 2), ("fo11", "fo12", 2), ("fo12", "fo13", 2), ("fo13", "fo14", 2), ("fo14", "fo15", 2),
                  ("fo15", "fo16", 2), ("fo16", "fo17", 2), ("fo10", "fo42", 20), ("fo17", "fo43", 20), ("fo20", "fo42", 20),
                  ("fo21", "fo43", 20), ("fo21", "fo31", 2), ("fo20", "fo29", 2), ("f18", "fo48", 2), ("f19", "fo49", 2),
                  ("f20", "fo45", 2), ("f21", "fo44", 2), ("f22", "fo46", 2), ("f23", "fo47", 2), ("f24", "fo51", 2), ("f25", "fo50", 2),
                  ("fo32", "fo44", 2), ("fo33", "fo45", 2), ("fo34", "fo46", 2), ("fo35", "fo47", 2), ("fo36", "fo48", 2), ("fo37", "fo49", 2),
                  ("fo38", "fo50", 2), ("fo39", "fo51", 2)]

control_edge_list = [("v1", "c3", 1), ("v2", "c3", 1), ("v3", "c3", 1), ("v4", "c3", 1), ("v28", "c3", 1), ("v29", "c3", 1),
                     ("v30", "c3", 1), ("v31", "c3", 1), ("v9", "c4", 1), ("v10", "c4", 1), ("v11", "c4", 1), ("v12", "c4", 1),
                     ("v36", "c4", 1), ("v37", "c4", 1), ("v38", "c4", 1), ("v39", "c4", 1), ("v26", "c5", 1), ("v40", "c5", 1),
                     ("v25", "c9", 1), ("v54", "c9", 1), ("v59", "c9", 1), ("v60", "c9", 1), ("v61", "c9", 1), ("v62", "c9", 1),
                     ("v13", "c14", 1), ("v14", "c14", 1), ("v15", "c14", 1), ("v16", "c14", 1), ("v41", "c14", 1), ("v42", "c14", 1),
                     ("v43", "c14", 1), ("v44", "c14", 1), ("v5", "c13", 1), ("v6", "c13", 1), ("v7", "c13", 1), ("v8", "c13", 1),
                     ("v32", "c13", 1), ("v33", "c13", 1), ("v34", "c13", 1), ("v35", "c13", 1), ("v27", "c6", 1), ("v53", "c6", 1),
                     ("v17", "c15", 1), ("v18", "c15", 1), ("v19", "c15", 1), ("v20", "c15", 1), ("v45", "c15", 1), ("v46", "c15", 1),
                     ("v47", "c15", 1), ("v48", "c15", 1), ("v21", "c16", 1), ("v22", "c16", 1), ("v23", "c16", 1), ("v24", "c16", 1),
                     ("v49", "c16", 1), ("v50", "c16", 1), ("v51", "c16", 1), ("v52", "c16", 1), ("v55", "c2", 1), ("v64", "c2", 1),
                     ("v56", "c1", 1), ("v63", "c1", 1), ("v58", "c7", 1), ("v65", "c7", 1), ("v57", "c8", 1), ("v66", "c8", 1),
                     ("co1", "c10", 1), ("co2", "c10", 1), ("co3", "c10", 1), ("co4", "c10", 1),
                     ("co1", "c11", 1), ("co2", "c11", 1), ("co3", "c11", 1), ("co4", "c11", 1),
                     ("co1", "c12", 1), ("co2", "c12", 1), ("co3", "c12", 1), ("co4", "c12", 1),
                     ("v1", "v2", 1), ("v2", "v3", 1), ("v3", "v4", 1), ("v4", "v1", 1), ("v28", "v29", 1), ("v29", "v30", 1),
                     ("v30", "v31", 1), ("v31", "v28", 1), ("v9", "v10", 1), ("v10", "v11", 1), ("v11", "v12", 1), ("v12", "v9", 1),
                     ("v36", "v37", 1), ("v37", "v38", 1), ("v38", "v39", 1), ("v39", "v36", 1),
                     ("v13", "v14", 1), ("v14", "v15", 1), ("v15", "v16", 1), ("v16", "v13", 1), ("v41", "v42", 1), ("v42", "v43", 1),
                     ("v43", "v44", 1), ("v44", "v41", 1), ("v5", "v6", 1), ("v6", "v7", 1), ("v7", "v8", 1), ("v8", "v5", 1),
                     ("v32", "v33", 1), ("v33", "v34", 1), ("v34", "v35", 1), ("v35", "v33", 1),
                     ("v17", "v18", 1), ("v18", "v19", 1), ("v19", "v20", 1), ("v20", "v17", 1), ("v45", "v46", 1),
                     ("v46", "v47", 1), ("v47", "v48", 1), ("v48", "v45", 1), ("v21", "v22", 1), ("v22", "v23", 1),
                     ("v23", "v24", 1), ("v24", "v21", 1), ("v49", "v50", 1), ("v50", "v51", 1), ("v51", "v52", 1), ("v52", "v49", 1),
                     ("co1", "co2", 1), ("co2", "co3", 1), ("co3", "co4", 1), ("co4", "co1", 1), ("v55", "v64", 1),
                     ("v56", "v63", 1), ("v58", "v65", 1), ("v57", "v66", 1)
                     ]

ValveLocation = [
    ["v1", "f1", "fo1"], ["v9", "f1", "fo1"], ["v17", "f1", "fo1"], ["v5", "f2", "fo2"], ["v10", "f2", "fo2"], ["v18", "f2", "fo2"],
    ["v2", "f3", "fo3"], ["v13", "f3", "fo3"], ["v19", "f3", "fo3"], ["v6", "f4", "fo4"], ["v14", "f4", "fo4"], ["v20", "f4", "fo4"],
    ["v3", "f5", "fo5"], ["v11", "f5", "fo5"], ["v21", "f5", "fo5"], ["v7", "f6", "fo6"], ["v12", "f6", "fo6"], ["v22", "f6", "fo6"],
    ["v4", "f7", "fo7"], ["v15", "f7", "fo7"], ["v23", "f7", "fo7"], ["v8", "f8", "fo8"], ["v16", "f8", "fo8"], ["v24", "f8", "fo8"],
    ["v45", "f10", "fo10"], ["v36", "f10", "fo10"], ["v28", "f10", "fo10"], ["v46", "f11", "fo11"], ["v37", "f11", "fo11"], ["v32", "f11", "fo11"],
    ["v47", "f12", "fo12"], ["v41", "f12", "fo12"], ["v29", "f12", "fo12"], ["v48", "f13", "fo13"], ["v42", "f13", "fo13"], ["v33", "f13", "fo13"],
    ["v49", "f14", "fo14"], ["v38", "f14", "fo14"], ["v30", "f14", "fo14"], ["v50", "f15", "fo15"], ["v39", "f15", "fo15"], ["v34", "f15", "fo15"],
    ["v51", "f16", "fo16"], ["v43", "f16", "fo16"], ["v31", "f16", "fo16"], ["v52", "f17", "fo17"], ["v44", "f17", "fo17"], ["v35", "f17", "fo17"],
    ["v25", "f9", "fo9"], ["v26", "fo40", "fo1"], ["v27", "fo41", "fo9"], ["v40", "fo42", "fo14"], ["v53", "fo43", "fo17"], ["v54", "fo22", "fo27"],
    ["v55", "fo23", "fo32"], ["v56", "fo24", "fo33"], ["v57", "fo25", "fo34"], ["v58", "fo26", "fo35"], ["v59", "fo24", "fo22"], ["v60", "fo26", "fo22"],
    ["v61", "fo28", "fo27"], ["v62", "fo30", "fo27"], ["v63", "fo28", "fo36"], ["v64", "fo29", "fo37"], ["v65", "fo30", "fo38"], ["v66", "fo31", "fo39"],
    ["co1", "fo18", "fo23"], ["co2", "fo19", "fo25"], ["co3", "fo20", "fo29"], ["co4", "fo21", "fo31"]
                 ]

g_flow.add_nodes_from(flow_node_list)
g_flow.add_weighted_edges_from(flow_edge_list)
g_control.add_nodes_from(control_node_list)
g_control.add_weighted_edges_from(control_edge_list)

folder_path = "../TestCaseFiles/lrb/"

outpath1 = f"{folder_path}/lrb5_control.dot"
outpath2 = f"{folder_path}/lrb5_flow.dot"
outpath = f"{folder_path}/lrb5_ValveLocation.txt"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

write_dot(g_control, outpath1)
write_dot(g_flow, outpath2)
with open(outpath, 'w') as f:
    for i in ValveLocation:
        i = str(i).strip('[').strip(']').replace(',', '').replace('\'', '')+'\n'
        f.writelines(i)



