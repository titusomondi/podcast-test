import yaml
import xml.etree.ElementTree as xml_tree
with open ('feed.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)