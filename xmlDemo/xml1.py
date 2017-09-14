__author__ = 'LiGuangyu'


import xml.sax as sax


class CardFreeXmlHandler(sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag =="movie":
            print(" **** MOVIE **** ")
            title = attributes["title"]
            print('TITLE : ', title)

    def endElement(self, tag):
        if self.CurrentData == "type":
            print("Type:", self.type)
        elif self.CurrentData == "format":
            print("Format:", self.format)
        elif self.CurrentData == "year":
            print("year:", self.year)
        elif self.CurrentData == "stars":
            print("stars:", self.stars)
        elif self.CurrentData == "rating":
            print("rating:", self.rating)
        elif self.CurrentData == "description":
            print("description:", self.description)

    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "stars":
            self.stars = content
        elif self.CurrentData == "description":
            self.description = content

if __name__ == '__main__':
    parser = sax.make_parser()
    parser.setFeature(sax.handler.feature_namespaces, 0)

    Handler = CardFreeXmlHandler()
    parser.setContentHandler(Handler)
    parser.parse("movie.xml")



