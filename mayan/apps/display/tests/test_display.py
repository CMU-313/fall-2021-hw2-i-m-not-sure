from mayan.apps.testing.tests.base import GenericViewTestCase

class DisplayViewTestCase(GenericViewTestCase):

	# Test Statistics Page Loading
    def test_statistics_view(self):
        response = self.get(viewname='common:statistics_view')
        self.assertContains(response=response, text='Statistics', status_code=200)

    # Test Students Page Loading 
    def test_students_view(self):
        response = self.get(viewname='common:student_view')
        self.assertContains(response=response, text='Students', status_code=200)