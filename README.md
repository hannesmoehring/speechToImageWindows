In diesem Projekt geht es grob darum, dass etwas eingesprochen werden kann in einer von 50+ Sprachen, dies dann ins englische übersetzt wird und durch KI ein Bild zu diesem Text
generiert wird. Das ist möglich durch die OpenAI API mit Whisperer und dem Image Generating Model.

Vorbereitung: Die benötigten Libraries sollten alle im requirements.txt stehen und sollten bereits im venv vorhanden sein. Es wurde mit Python3.9 getestet. Zusätzlich wird ein API Key benötigt da es kostenpflichtig ist und darüber verrechnet wird. 
Den API Key einfach in apiKey.txt ablegen. Zusaätzlich muss der Pfad zum Python interpreter in startup.py abgelegt werden.


Kurze Anleitung:

Projekt start durch startup.py,  es erscheint ein Screen mit einem "Start" Button, den drücken, danach erscheint eine Benutzeroberfläche mit einem roten Button in der mitte.
Sobald dieser gedrückt wird wird eine Audioaufnahme gestartet welche nach 10 Sekunden endet. Diese ercheint nach kurzem Warten auf dem Bildschirm
und nach weiteren 10 Sekunden erscheint das dazugehörige Bild. Dieser Screen wird gespeichert mit einem Timestamp in /imgOnLayout.

Im Moment ist drucken deaktiviert, zum aktivieren muss printHandler.py bearbeitet werden.

