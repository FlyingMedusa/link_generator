## Project:          Link generator

Python version:     Python 3

#### Files:

HackGeneratorLinkow.py  [main file]

GeneratorModul1.py      [module file]

createdlinks.txt        [output storing file]

## Main aim:
Link generator for affiliate program users of Helion.pl.

The user can turn regular links into links of a chosen client.

#### Regular links that can be changed this way:
    - home page
        e.g. https://helion.pl/
    - category page
        e.g. https://helion.pl/kategorie/ebooki
    - product page
        e.g. https://helion.pl/ksiazki/jak-naprawic-sprzet-elektroniczny-poradnik-dla-nieelektronika-wydanie-ii-michael-jay-geier,janas2.htm#format/e
    - basket page
        e.g. https://helion.pl/zakupy/edit.cgi

An example of a change [user id in this example: 90412]:

    input:  https://helion.pl/kategorie/ebooki
    
    output: https://helion.pl/page/90412/kategorie/ebooki


##### General:
Input:<br>

    user id, 
    basic link
    
Output:<br>

        updated link according to the users id,
        links stored in a .txt file

## USAGE WARNING

While giving a link as an input, remember to add a space at the end and then press enter. <br>
Otherwise your browser will open this link. <br>
Do NOT add more than ONE space at the end.
