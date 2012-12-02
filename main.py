#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2 
import db

class MainHandler(webapp2.RequestHandler):
    def get(self):
		
		nokkel = db.Nivaa.create_key("Bever")
		r = db.Nivaa(navn="Bever")
		r.key = nokkel
		r.put()

		nokkel = db.Gruppe.create_key("Askim Speidergruppe")
		r = db.Gruppe(navn="Askim Speidergruppe")
		r.key = nokkel
		r.put()

		nokkel = db.Programmerke.create_key("Bever", "Friluftsliv")
		r = db.Programmerke(navn="Friluftsliv")
		r.key = nokkel
		r.put()

		nivaa_nokkel = db.Nivaa.create_key("Bever")
		nokkel = db.Fordypningsmerke.create_key("flagg_bever")
		r = db.Fordypningsmerke(id="flagg_bever",
				navn="Flagg",
				nivaa=[nivaa_nokkel])
		r.key = nokkel
		r.put()

		self.response.write('Hei DU!!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

