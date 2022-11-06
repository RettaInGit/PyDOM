# DESCRIPTION
BeautifulSoup wrapper to simulate the JavaScript "document" with python


# USAGE
```python
import PyDOM

# create DOM
document = Document( *URL* )

# ID
id_elem = document.getElementById( *id_name* )
print( id_elem )
print( id_elem.innerHTML )
print( id_elem.innerText )
print( id_elem.attrs )

# TAG
tag_elems = document.getElementByTagName( *tag_name* )
for tag_elem in tag_elems:
    print( tag_elem )
    print( tag_elem.innerHTML )
    print( tag_elem.innerText )
    print( tag_elem.attrs )

# CLASS
class_elems = document.getElementByClassName( *class_name* )
for class_elem in class_elems:
    print( class_elem )
    print( class_elem.innerHTML )
    print( class_elem.innerText )
    print( class_elem.attrs )
```


# LICENSE
This repository and all the code it contains can be copied and edited by anyone.