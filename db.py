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
	
