from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponse
from .models import Note

# Create your views here.
def delete_note_view(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return redirect(reverse('notes'))

def create_note(request):
    if request.method == "POST":
        # Captura os dados do formulário
        name_task = request.POST.get('taskTitle')
        description = request.POST.get('taskDescription')
        end_date = request.POST.get('taskDueDate')
        # Cria uma nova nota com os dados do formulário
        new_note = Note(
            name_task=name_task,
            description=description,
            end_date=end_date
        )
        new_note.save()  # Salva a nova nota no banco de dados
        
        return redirect(reverse('notes'))  # Redireciona para a página com a lista de notas
    
    return render(request, 'notes.html')  # Caso seja um GET, renderiza a página de notas


def notes(request):
    pending_notes = Note.objects.filter(completed=False)
    completed_notes = Note.objects.filter(completed=True)
    
        
        
    return render(request, 'notes.html', {'pending_notes': pending_notes, 'completed_notes': completed_notes})


def edit_note_view(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    
    if request.method == "POST":
        note.name_task = request.POST.get('taskTitle')
        note.description = request.POST.get('taskDescription')
        note.save()
        return redirect(reverse('notes'))
    
    return render(request, 'notes.html', {'note': note})


def toggle_completion_view(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.completed = not note.completed
    note.save()
    return redirect(reverse('notes'))
    