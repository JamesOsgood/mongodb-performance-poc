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

		ret = self.getTestRun(test_id)
		self.log.info(ret)

	def validate(self):
		self.assertGrep('run.log', expr="'_id': 'Test 1'")

