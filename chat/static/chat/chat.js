// ===== CONFIG =====
const roomId = JSON.parse(document.getElementById("room-id").textContent);
const username = JSON.parse(document.getElementById("username").textContent);

// Auto switch ws / wss
const protocol = window.location.protocol === "https:" ? "wss" : "ws";
const socketUrl = `${protocol}://${window.location.host}/ws/chat/${roomId}/`;

// ===== SOCKET =====
const socket = new WebSocket(socketUrl);

// ===== ELEMENTS =====
const chatBox = document.getElementById("chat-box");
const messageInput = document.getElementById("message-input");
const sendBtn = document.getElementById("send-btn");

// ===== SOCKET EVENTS =====
socket.onopen = function () {
  console.log("✅ WebSocket connected");
};

socket.onmessage = function (e) {
  const data = JSON.parse(e.data);

  const msgDiv = document.createElement("div");
  msgDiv.classList.add("message");

  // Right/left alignment
  if (data.username === username) {
    msgDiv.classList.add("me");
  } else {
    msgDiv.classList.add("other");
  }

  msgDiv.innerHTML = `<b>${data.username}:</b> ${data.message}`;
  chatBox.appendChild(msgDiv);

  // Auto scroll
  chatBox.scrollTop = chatBox.scrollHeight;
};

socket.onerror = function (e) {
  console.error("❌ WebSocket error", e);
};

socket.onclose = function () {
  console.warn("⚠️ WebSocket closed");
};

// ===== SEND MESSAGE =====
function sendMessage() {
  const message = messageInput.value.trim();

  if (!message) return;

  socket.send(JSON.stringify({
    message: message,
  }));

  messageInput.value = "";
}

// ===== EVENTS =====
sendBtn.onclick = sendMessage;

messageInput.addEventListener("keyup", function (e) {
  if (e.key === "Enter") {
    sendMessage();
  }
});
