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

		for i in range(7):
			measurement = { 'timestamp' : datetime.now(), 'value' : i * 10 }
			if i % 2 == 0:
				ret = self.addMeasurementToTestRun(test_id, 'total_documents', measurement)
			else:
				ret = self.addMeasurementToTestRun(test_id, 'cpu', measurement)
			self.log.info(ret)

		ret = self.getTestRun(test_id)
		self.log.info(ret)

	def validate(self):
		self.assertGrep('run.log', expr="'_id': 'Test 1'")

