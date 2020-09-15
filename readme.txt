SMWinservice
by Davide Mastromatteo
Base class to create winservice in Python
-----------------------------------------
Anleitung:
1. Erstellen Sie einfach eine neue Klasse, die von dieser Basisklasse erbt
2. Definieren Sie in der neuen Klasse die Variablen
    _svc_name_ = "nameOfWinservice"
    _svc_display_name_ = "Name des Winservices, der in scm angezeigt wird"
    _svc_description_ = "Beschreibung des Winservice, der in scm angezeigt wird"
3. Überschreiben Sie die drei Hauptmethoden:
     def start (self): wenn Sie bei der Dienstinitialisierung etwas tun müssen.
     Eine gute Idee ist es, hier die Inizialisierung des Laufzustands vorzunehmen
     def stop (self): Wenn Sie etwas tun müssen, bevor der Dienst beendet wird.
     Eine gute Idee ist es, hier die Ungültigmachung des Betriebszustands zu setzen
     def main (self): Ihre aktuelle Run-Schleife. Erstellen Sie einfach eine Schleife, die auf Ihrem Laufzustand basiert
4. Definieren Sie den Einstiegspunkt Ihres Moduls mit der Methode "parse_command_line" der neuen Klasse
5. Installieren sie den Dienst über die Befehlszeile mit folgendem Befehl: "python PythonCornerExample.py install"
6. um den Dienst zu aktualisieren: "python PythonCornerExample.py update"
7. Um den dienst zu stoppen: "net stop PythonCornerExample"

8. Viel Spaß