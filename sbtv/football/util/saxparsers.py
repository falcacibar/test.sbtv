import xml.sax


class MatchesHandler(xml.sax.handler.ContentHandler):

    parseElemDataNone     = 0
    parseElemDataAsScalar = 1
    parseElemDataAsDict   = 2

    ignoreElements = [ 
        'goleadoreslocal'
        , 'goleadoresvisitante'
        , 'gol'
        , 'goles'
        , 'jugador'
        , 'arbitro'
        , 'medios'
    ]

    def __init__(self, items):
        self.items = items
        self.parse = True
        self.parsingMatch = False
        self.parseElemData = self.parseElemDataNone
        self.parseElemDataName = None

    def startElement(self, name, attrs):
        if self.parse:
            if name == 'partido':
                self.items.append(dict(attrs))
                self.parsingMatch = True
            # In this case doesn't have sense parse goleadores
            # and will be ignored in the following if
            elif self.parsingMatch and name not in self.ignoreElements:
                if name == 'estado' and attrs['id'] != '2':
                    self.parse = False
                    self.items.pop()

                    return

                self.parseElemDataName = name

                if len(attrs):
                    self.parseElemData = self.parseElemDataAsDict
                    self.items[-1][name] = dict(attrs)
                else:
                    self.parseElemData = self.parseElemDataAsScalar
                    self.items[-1][name] = None

    def endElement(self, name):
        if name == 'partido':
            self.parsingMatch = False
            self.parse = True

    def characters(self, content):
        if self.parseElemData and len(content):
            # I will assume as "nombre" as the entry for the
            # character data inside the element when have attrs
            if self.parseElemData == self.parseElemDataAsDict:
                self.items[-1][self.parseElemDataName]['nombre'] = content
            elif self.parseElemData == self.parseElemDataAsScalar:
                self.items[-1][self.parseElemDataName] = content

            self.parseElemData = self.parseElemDataNone
            self.parseElemDataName = None
