async function sendMessage() {
  let inputBox = document.getElementById("userInput");
  let userMessage = inputBox.value;

  if (!userMessage.trim()) return;

  document.getElementById("messages").innerHTML += `<p><b>You:</b> ${userMessage}</p>`;

  let response = await fetch("https://YOUR_BACKEND_URL/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: userMessage })
  });

  let data = await response.json();
  document.getElementById("messages").innerHTML += `<p><b>Bot:</b> ${data.reply}</p>`;

  inputBox.value = "";
}
