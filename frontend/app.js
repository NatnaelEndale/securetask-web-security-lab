"use strict";

/*
 * SecureTask — Frontend Application
 *
 * M2.3: Task Rendering and Application State
 */

const STORAGE_KEY = "securetask.tasks.v1";

// ----------------------------------------
// 1. Application State
// ----------------------------------------

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
    searchQuery: ""
};


// ----------------------------------------
// 2. DOM References
// ----------------------------------------

const taskListElement = document.querySelector("#task-list");

const totalTasksElement =
    document.querySelector("#total-tasks");

const activeTasksElement =
    document.querySelector("#active-tasks");

const completedTasksElement =
    document.querySelector("#completed-tasks");

const taskCountElement =
    document.querySelector("#task-count");


// ----------------------------------------
// 3. Render a Single Task
// ----------------------------------------

function createTaskCard(task) {

    const article = document.createElement("article");

    article.className = "task-card";

    if (task.completed) {
        article.classList.add("is-completed");
    }

    const header = document.createElement("div");
    header.className = "task-card-header";

    const title = document.createElement("h3");

    // Use textContent rather than innerHTML.
    title.textContent = task.title;

    const status = document.createElement("span");

    status.className = task.completed
        ? "task-status completed"
        : "task-status active";

    status.textContent = task.completed
        ? "Completed"
        : "Active";

    const description = document.createElement("p");

    description.textContent = task.description;

    header.append(title, status);

    article.append(header, description);

    return article;
}


// ----------------------------------------
// 4. Render All Tasks
// ----------------------------------------

function renderTasks() {

    taskListElement.replaceChildren();

    if (state.tasks.length === 0) {

        const emptyState = document.createElement("div");
        emptyState.className = "empty-state";

        const heading = document.createElement("h3");
        heading.textContent = "No tasks yet";

        const description = document.createElement("p");

        description.textContent =
            "Your tasks will appear here. Start organizing your work in SecureTask.";

        emptyState.append(heading, description);

        taskListElement.append(emptyState);

        return;
    }

    for (const task of state.tasks) {

        const taskCard = createTaskCard(task);

        taskListElement.append(taskCard);
    }
}


// ----------------------------------------
// 5. Update Dashboard Statistics
// ----------------------------------------

function updateStatistics() {

    const total = state.tasks.length;

    const completed = state.tasks.filter(
        task => task.completed
    ).length;

    const active = total - completed;

    totalTasksElement.textContent = total;

    activeTasksElement.textContent = active;

    completedTasksElement.textContent = completed;

    taskCountElement.textContent =
        `${total} ${total === 1 ? "task" : "tasks"}`;
}


// ----------------------------------------
// 6. Render Dashboard
// ----------------------------------------

function renderDashboard() {

    renderTasks();

    updateStatistics();
}


// ----------------------------------------
// 7. Initialize Application
// ----------------------------------------

function initializeApp() {

    console.log("SecureTask frontend initialized.");

    renderDashboard();

    console.log("Application state:", state);
}

initializeApp();
