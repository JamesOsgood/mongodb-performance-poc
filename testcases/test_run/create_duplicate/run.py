# Import base test
from TestRunBaseTest import TestRunBaseTest
from datetime import datetime

class PySysTest(TestRunBaseTest):

	def execute(self):
	
		test_id = 'Test 1'
		ret = self.deleteTestRun(test_id)
		self.log.info(ret)

		ret = self.createTestRun(test_id)
		self.log.info(ret)

		try:
			ret = self.createTestRun(test_id)
			self.log.info(ret)
		except RuntimeError as ex:
			self.log.error(ex)

	def validate(self):
		self.assertGrep('run.log', expr='Error: MongoError: E11000 duplicate key error collection')

