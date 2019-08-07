import os

class writecompositionXML():
    """
    Class managing the writing of a composition model xml file with all gathered data with pycrop2ml' user interface.

    Parameters : \n
        - data : {
                    'Path': '',
                    'Model type': 'unit',
                    'Model name': '',
                    'Model ID': '',
                    'Version': '',
                    'Timestep': '',
                    'Title': '',
                    'Authors': '',
                    'Institution': '',
                    'Reference': '',
                    'Abstract': '',
                    'Old name':'' IF iscreate=False
                   }
        
        - listmodel : []

        - listlink : [
                       {
                        'Link type': '',
                        'Target': '',
                        'Source': ''
                       }
                     ]
        
        - iscreate : bool
    """


    def __init__(self, data, listmodel, listlink, iscreate=True):

        self._datas = data
        self._listmodel = listmodel
        self._listlink = listlink
        self._iscreate = iscreate



    def write(self):
        """
        Writes the xml file with the new data set
        """
      
        try:
            fw = open('{}{}{}.{}.xml'.format(self._datas['Path'], os.path.sep, self._datas['Model type'], self._datas['Model name']), "w", encoding='utf8')

        except IOError as ioerr:
            raise Exception('File {} could not be opened in write mode. {}'.format(self._datas['Path'], ioerr))

        else:
            split = self._datas['Path'].split(os.path.sep)

            fw.write('<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE ModelComposition PUBLIC " " "https://raw.githubusercontent.com/AgriculturalModelExchangeInitiative/crop2ml/master/ModelComposition.dtd">')
            fw.write('<ModelComposition name="{0}" id="{2}.{1}.{0}" version="{3}" timestep ="{4}">'.format(self._datas['Model name'], split[-2], self._datas['Model ID'], self._datas['Version'], self._datas['Timestep']))
            fw.write('\n\t<Description>\n\t\t<Title>{}</Title>\n\t\t<Authors>{}</Authors>\n\t\t<Institution>{}</Institution>\n\t\t<Reference>{}</Reference>\n\t\t<Abstract>{}</Abstract>'.format(self._datas['Title'], self._datas['Authors'], self._datas['Institution'], self._datas['Reference'], self._datas['Abstract']))
            fw.write('\n\t</Description>\n\n\t<Composition>')

            for i in self._listmodel:
                fw.write('\n\t\t<Model name="{0}" id="{1}.{0}" filename="{2}" {3}/>'.format(i.split('.')[1], i.split(':')[0] if ':' in i else split[-2], i.split(':')[-1], ('package_name="{}" '.format(i.split(':')[0]) if ':' in i else '')))

            fw.write("\n\n\t\t<Links>")
            
            for j in self._listlink:
                fw.write('\n\t\t\t<{} target="{}" source="{}" />'.format(j['Link type'], j['Target'], j['Source']))
                       
            fw.write('\n\t\t</Links>\n\t</Composition>\n</ModelComposition>')
            fw.close()
        

            if all([not self._iscreate, self._datas['Model name'] != self._datas['Old name']]):
                os.remove('{}{}composition.{}.xml'.format(self._datas['Path'], os.path.sep, self._datas['Old name']))