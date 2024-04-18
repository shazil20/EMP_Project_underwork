from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from rest_framework import viewsets

from .forms import ApplyLeave, CustomUserEditForm
from .forms import UserRegistrationForm
from .models import Notification, CustomUser
from .serializers import CustomUserSerializer


@login_required
def HomePage(request):
    notifications = Notification.objects.all()
    return render(request, 'home.html', {'notifications': notifications})


def createuser(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully.")
            return redirect('login')
        else:
            messages.error(request, "There was a problem with your form submission.")
    else:
        form = UserRegistrationForm()

    return render(request, 'signup.html', {'form': form})


# def LoginPage(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 # Redirect to a success page
#                 return redirect('home')  # Replace 'home' with the name of your homepage URL
#     else:
#         form = UserLoginForm()
#     return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


def generate_salary_slip(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="salary_slip.pdf"'

    # Generate PDF
    p = canvas.Canvas(response, pagesize=letter)
    p.drawString(100, 750, "Salary Slip")
    # Add more content here
    p.showPage()
    p.save()

    return response


def apply_leave(request):
    if request.method == 'POST':
        form = ApplyLeave(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                'New Contact Form Submission',
                f'Name: {name}\nEmail: {email}\nMessage: {message}',
                'shazil03144426622@gmail.com',
                ['shazil03144426622@gmail.com'],
                fail_silently=False,
            )

            send_mail(
                'Subject: Thank you for contacting us',
                f'Thank you for reaching out, {name}!\n\nWe have received your message and will get back to you soon.',
                'shazil03144426622@gmail.com',
                [email],
                fail_silently=False,
            )
            return render(request, 'success.html')

    return render(request, 'applyleave.html', {'form': ApplyLeave()})


def success_page(request):
    return render(request, 'success.html')


def admin_login(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/admin_dashboard')
        else:
            return redirect('/home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('/admin_dashboard')
            else:
                return redirect('/home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('/login')

    return render(request, 'login.html')


def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')


def is_superuser(user):
    return user.is_superuser



@login_required
@user_passes_test(is_superuser)
def listuser(request):
    employees = CustomUser.objects.all()
    return render(request, 'listuser.html', {'employees': employees})


@login_required
@user_passes_test(is_superuser)
def userdetails(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    return render(request, 'userdetails.html', {'user': user})

@login_required
@user_passes_test(is_superuser)
def edit_employee(request):
    employees = CustomUser.objects.all()
    return render(request, 'edit_employee.html', {'employees': employees})


@login_required
@user_passes_test(is_superuser)
def edit_employee_detail(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        form = CustomUserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('edit_employee')
    else:
        form = CustomUserEditForm(instance=user)
    return render(request, 'edit_employee_detail.html', {'form': form})


@login_required
def delete_employee(request, pk):
    if not request.user.is_superuser:
        messages.error(request, "You are not authorized to delete employees.")
        return redirect('edit_employee')

    employee = get_object_or_404(CustomUser, pk=pk)
    employee.delete()
    messages.success(request, "Employee deleted successfully.")
    return redirect('edit_employee')



# api views
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer