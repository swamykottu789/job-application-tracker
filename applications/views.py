from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .models import Job
from .forms import JobForm, RegisterForm


# User registration
def register(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            messages.success(
                request,
                'Registration successful!'
            )

            return redirect('dashboard')

    else:

        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


# Dashboard
@login_required
def dashboard(request):

    search = request.GET.get('search', '')

    jobs = Job.objects.filter(
        user=request.user
    ).order_by('-applied_date')

    if search:

        jobs = jobs.filter(
            company_name__icontains=search
        ) | jobs.filter(
            user=request.user,
            job_title__icontains=search
        )

    total_jobs = Job.objects.filter(
        user=request.user
    ).count()

    applied = Job.objects.filter(
        user=request.user,
        status='Applied'
    ).count()

    interviews = Job.objects.filter(
        user=request.user,
        status='Interview'
    ).count()

    selected = Job.objects.filter(
        user=request.user,
        status='Selected'
    ).count()

    rejected = Job.objects.filter(
        user=request.user,
        status='Rejected'
    ).count()

    context = {
        'jobs': jobs,
        'total_jobs': total_jobs,
        'applied': applied,
        'interviews': interviews,
        'selected': selected,
        'rejected': rejected,
        'search': search,
    }

    return render(request, 'dashboard.html', context)


# Add job
@login_required
def add_job(request):

    if request.method == 'POST':

        form = JobForm(request.POST)

        if form.is_valid():

            job = form.save(commit=False)

            job.user = request.user

            job.save()

            messages.success(
                request,
                'Job added successfully!'
            )

            return redirect('dashboard')

    else:

        form = JobForm()

    return render(request, 'add_job.html', {'form': form})


# Edit job
@login_required
def edit_job(request, id):

    job = get_object_or_404(
        Job,
        id=id,
        user=request.user
    )

    if request.method == 'POST':

        form = JobForm(request.POST, instance=job)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Job updated successfully!'
            )

            return redirect('dashboard')

    else:

        form = JobForm(instance=job)

    return render(
        request,
        'edit_job.html',
        {'form': form, 'job': job}
    )


# Delete job
@login_required
def delete_job(request, id):

    job = get_object_or_404(
        Job,
        id=id,
        user=request.user
    )

    if request.method == 'POST':

        job.delete()

        messages.success(
            request,
            'Job deleted successfully!'
        )

    return redirect('dashboard')