#测试函数
#单元测试和测试用例
#可通过的测试 ------------run 1 test in 0.000s ok
#未通过的测试 E Error Traceback failed
#11-1 测试函数
import unittest
from turtledemo.clock import setup

from city_recnz import world_definition
class WorldTest(unittest.TestCase):
  def test_city_country(self):
    current_name=world_definition('Santiago','Chile')
    self.assertEqual(current_name,'Santiago,Chile')
  def test_country_population(self):
    current_name=world_definition('Santiago','Chile',5000)
    self.assertEqual(current_name,'Santiago,Chile-population:5000')
if __name__ == '__main__':
    unittest.main()

#测试类 11-3
import unittest
from city_recnz import Eployee
class EployeeTest(unittest.TestCase):
    def setUp(self):
        self.employee=Eployee('harry','de suza',50000)
    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.year_salary,50000)
    def test_give_custom_raise(self):
        self.employee.give_raise(add=10000)
        self.assertEqual(self.employee.year_salary,60000)

