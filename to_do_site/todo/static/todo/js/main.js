var modal = document.getElementById("myModal");

var btn = document.getElementById("myBtn");

// Aqui, você deveria usar querySelector se você tem certeza de que há apenas um elemento com a classe 'close'.
var span = document.getElementsByClassName("close")[0];  // Corrigido: usando `getElementsByClassName` para pegar o primeiro elemento com a classe 'close'

btn.onclick = function() {
    modal.style.display = "block";
}

span.onclick = function () {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal){
        modal.style.display = "none";
    }
}

document.addEventListener("DOMContentLoaded", function() {
    // Referências para os modais e botões
    var createModal = document.getElementById("myModal");
    var taskModal = document.getElementById("taskModal");
    var btn = document.getElementById("myBtn");
    var closeCreateModal = document.querySelector("#myModal .close");
    var closeTaskModal = document.querySelector("#taskModal .close");

    // Botões e elementos do modal de tarefa
    var taskTitle = document.getElementById("taskTitle");
    var taskDescription = document.getElementById("taskDescription");
    var taskDueDate = document.getElementById("taskDueDate");
    var deleteTaskForm = document.getElementById("deleteTaskForm");

    // Abre o modal para criar nova tarefa
    btn.onclick = function() {
        createModal.style.display = "block";
    }

    // Fecha o modal de criação de nova tarefa
    closeCreateModal.onclick = function() {
        createModal.style.display = "none";
    }

    // Fecha o modal de tarefa existente
    closeTaskModal.onclick = function() {
        taskModal.style.display = "none";
    }

    // Fecha qualquer modal ao clicar fora do conteúdo
    window.onclick = function(event) {
        if (event.target == createModal) {
            createModal.style.display = "none";
        } else if (event.target == taskModal) {
            taskModal.style.display = "none";
        }
    }

    // Configuração do clique em uma tarefa na tabela
    var taskRows = document.getElementsByClassName("task-row");
    
    Array.from(taskRows).forEach(function(row) {
        row.onclick = function() {
            var taskId = this.getAttribute("data-id");
            var taskName = this.getAttribute("data-title");
            var taskDesc = this.getAttribute("data-description");
            var taskDate = this.getAttribute("data-duedate");

            // Preenchendo o modal com as informações da tarefa
            taskTitle.innerText = taskName;
            taskDescription.innerText = "Descrição: " + taskDesc;
            taskDueDate.innerText = "Data de Vencimento: " + taskDate;

            // Configurando o formulário de exclusão
            deleteTaskForm.action = "/todo/notes/delete/" + taskId + "/";

            // Mostrando o modal de visualização/exclusão de tarefa
            taskModal.style.display = "block";
        }
    });
});



