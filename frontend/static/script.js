const API_URL = "http://localhost:8000";

async function loadTasks() {
  const res = await fetch(`${API_URL}/list`);
  const tasks = await res.json();
  const list = document.getElementById('taskList');
  list.innerHTML = '';

  for (const task of tasks) {
    const li = document.createElement('li');
    li.textContent = `${task.text} ${task.done ? '✔️' : ''}`;

    const doneBtn = document.createElement('button');
    doneBtn.textContent = '✔️';
    doneBtn.onclick = () => markDone(task.id);

    const delBtn = document.createElement('button');
    delBtn.textContent = '❌';
    delBtn.onclick = () => deleteTask(task.id);

    li.appendChild(doneBtn);
    li.appendChild(delBtn);
    list.appendChild(li);
  }
}

async function addTask() {
  const input = document.getElementById('taskInput');
  const text = input.value.trim();
  if (!text) return;
  await fetch(`${API_URL}/add?text=${encodeURIComponent(text)}`, {
    method: 'POST'
  });
  input.value = '';
  loadTasks();
}

async function markDone(id) {
  await fetch(`${API_URL}/done/${id}`, { method: 'POST' });
  loadTasks();
}

async function deleteTask(id) {
  await fetch(`${API_URL}/delete/${id}`, { method: 'DELETE' });
  loadTasks();
}

window.onload = loadTasks;
