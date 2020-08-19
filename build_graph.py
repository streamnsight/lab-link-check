import os
import argparse
import glob
import json
import csv

def main(path):
    graph = {}
    files=glob.glob(os.path.join(path, '**/manifest.json'), recursive=True)
    for json_file in files:
        folder = os.path.dirname(json_file)
        folder = folder.replace(path, '')
        try:
            manifest = json.load(open(json_file, 'r'))
        except Exception as e:
            print(str(e))
        tutorials = manifest.get('tutorials', [])
        for lab in tutorials:
            filename = lab.get('filename')
            if 'https://raw.githubusercontent' in filename:
                filename = filename.replace('https:/raw.githubusercontent.com/oracle/learning-library/master', '')
            file_path = os.path.normpath(os.path.join(folder, filename))
            title = lab.get('title', 'no title')
            description = lab.get('description', 'no description')
            if file_path not in graph:
                graph[file_path] = []
            graph[file_path].append({'workshop': folder, 'title': title, 'description': description})
    return graph


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='path to the root of the local repository')
    args = parser.parse_args()
    graph = main(args.path)
    usage_graph = {}
    flat_graph = []
    for k,v in graph.items():
        if len(v) > 1:
            usage_graph[k] = v
            flat_graph.append([k, "\n".join([r.get('workshop') for r in v])])
    json.dump(usage_graph, open('dependency_graph.json', 'w'), indent=2)
    writer = csv.writer(open('dependency_graph.csv', 'w'), quoting=csv.QUOTE_ALL)
    writer.writerow(['Lab', 'Workshop'])
    for row in flat_graph:
        writer.writerow(row)
