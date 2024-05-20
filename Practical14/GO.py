import xml.dom.minidom
import matplotlib.pyplot as plt
import xml.sax
import datetime

def parse_DOM(file_path):
    start_time = datetime.datetime.now()
    DOMTree = xml.dom.minidom.parse(file_path)
    collection = DOMTree.documentElement
    namespace = collection.getElementsByTagName('namespace')
    total = {'biological_process': 0,'molecular_function': 0, 'cellular_component': 0}  
    terms = collection.getElementsByTagName('term')  
  
    for term in terms:  
        namespace_elem = term.getElementsByTagName('namespace')[0]  
        namespace_text = namespace_elem.firstChild.data 
        if namespace_text in total:  
            total[namespace_text] += 1  
    
    end_time = datetime.datetime.now()
    time_dom = end_time - start_time
    print(f"Time taken to parse XML using DOM: {time_dom}")
    return total

def parse_SAX(file_path):
    start_time = datetime.datetime.now()
    terms_found = []
    total = {}
    class namespaceHandler(xml.sax.ContentHandler):
        def __init__(self):
            self.currentElement = ''
            self.namespace = ''
    
        def startElement(self, tag, attrs):
            self.currentElement = tag
    
        def characters(self, content):
            if self.currentElement == 'namespace':
                self.namespace += content.strip()
    
        def endElement(self, tag):
            if tag == 'namespace':
                if self.namespace:  
                    terms_found.append(self.namespace)  
                    self.namespace = ''  
    
    handler = namespaceHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(file_path)
    for term in terms_found:
        if term in ('molecular_function', 'biological_process', 'cellular_component'): 
            if term not in total:
                total[term] = 1
            else:
                total[term] += 1
    
    end_time = datetime.datetime.now()
    time_sax = end_time - start_time
    print(f"Time taken to parse XML using SAX: {time_sax}")
    return total
file_path=('/Users/zhangmaisha/Desktop/IBI/IBI1_2023-24/IBI1_2023-24/Practical14/go_obo.xml')

total_DOM = parse_DOM(file_path)
total_SAX = parse_SAX(file_path)
for term, count in total_DOM.items():  
    print(f"DOM: Term: {term}, Count: {count}")  
for term, count in total_SAX.items():  
    print(f"SAX: Term: {term}, Count: {count}")  

# Plotting the results
plt.figure(figsize=(10, 6)) 
bars = plt.bar(total_DOM.keys(), total_DOM.values(), width=0.3, color="black")
plt.ylabel('Number of GO Terms')
plt.title('The Number of Terms within Each Ontology: DOM')
plt.xticks(rotation=90) 
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6)) 
bars = plt.bar(total_SAX.keys(), total_SAX.values(), width=0.3, color="blue")
plt.ylabel('Number of GO Terms')
plt.title('The Number of Terms within Each Ontology: SAX')
plt.tight_layout()
plt.show()
plt.clf()

#Time taken to parse XML using DOM: 0:00:12.944466
#Time taken to parse XML using SAX: 0:00:02.675386
#SAX is quicker to complete the task