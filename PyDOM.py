import requests
from time import sleep
from bs4 import BeautifulSoup
from dataclasses import dataclass


@dataclass
class Element:
    def __init__( self, element ):
        self._HTML      = str(element)
        self.prettyHTML = element.prettify().strip(" \n ")
        self.innerHTML  = element.decode_contents().strip(" \n ")
        self.innerText  = element.text.strip(" \n ")
        self.attrs      = element.attrs

    '''
    def __str__(self):
        return "<class 'PyDOM.Element'>"
    '''

    def __repr__(self):
        return str(self._HTML)


@dataclass
class Document:
    def __init__( self, URL ):
        response = requests.get( URL )
        while( response.status_code != 200 ):
            print(f"URL responded with wrong status code ({response.status_code}). Trying again...")
            sleep( 1 )
            response = requests.get( URL )
        self._beautiful_soup = BeautifulSoup(response.text, 'html.parser')
        response.close()

    def __str__(self):
        return "<class 'PyDOM.Document'>"

    def getElementById( self, id_name : str ):
        if( self._beautiful_soup.find( id = id_name ) is None):
            return None
        return Element( self._beautiful_soup.find( id = id_name ) )

    def getElementByTagName( self, tag_name : str ):
        return [ Element(t) for t in self._beautiful_soup.find_all( tag_name ) ]

    def getElementByClassName( self, class_name : str ):
        return [ Element(c) for c in self._beautiful_soup.find_all( class_ = class_name ) ]

    def getElementByName( self, name : str ):
        print("WARNING: 'getElementByName' method is not implemented yet")