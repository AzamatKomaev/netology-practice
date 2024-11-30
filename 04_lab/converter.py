import json
import xml
import xml.etree
import xml.etree.ElementTree


def main():
    output_dict = {}

    tree = xml.etree.ElementTree.parse("input.xml")
    root = tree.getroot()
    root_tag = root.tag
    output_dict[root_tag] = []
    
    for person in root.findall("person"):
        output_dict[root_tag].append({})
        for param in person:
            output_dict[root_tag][-1][param.tag] = param.text

    output_json = json.dumps(output_dict)
    with open('output.json', 'w') as fout:
        fout.write(output_json)
        



if __name__ == '__main__':
    main()