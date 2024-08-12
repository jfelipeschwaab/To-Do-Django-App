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

    const pendingTasksTable = document.getElementById("pendingTasksTable").querySelector("tbody");
    const completedTasksTable = document.getElementById("completedTasksTable").querySelector("tbody");


    // Configuração do clique em uma tarefa na tabela
    var taskRows = document.querySelectorAll(".task-row");

    taskRows.forEach(function(row) {
        // Adiciona o evento de clique na linha da tabela
        row.addEventListener('click', function(event) {
            // Verifica se o elemento clicado foi uma checkbox
            if (event.target.tagName.toLowerCase() === 'input' && event.target.type === 'checkbox') {
                // Se for uma checkbox, não faça nada (deixe o checkbox handle)
                return;
            }

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
        });
    });

    // Seleciona todas as checkboxes
    const checkboxes = document.querySelectorAll('.complete-checkbox');

    // Itera por cada checkbox para adicionar o event listener
    checkboxes.forEach(function(checkbox) {
        checkbox.addEventListener('change', function(event) {
            // Previne o clique na checkbox de abrir o modal
            event.stopPropagation();

            // Encontra a linha da tabela correspondente
            const row = this.closest('tr');

            // Seleciona o <td> que contém o nome da tarefa
            const taskNameCell = row.querySelector('td:nth-child(2)');

            // Adiciona ou remove a classe 'completed' ao <td> com base no estado da checkbox
            if (this.checked) {
                taskNameCell.classList.add('completed');
                row.classList.add('task-completed');
                completedTasksTable.appendChild(row);
            } else {
                taskNameCell.classList.remove('completed');
                row.classList.remove('task-completed');
                pendingTasksTable.appendChild(row);
            }
        });
    });
});
