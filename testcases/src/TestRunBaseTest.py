
import json
from datetime import datetime

import requests
from bson.json_util import RELAXED_JSON_OPTIONS
from pysys.basetest import BaseTest


'''
Created on 30th July 2019

Base class for Case tests

@author: James Osgood
'''

class TestRunBaseTest(BaseTest):
	def __init__ (self, descriptor, outsubdir, runner):
		BaseTest.__init__(self, descriptor, outsubdir, runner)

		self.baseUrl = 'http://localhost:3334'

	def createTestRun(self, test_id=None, log_messages=False):
		if not test_id:
			test_id = 'Test_' + datetime.now().isoformat()
		url = f'{self.baseUrl}/test_run/{test_id}'
		return self.doRequestPost(url, {}, 201, log_messages)

	def deleteTestRun(self, test_id, log_messages=False):
		url = f'{self.baseUrl}/test_run/{test_id}'
		return self.doRequestDelete(url, log_messages)

	def getTestRun(self, test_id, log_messages=False):
		url = f'{self.baseUrl}/test_run/{test_id}'
		return self.doRequestGet(url, log_messages)

	def addMeasurementToTestRun(self, test_id, measurement_name, measurement, log_messages=False):
		measurements = [measurement]
		return self.addMeasurementsToTestRun(test_id, measurement_name, measurements, log_messages)

	def addMeasurementsToTestRun(self, test_id, measurement_name, measurements, log_messages=False):
		url = f'{self.baseUrl}/test_run/{test_id}'
		data = { 'measurement_name' : measurement_name, 'measurements' : measurements}
		return self.doRequestPatch(url, data, 200, log_messages)
	
	def doRequestGet(self, url, log_messages=False):
		if log_messages:
			self.log.info('GET:%s' % url)
		response = requests.get(url)
		if log_messages:
			self.log.info(response.json())
		
		expected_return = 200
		if response.status_code != expected_return:
			self.log.info('API call returned %d, expected %d' % (response.status_code, expected_return))
			raise RuntimeError(response.json())
		else:
			return response.json()

	def doRequestDelete(self, url, log_messages=False):
		if log_messages:
			self.log.info('DELETE:%s' % url)
		response = requests.delete(url)
		if log_messages:
			self.log.info(response.json())
		
		expected_return = 200
		if response.status_code != expected_return:
			self.log.info('API call returned %d, expected %d' % (response.status_code, expected_return))
			raise RuntimeError(response.json())
		else:
			return response.json()

	def doRequestPost(self, url, data, expected_return = 200, log_messages = False):
		if log_messages:
			self.log.info(url)
		payload = json.dumps(data, default=self.json_serializer)
		response = requests.post(url, data=payload ,headers={'content-type':'application/json', 'accept':'application/json'})
		if log_messages:
			self.log.info(response.json())
		if response.status_code != expected_return:
			self.log.info('API call returned %d, expected %d' % (response.status_code, expected_return))
			raise RuntimeError(response.json())
		else:
			return response.json()

	def doRequestPatch(self, url, data, expected_return = 200, log_messages = False):
		if log_messages:
			self.log.info(url)
		payload = json.dumps(data, default=self.json_serializer)
		self.log.info(payload)
		response = requests.patch(url, data=payload ,headers={'content-type':'application/json', 'accept':'application/json'})
		if log_messages:
			self.log.info(response.json())
		if response.status_code != expected_return:
			self.log.info('API call returned %d, expected %d' % (response.status_code, expected_return))
			raise RuntimeError(response.json())
		else:
			return response.json()

	def json_serializer(self, obj):
		"""JSON serializer for objects not serializable by default json code"""

		if isinstance(obj, (datetime)):
			return obj.isoformat()
		raise TypeError ("Type %s not serializable" % type(obj))
