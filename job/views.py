from django.shortcuts import redirect, render
from  .models import Job
from django.core.paginator import Paginator
from .form import ApplyForm, JobForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from  .filters import JobFilter


#this is 
def job_list(request):
    job_list = Job.objects.all()   #google for django query set documentation 
    
    #filters
    myfilter = JobFilter(request.GET, queryset=job_list)
    
    job_list = myfilter.qs
    
    #this is from django paginator documentation
    paginator = Paginator(job_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    #don't forget to return the page object in the context 
    context = {'jobs':page_obj, 'myfilter':myfilter}    #key is the name you will use in template -- value is your name here
    return render(request,'job/job_list.html', context) #you will need 3 arguments in the return


def job_detail(request, slug):
    job_detail = Job.objects.get(slug=slug)
    
    if request.method=='post':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
    else:
        form = ApplyForm
    
    context = {'job':job_detail, 'form1':form }
    return render(request,'job/job_detail.html', context)


@login_required
def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect (reverse('jobs:job_list'))
    else:
        form = JobForm()
    return render(request, 'job/add_job.html', {'form':form})