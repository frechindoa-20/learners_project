from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .models import Student

class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'
    paginate_by = 10

class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student_detail.html'
    context_object_name = 'student'

class StudentCreateView(SuccessMessageMixin, CreateView):
    model = Student
    template_name = 'students/student_form.html'
    fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'phone', 'address']
    success_url = reverse_lazy('students:student_list')
    success_message = "L'étudiant a été créé avec succès."

class StudentUpdateView(SuccessMessageMixin, UpdateView):
    model = Student
    template_name = 'students/student_form.html'
    fields = ['first_name', 'last_name', 'email', 'date_of_birth', 'phone', 'address']
    success_url = reverse_lazy('students:student_list')
    success_message = "Les modifications ont été enregistrées avec succès."

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('students:student_list')
    success_message = "L'étudiant a été supprimé avec succès."
    
    def delete(self, request, *args, **kwargs):
        from django.contrib import messages
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
