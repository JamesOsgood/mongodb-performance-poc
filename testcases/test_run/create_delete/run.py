# Import base test
from TestRunBaseTest import TestRunBaseTest
from datetime import datetime

class PySysTest(TestRunBaseTest):

	def execute(self):
	
		ret = self.createTestRun()
		self.log.info(ret)
		test_id = ret['test_id']

		ret = self.deleteTestRun(test_id)
		self.log.info(ret)

	def validate(self):
		self.assertGrep('run.log', expr='Created test run')
		self.assertGrep('run.log', expr='Deleted test run')

