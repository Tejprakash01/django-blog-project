const socket = new WebSocket(
  `ws://${window.location.host}/ws/chat/${roomId}/`
);

socket.onmessage = function(e) {
  const data = JSON.parse(e.data);
  const box = document.getElementById("chat-box");

  box.innerHTML += `<div><b>${data.username}:</b> ${data.message}</div>`;
};

function sendMessage() {
  const input = document.getElementById("message-input");
  socket.send(JSON.stringify({
    message: input.value
  }));
  input.value = "";
}
