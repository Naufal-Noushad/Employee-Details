from django.shortcuts import render,redirect

from django.views.generic import View

from myapp.forms import EmployeeForm

from myapp.models import Employee

from django.contrib import messages

# Create your views here.


class EmployeeCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=EmployeeForm()

        return render(request,'Employee_add.html',{'form':form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=EmployeeForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Employee.objects.create(**data)

            messages.success(request,"Employee added Successfully")

            return redirect('employee-list')
        
        else:

            messages.error(request,"An Error Occured when Adding Employee")

            return render(request,'Employee_add.html',{'form':form_instance})
        

class EmployeeListView(View):

    def get(self,request,*args,**kwargs):

        qs=Employee.objects.all()

        return render(request,'employee_list.html',{'employee':qs})
    
class EmployeeDetailView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get('pk')

        qs=Employee.objects.get(id=id)

        return render(request,'employee_detail.html',{'employee':qs})
    

class EmployeeDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get('pk')

        Employee.objects.get(id=id).delete()

        messages.success(request,"Employee Deleted Succesfully")

        return redirect('employee-list')
    

class EmployeeUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get('pk')

        employee_obj=Employee.objects.get(id=id)

        employee_dict={

            "name" : employee_obj.name,
            "designation" : employee_obj.designation,
            "department" : employee_obj.department,
            "salary": employee_obj.salary,
            "contact": employee_obj.contact,
            "address":employee_obj.address,
        }

        form_instance=EmployeeForm(initial=employee_dict)

        return render(request,'employee_update.html',{'form':form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=EmployeeForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            id=kwargs.get('pk')

            Employee.objects.filter(id=id).update(**data)

            messages.success(request,"Employee Updated Succesfully")

            return redirect('employee-list')
        
        else:

            messages.error(request,"Employee failed to update")

            return render(request,'employee_update.html',{'form':form_instance})

        