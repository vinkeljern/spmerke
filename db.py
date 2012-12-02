from google.appengine.ext import ndb

class Speider(ndb.Model):
	navn = ndb.StringProperty()
	medlemsNummer = ndb.IntegerProperty()
	gruppe = ndb.KeyProperty()
	nivaa = ndb.KeyProperty(repeated=True)
	fordypingingsMerker = ndb.KeyProperty(repeated=True)
	programMerker = ndb.KeyProperty(repeated=True)
	programMaal = ndb.KeyProperty(repeated=True)
	
	@staticmethod
	def create_key (gruppe, medlemsNummer):
		return ndb.Key('Gruppe', gruppe, 'Speider',medlemsNummer)
	
class Fordypningsmerke(ndb.Model):
	id = ndb.StringProperty()
	navn = ndb.StringProperty() 
	beskrivelse = ndb.StringProperty()
	link = ndb.StringProperty()
	nivaa = ndb.KeyProperty(repeated=True)
	bidrarTil = ndb.KeyProperty(repeated=True)
	
	@staticmethod
	def create_key (id):
		return ndb.Key('Fordypningsmerke',id)
	
class Programmerke(ndb.Model):
	navn = ndb.StringProperty()
	beskrivelse = ndb.StringProperty()
	link = ndb.StringProperty()

	@staticmethod
	def create_key (nivaa, navn):
		return ndb.Key('Nivaa', nivaa,'Programmerke',navn)

class Nivaa(ndb.Model):
	navn = ndb.StringProperty()
	beskrivelse = ndb.StringProperty()
	link = ndb.StringProperty()

	@staticmethod
	def create_key (navn):
		return ndb.Key('Nivaa', navn)

class Gruppe(ndb.Model):
	navn = ndb.StringProperty()
	link = ndb.StringProperty()

	@staticmethod
	def create_key (navn):
		return ndb.Key('Gruppe', navn)

class Aktivitet(ndb.Model):
        navn = ndb.StringProperty()
        beskrivelse = ndb.StringProperty()
        link = ndb.StringProperty()
        nivaa = ndb.KeyProperty(repeated=True)
	bidrarTil = ndb.KeyProperty(repeated=True)

	@staticmethod
	def create_key (nivaa, navn):
		return ndb.Key('Nivaa', nivaa,'Aktivitet',navn)
