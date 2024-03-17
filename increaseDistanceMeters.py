import re

filename  = 'data.xml'
distance_to_increase_by = 22936.76953125

with open(filename, 'r') as file:
    xml_data = file.read()
updated_xml = re.sub(r'<DistanceMeters>(.*?)</DistanceMeters>',
                    lambda match: '<DistanceMeters>' + str(float(match.group(1)) + distance_to_increase_by) + '</DistanceMeters>',
                    xml_data)
with open('modified.xml', 'w') as file:
    file.write(updated_xml)