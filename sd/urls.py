from django.urls import include, path
from rest_framework.routers import DefaultRouter

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from usermanager import views as userVies
from frontend import views as frentViews
from menumanager.views import MenuView
from salarymanager import views as salView
from django.conf import settings
from django.conf.urls.static import static
from employeemanager.views import DownloadViewSet, FileUploadView, EmployeeIdcardsviewSet,EmployeeExport
 

router = DefaultRouter()
# router.register('users', UserViewSet)
# router.register('employees', EmployeeViewSet)
# router.register('payslips', PayslipViewSet)
# router.register('attendance', AttendanceViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="SD SERVICE ",
        default_version='v1',
        description="API documentation for SDSERVICE App",
        terms_of_service=" ",
        contact=openapi.Contact(email="ramesh@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

swagger_info = openapi.Info(
    title="SD SRVICE",
    default_version='v1',
    description="API documentation for SD SRVICE App",
    terms_of_service="https://www.example.com/terms/",
    contact=openapi.Contact(email="contact@example.com"),
    license=openapi.License(name="MIT License"),
)


front_urls = [path('dashboard', frentViews.dashboard),
          path('employee', frentViews.EmployeeView),
          path('newemployee', frentViews.NewEmployeeView),
          path('login', frentViews.login),
            path('', frentViews.home),
          path('attendence', frentViews.AttendanceView),
          path('myattendence', frentViews.MyAttendanceView),
        path('myfamaly', frentViews.MyfamalyView),
         path('employeedetails', frentViews.Employeedetails),


          path('newattendence', frentViews.NewAttendanceView),
          path('company', frentViews.CompanyList),
          path('salary', frentViews.Salary),
          path('newsalary', frentViews.NewSalary),  
           path('addsalary', frentViews.BulkSalary), 
           path('famaly', frentViews.EmpFamaly),  
          path('companysettings', frentViews.CompanySettingsview),  

          

         ]

urlpatterns = front_urls+[
     path('api/download/', DownloadViewSet.as_view() ),
     path('api/idcards/', EmployeeIdcardsviewSet.as_view() ),
      path('api/export/', EmployeeExport.as_view() ),
     
        path('api/upload/', FileUploadView.as_view(), name='file-upload'),
        path('api/signin/', userVies.SignInView.as_view(), name='signin'),
        # path('api/downloadexcel/', salView.YourModelViewSet.as_view({'get': 'download_payslip'}), name='download-excel'),
        path('logout/', userVies.Logout, name='loout'),
        path('adminslist/', userVies.adminslist, name='userlist'),
        
        
        path('admin/', admin.site.urls),
        path('api/', include(router.urls)),
        
        
        path('api/user/', include('usermanager.urls')),
        path('api/employee/', include('employeemanager.urls')),
        path('api/salary/', include('salarymanager.urls')),
        path('api/company/', include('companymanager.urls')),
        path('api/attendance/', include('attendencemanager.urls')),
        path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
        path('api/menu/', MenuView.as_view()),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
