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
	def create_key (medlemsNummer):
		return ndb.Key('Speider',medlemsNummer)
	
class Fordypningsmerke(ndb.Model):
	navn = ndb.StringProperty() 
	beskrivelse = ndb.StringProperty()
	link = ndb.StringProperty()
	nivaa = ndb.KeyProperty(repeated=True)
	bidrarTil = ndb.KeyProperty(repeated=True)
	
	@staticmethod
	def create_key (navn):
		return ndb.Key('Fordypningsmerke',navn)
	
