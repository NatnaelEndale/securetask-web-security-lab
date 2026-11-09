
"use strict";

/*
 * SecureTask — Frontend Application
 *
 * M2.4: Task Interactions
 *
 * Features:
 * - Render tasks
 * - Calculate dashboard statistics
 * - Complete and restore tasks
 * - Delete tasks
 */

const STORAGE_KEY = "securetask.tasks.v1";


// 1. Application State
// ========================================

const state = {
    tasks: [
        {
            id: "task-001",
            title: "Review network architecture",
            description:
                "Verify NAT, Host-only adapters, and static IP assignments.",
            completed: true,
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString()
        },
        {
            id: "task-002",
            title: "Study JavaScript DOM manipulation",
            description:
                "Practice selecting and updating HTML elements.",
            completed: false,
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString()
        },
        {
            id: "task-003",
            title: "Review HTTP fundamentals",
            description:
                "Understand HTTP requests, responses, and status codes.",
            completed: false,
            createdAt: new Date().toISOString(),
            updatedAt: new Date().toISOString()
        }
    ],

    filter: "all",
    searchQuery: "",
    editingTaskId: null
};

function persistTasks() {
    try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(state.tasks));
    } catch (error) {
        console.error("Unable to save tasks.", error);
    }
}

function loadTasks() {
    try {
        const storedTasks = localStorage.getItem(STORAGE_KEY);

        if (storedTasks === null) {
            return;
        }

        const parsedTasks = JSON.parse(storedTasks);

        if (!Array.isArray(parsedTasks)) {
            throw new Error("Stored tasks are not an array.");
        }

        state.tasks = parsedTasks;
    } catch (error) {
        console.error("Unable to load saved tasks.", error);
    }
}

function createTaskId() {
    if (typeof crypto !== "undefined" &&
        typeof crypto.randomUUID === "function") {
        return crypto.randomUUID();
    }

    return `task-${Date.now()}-${Math.random().toString(36).slice(2)}`;
}


// ========================================
// 2. DOM References
// ========================================

const taskListElement = document.querySelector("#task-list");

const totalTasksElement =
    document.querySelector("#total-tasks");

const activeTasksElement =
    document.querySelector("#active-tasks");

const completedTasksElement =
    document.querySelector("#completed-tasks");

const taskCountElement =
    document.querySelector("#task-count");
const addTaskButton =
    document.querySelector("#add-task-button");

const taskFormElement =
    document.querySelector("#task-form");

const taskTitleInput =
    document.querySelector("#task-title");

const taskDescriptionInput =
    document.querySelector("#task-description");

const taskFormHeading =
    document.querySelector("#task-form-heading");

const submitTaskButton =
    document.querySelector("#submit-task-button");

const cancelTaskButton =
    document.querySelector("#cancel-task-button");
const taskSearchInput =
    document.querySelector("#task-search");

const taskFilterSelect =
    document.querySelector("#task-filter");


// ========================================
// 3. Create a Task Card
// ========================================

function createTaskCard(task) {

    const article = document.createElement("article");

    article.className = "task-card";

    if (task.completed) {
        article.classList.add("is-completed");
    }

    // Task heading
    const header = document.createElement("div");
    header.className = "task-card-header";

    const title = document.createElement("h3");
    title.textContent = task.title;

    // Completion status
    const status = document.createElement("span");

    status.className = task.completed
        ? "task-status completed"
        : "task-status active";

    status.textContent = task.completed
        ? "Completed"
        : "Active";

    header.append(title, status);

    // Task description
    const description = document.createElement("p");
    description.textContent = task.description;

    // Action buttons
    const actions = document.createElement("div");
    actions.className = "task-actions";

    const toggleButton = document.createElement("button");

    toggleButton.type = "button";
    toggleButton.className = "task-action-button";

    toggleButton.dataset.action = "toggle";
    toggleButton.dataset.taskId = task.id;

    toggleButton.textContent = task.completed
        ? "Mark active"
        : "Mark complete";

    toggleButton.setAttribute(
        "aria-label",
        `${task.completed ? "Restore" : "Complete"} task: ${task.title}`
    );

    const editButton = document.createElement("button");

    editButton.type = "button";
    editButton.className = "task-action-button";

    editButton.dataset.action = "edit";
    editButton.dataset.taskId = task.id;

    editButton.textContent = "Edit";

    const deleteButton = document.createElement("button");

    deleteButton.type = "button";
    deleteButton.className =
        "task-action-button delete-button";

    deleteButton.dataset.action = "delete";
    deleteButton.dataset.taskId = task.id;

    deleteButton.textContent = "Delete";

    deleteButton.setAttribute(
        "aria-label",
        `Delete task: ${task.title}`
    );

    actions.append(toggleButton, editButton, deleteButton);

    article.append(header, description, actions);

    return article;
}

// ========================================
// 4.Get Filtered Tasks
// ========================================

function getFilteredTasks() {

    const query = state.searchQuery
        .trim()
        .toLowerCase();

    return state.tasks.filter(task => {

        // Filter by completion status.
        const matchesFilter =
            state.filter === "all" ||
            (state.filter === "active" && !task.completed) ||
            (state.filter === "completed" && task.completed);

        // Search title and description.
        const matchesSearch =
            task.title.toLowerCase().includes(query) ||
            task.description.toLowerCase().includes(query);

        return matchesFilter && matchesSearch;
    });
}

// ========================================
// 5. Render All Tasks
// ========================================

