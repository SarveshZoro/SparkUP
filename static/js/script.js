async function sendMessage() {
  const userInput = document.getElementById("user-input");
  const message = userInput.value.trim();
  if (!message) return;

  const chatBox = document.getElementById("chat-box");

  // Display user message
  chatBox.innerHTML += `<p><strong>You:</strong> ${message}</p>`;
  userInput.value = "";

  try {
    const response = await fetch("/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message }),
    });

    const data = await response.json();
    chatBox.innerHTML += `<p><strong>Bot:</strong> ${data.reply}</p>`;
    chatBox.scrollTop = chatBox.scrollHeight;
  } catch (err) {
    chatBox.innerHTML += `<p><strong>Bot:</strong> ❌ Error talking to the assistant.</p>`;
  }
}
