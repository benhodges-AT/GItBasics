const actions = {
  sayHello() {
    console.log("Hello!");
    alert("Hello!");
  },

  openPage() {
    console.log("Open page action");
    // e.g. window.location.href = "other.html";
  },

  anotherAction() {
    console.log("Another button pressed");
  }
};

function handleButtonClick(event) {
  const action = event.currentTarget.dataset.action;
  if (!action) return;

  const fn = actions[action];
  if (typeof fn === "function") {
    fn();
  } else {
    console.warn(`No action found for ${action}`);
  }
}

function initButtons() {
  const buttons = document.querySelectorAll("button[data-action]");
  buttons.forEach((button) => {
    button.addEventListener("click", handleButtonClick);
  });
}

document.addEventListener("DOMContentLoaded", initButtons);