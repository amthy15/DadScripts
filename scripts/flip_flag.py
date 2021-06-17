import xml.etree.ElementTree as et
import sys

def flip_flag(filepath: str, filename: str, flag: str):
    xml_tree = et.parse(f'{filepath}/{filename}')
    root = xml_tree.getroot()
    for elem in root.iter(flag):
        elem.text = 'False'
    xml_tree.write(f'{filepath}/{filename.rsplit( ".", 1 )[ 0 ]}_new.xml')


filename = sys.argv[1]
filepath = sys.argv[2]
flagname = sys.argv[3]
flip_flag(filepath, filename, flagname)
