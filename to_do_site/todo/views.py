from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Note

"""
Este módulo contém as views para a aplicação de lista de tarefas.
Inclui funcionalidades de criação, edição, visualização e exclusão de tarefas.
"""

def delete_note_view(_request, note_id):
    """
    Exclui uma nota especificada pelo ID e redireciona para a lista de notas.
    """
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return redirect(reverse('notes'))

def create_note(request):
    """
    Cria uma nova nota com base nos dados do formulário POST.
    """
    if request.method == "POST":
        name_task = request.POST.get('taskTitle')
        description = request.POST.get('taskDescription')
        end_date = request.POST.get('taskDueDate')
        
        new_note = Note(
            name_task=name_task,
            description=description,
            end_date=end_date
        )
        new_note.save()
        
        return redirect(reverse('notes'))
    
    return render(request, 'notes.html')

def notes(request):
    """
    Renderiza a página de notas, exibindo notas pendentes e concluídas.
    """
    pending_notes = Note.objects.filter(completed=False)
    completed_notes = Note.objects.filter(completed=True)
    
    return render(request, 'notes.html', {'pending_notes': pending_notes, 'completed_notes': completed_notes})

def edit_note_view(request, note_id):
    """
    Permite a edição de uma nota existente.
    """
    note = get_object_or_404(Note, id=note_id)
    
    if request.method == "POST":
        note.name_task = request.POST.get('taskTitle')
        note.description = request.POST.get('taskDescription')
        note.save()
        return redirect(reverse('notes'))
    
    return render(request, 'notes.html', {'note': note})

def toggle_completion_view(_request, note_id):
    """
    Alterna o status de conclusão de uma nota e redireciona para a lista de notas.
    """
    note = get_object_or_404(Note, id=note_id)
    note.completed = not note.completed
    note.save()
    return redirect(reverse('notes'))
