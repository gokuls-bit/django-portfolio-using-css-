# myapp/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

def home(request):
    """
    Renders the main portfolio homepage.
    """
    # For this version, project data is hardcoded directly in the template
    # to match the prompt's detailed list. If you were using the Project model,
    # you would query the database here.
    
    projects_data = [
        { "title": "Stitch & Style", "tech": "WordPress, WooCommerce", "desc": "E-commerce website with product pages & payment gateway.", "git": "#", "demo": "#" },
        { "title": "E-Notice Board", "tech": "React.js, PHP, MySQL", "desc": "Digital notice board for real-time campus communication.", "git": "#", "demo": "#" },
        { "title": "Finance Tracker", "tech": "Django, Chart.js, PostgreSQL", "desc": "Expense tracker with analytics dashboards.", "git": "#", "demo": "#" },
        { "title": "Furnimart Chatbox", "tech": "MERN, Socket.IO", "desc": "Real-time chat app with categorized users.", "git": "#", "demo": "#" },
        { "title": "Bhagwat Praptati", "tech": "Next.js, MongoDB", "desc": "Chant-tracking app with progress charts & reminders.", "git": "#", "demo": "#" },
        { "title": "Password Generator", "tech": "Next.js, Vite", "desc": "Secure password generator with strength meter.", "git": "#", "demo": "#" },
        { "title": "Project Management Tool", "tech": "React, Node.js, PostgreSQL", "desc": "Kanban-style team management tool.", "git": "#", "demo": "#" },
        { "title": "E-Commerce Website", "tech": "React, Node.js, MongoDB", "desc": "Full-stack store with authentication.", "git": "#", "demo": "#" },
        { "title": "Portfolio Website", "tech": "Next.js, Tailwind CSS", "desc": "Responsive personal portfolio.", "git": "#", "demo": "#" },
        { "title": "DCGAN Fashion-MNIST", "tech": "TensorFlow", "desc": "GAN generating synthetic fashion items.", "git": "#", "demo": "#" },
        { "title": "CNN Image Classifier", "tech": "Keras", "desc": "Custom dataset classification with CNN.", "git": "#", "demo": "#" },
        { "title": "AI Reintegration Guide", "tech": "LLM App", "desc": "Chatbot for refugee reintegration programs.", "git": "#", "demo": "#" },
        { "title": "Library DBMS", "tech": "MySQL", "desc": "ER model, relational schema, and advanced queries.", "git": "#", "demo": "#" },
        { "title": "Student Attendance System", "tech": "Django, SQLite", "desc": "Faculty dashboard for attendance.", "git": "#", "demo": "#" },
        { "title": "Online Voting System", "tech": "PHP, MySQL", "desc": "Secure web-based voting platform.", "git": "#", "demo": "#" },
        { "title": "Weather Dashboard", "tech": "React, API", "desc": "Live weather search using OpenWeather API.", "git": "#", "demo": "#" },
        { "title": "Quiz App", "tech": "React, Firebase", "desc": "Real-time quiz system with score tracking.", "git": "#", "demo": "#" },
        { "title": "Music Playlist Manager", "tech": "Node.js, MongoDB", "desc": "CRUD app for managing playlists.", "git": "#", "demo": "#" }
    ]

    context = {
        'projects': projects_data
    }
    return render(request, 'home.html', context)

def contact_submit(request):
    """
    Handles the submission of the contact form.
    Saves the message to the database and displays a success message.
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_text = request.POST.get('message')

        # Basic validation
        if name and email and message_text:
            # Create and save the contact message instance
            ContactMessage.objects.create(
                name=name,
                email=email,
                message=message_text
            )
            # Add a success message to be displayed on the page
            messages.success(request, 'Your message has been sent successfully! I will get back to you soon.')
        else:
            # Add an error message if fields are missing
            messages.error(request, 'Please fill out all fields in the form.')
        
        # Redirect back to the home page, appending the contact section hash
        return redirect('/#contact')
    
    # If not a POST request, just redirect to home
    return redirect('home')

# Create your views here.
