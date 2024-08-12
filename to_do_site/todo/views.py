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
        name_task = request.POST.get('name_task')
        description = request.POST.get('description')
        end_date = request.POST.get('end_date')
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
    all_notes = Note.objects.all() ##Retorna todas as notas
    for note in all_notes:
        print(f"ID: {note.id}, Tarefa: {note.name_task}, Descrição: {note.description}, Data de criação: {note.created_date}")
        
        
    return render(request, 'notes.html', {'notes': all_notes})

    