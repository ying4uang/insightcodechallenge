import sys
import json
import networkx as nx
import numpy
import locale
from datetime import datetime, timedelta

# set locale to format output from 1.0 to 1.00
locale.setlocale(locale.LC_ALL, '')


# borrow the median function in numpy
def median(l):
    return numpy.median(numpy.array(l))


# loop through edges graph to remove edges/nodes earlier than threshold time
def remove_edges(Grph, threshold):
    edges_to_remove = []
    nodes_to_check = []

    for e in Grph.edges_iter():

        # second loop is in case there are multiple transactions between same people
        for key in G.edge[e[0]][e[1]].keys():

            if Grph.edge[e[0]][e[1]][key]['time'] < threshold:
                edges_to_remove.append((e[0], e[1],key))
                nodes_to_check.append(e[0])
                nodes_to_check.append(e[1])

    Grph.remove_edges_from(edges_to_remove)

    # loop through nodes to remove nodes w/ no edges
    nodes_to_remove = []
    for node in nodes_to_check:
        if not Grph.neighbors(node):
            nodes_to_remove.append(node)
    Grph.remove_nodes_from(nodes_to_remove)


# ------init variables BEGIN

inputfile = sys.argv[1]
outputfile = open(sys.argv[2], 'w')

G = nx.MultiGraph()

# stores the current max time of all the lines read.
current_max_time = None

# -------init variables END


with open(inputfile, 'rb') as f:

    for line in f:

        if line == '\n':
            print "Skipping an empty line."
            continue

        record = json.loads(line)

        try:
            record['time'] = datetime.strptime(record['created_time'], '%Y-%m-%dT%H:%M:%SZ')
            record['actor'] = str(record['actor']).lower()
            record['target'] = str((record['target']).lower())
        except ValueError:
            print("Oops!  That was not a valid time format.  Skipping to next line...")
            continue


        if not current_max_time:
            current_max_time = record['time']

        # if a record's timestamp is earlier than the current max time, but within 60s window
        # should add but no need to update graph
        if (record['time'] <= current_max_time) and (current_max_time - record['time'] <= timedelta(seconds=60)):
            G.add_edge(record['actor'], record['target'], time=record['time'])

        # if a new record has a timestamp that is 60s later than any current record
        # clear the current graph and  add the new node
        elif record['time'] - current_max_time > timedelta(seconds=60):
            G.clear()
            G.add_edge(record['actor'], record['target'], time=record['time'])
            current_max_time = record['time']

        # new edges, later than the current time, should add and update graph
        elif record['time'] > current_max_time:

            current_max_time = record['time']
            threshold_time = current_max_time - timedelta(seconds=60)

            remove_edges(G, threshold_time)
            G.add_edge(record['actor'], record['target'], time=record['time'])


        # calculate degree
        degreedict = G.degree()
        median_degree = median(degreedict.values())

        # format output
        d = locale.format("%.2f", float(median_degree), grouping=True)
        outputfile.write(d + '\n')

outputfile.close()
