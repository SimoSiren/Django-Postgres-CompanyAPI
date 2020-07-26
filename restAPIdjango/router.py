from employeeAPI.viewsets import EmployeeViewset, CustomerViewset, ProductViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee',EmployeeViewset)
router.register('customer',CustomerViewset)
router.register('product',ProductViewset)