function renderTasks() {

    taskListElement.replaceChildren();

    const visibleTasks = getFilteredTasks();

    // No tasks exist in the application.
    if (state.tasks.length === 0) {

        const emptyState = document.createElement("div");
        emptyState.className = "empty-state";

        const heading = document.createElement("h3");
        heading.textContent = "No tasks yet";

        const description = document.createElement("p");
        description.textContent =
            "Create your first task to get started.";

        emptyState.append(heading, description);
        taskListElement.append(emptyState);

        return;
    }

    // Tasks exist, but none match the search/filter.
    if (visibleTasks.length === 0) {

        const emptyState = document.createElement("div");
        emptyState.className = "empty-state";

        const heading = document.createElement("h3");
        heading.textContent = "No matching tasks";

        const description = document.createElement("p");
        description.textContent =
            "Try another search term or change your filter.";

        emptyState.append(heading, description);
        taskListElement.append(emptyState);

        return;
    }

    // Display matching tasks.
    for (const task of visibleTasks) {

        const taskCard = createTaskCard(task);

        taskListElement.append(taskCard);
    }
}

// ========================================
// 6. Update Dashboard Statistics
// ========================================

function updateStatistics() {

    const total = state.tasks.length;

    const completed = state.tasks.filter(
        task => task.completed
    ).length;

    const active = total - completed;

    totalTasksElement.textContent = total;

    activeTasksElement.textContent = active;

    completedTasksElement.textContent = completed;

    const visibleCount = getFilteredTasks().length;

    taskCountElement.textContent =
       visibleCount === total
          ? `${total} ${total === 1 ? "task" : "tasks"}`
          : `${visibleCount} of ${total} tasks`;
}


// ========================================
// 7. Render Dashboard
// ========================================

function renderDashboard() {

    renderTasks();

    updateStatistics();
}


// ========================================
// 8. Handle Task Interactions
// ========================================

function handleTaskAction(event) {

    const button = event.target.closest(
        "button[data-action]"
    );

    // Ignore clicks that aren't on our action buttons.
    if (!button || !taskListElement.contains(button)) {
        return;
    }

    const taskId = button.dataset.taskId;
    const action = button.dataset.action;

    const task = state.tasks.find(
        item => item.id === taskId
    );

    // Make sure the task still exists.
    if (!task) {
        return;
    }

    // Handle editing an existing task.
    if (action === "edit") {
        openTaskForm(task);
        return;
    }

    // Complete or restore a task.
    if (action === "toggle") {

        task.completed = !task.completed;

        task.updatedAt = new Date().toISOString();

        console.log(
            `Task "${task.title}" is now ${
                task.completed ? "completed" : "active"
            }.`
        );

        persistTasks();
        renderDashboard();

        return;
    }

    // Delete a task.
    if (action === "delete") {

        const confirmed = window.confirm(
            `Are you sure you want to delete "${task.title}"?`
        );

        if (!confirmed) {
            return;
        }

        state.tasks = state.tasks.filter(
            item => item.id !== taskId
        );

        console.log(`Task "${task.title}" deleted.`);

        persistTasks();
        renderDashboard();
    }
}


// ========================================
// 9. Create and Edit Tasks
// ========================================

function openTaskForm(task = null) {

    state.editingTaskId = task?.id ?? null;

    const isEditing = task !== null;

    taskFormHeading.textContent = isEditing
        ? "Edit task"
        : "Create a task";

    submitTaskButton.textContent = isEditing
        ? "Save changes"
        : "Create task";

    taskTitleInput.value = task?.title ?? "";

    taskDescriptionInput.value =
        task?.description ?? "";

    taskFormElement.hidden = false;

    taskTitleInput.focus();
}


function closeTaskForm() {

    taskFormElement.hidden = true;

    taskFormElement.reset();

    state.editingTaskId = null;
}


function handleTaskFormSubmit(event) {

    event.preventDefault();

    const title = taskTitleInput.value.trim();

    const description =
        taskDescriptionInput.value.trim();

    // Reject empty or whitespace-only titles.
    if (!title) {

        taskTitleInput.setCustomValidity(
            "Please enter a task title."
        );

        taskTitleInput.reportValidity();

        taskTitleInput.setCustomValidity("");

        return;
    }

    const now = new Date().toISOString();

    // Editing an existing task.
    if (state.editingTaskId !== null) {

        const task = state.tasks.find(
            item => item.id === state.editingTaskId
        );

        if (!task) {
            console.error("Task not found.");
            closeTaskForm();
            return;
        }

        task.title = title;
        task.description = description;
        task.updatedAt = now;

        console.log(`Task "${title}" updated.`);

    } else {

        // Creating a new task.
        const newTask = {
            id: createTaskId(),

            title: title,

            description: description,

            completed: false,

            createdAt: now,

            updatedAt: now
        };

        state.tasks.unshift(newTask);

        console.log(`Task "${title}" created.`);
    }

    closeTaskForm();

    persistTasks();
    renderDashboard();
}


// ========================================
// 10. Initialize Application
// ========================================

function initializeApp() {

    console.log("SecureTask frontend initialized.");

    loadTasks();

    // One event listener handles all task action buttons.
    taskListElement.addEventListener(
        "click",
        handleTaskAction
    );
    addTaskButton.addEventListener(
        "click",
        () => openTaskForm()
    );

    cancelTaskButton.addEventListener(
        "click",
        closeTaskForm
    );

    taskFormElement.addEventListener(
        "submit",
        handleTaskFormSubmit
    );
    taskSearchInput.addEventListener("input", () => {

       state.searchQuery = taskSearchInput.value;

       renderDashboard();

    });


    taskFilterSelect.addEventListener("change", () => {

       state.filter = taskFilterSelect.value;

       renderDashboard();

    });
    renderDashboard();

    console.log("Application state:", state);
}

initializeApp();
