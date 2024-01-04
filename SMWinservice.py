'''
SMWinservice
by Davide Mastromatteo
Base class to create winservice in Python
-----------------------------------------
Anleitung:
1. Erstellen Sie einfach eine neue Klasse, die von dieser Basisklasse erbt
2. Definieren Sie in der neuen Klasse die Variablen
    - _svc_name_ = "nameOfWinservice"
    - _svc_display_name_ = "Name des Winservices, der in scm angezeigt wird"
    - _svc_description_ = "Beschreibung des Winservice, der in scm angezeigt wird"
3. Überschreiben Sie die drei Hauptmethoden:
    - def start (self): wenn Sie bei der Dienstinitialisierung etwas tun müssen.
    - Eine gute Idee ist es, hier die Inizialisierung des Laufzustands vorzunehmen
    - def stop (self): Wenn Sie etwas tun müssen, bevor der Dienst beendet wird.
    - Eine gute Idee ist es, hier die Ungültigmachung des Betriebszustands zu setzen
    - def main (self): Ihre aktuelle Run-Schleife. Erstellen Sie einfach eine Schleife, die auf Ihrem Laufzustand basiert
4. Definieren Sie den Einstiegspunkt Ihres Moduls mit der Methode "parse_command_line" der neuen Klasse
5. Installieren sie den Dienst über die Befehlszeile mit folgendem Befehl: "python PythonCornerExample.py install"
6. um den Dienst zu aktualisieren: "python PythonCornerExample.py update"
7. Um den dienst zu stoppen: "net stop PythonCornerExample"

8. Viel Spaß
'''

import socket
import win32serviceutil

import servicemanager
import win32event 
import win32service


class SMWinservice(win32serviceutil.ServiceFramework):
    '''Base class to create winservice in Python'''

    _svc_name_ = 'pythonService'
    _svc_display_name_ = 'Python Service'
    _svc_description_ = 'Python Service Description'

    @classmethod
    def parse_command_line(cls):
        '''
        ClassMethod to parse the command line
        '''
        win32serviceutil.HandleCommandLine(cls)

    def __init__(self, args):
        '''
        Constructor of the winservice
        '''
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        '''
        Called when the service is asked to stop
        '''
        self.stop()
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        '''
        Called when the service is asked to start
        '''
        self.start()
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()

    def start(self):
        '''
        Override to add logic before the start
        eg. running condition
        '''
        pass

    def stop(self):
        '''
        Override to add logic before the stop
        eg. invalidating running condition
        '''
        pass

    def main(self):
        '''
        Main class to be ovverridden to add logic
        '''
        pass

# entry point of the module: copy and paste into the new module
# ensuring you are calling the "parse_command_line" of the new created class
if __name__ == '__main__':
    SMWinservice.parse_command_line()