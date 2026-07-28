document.getElementById("chatForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const input = document.getElementById("userInput");
    const text = input.value.trim();

    if (!text) return;

    // 1. Mostrar mensaje del usuario
    appendMsg(text, "user");
    input.value = "";

    // 2. Mensaje temporal de carga
    const loading = appendMsg("Pensando...", "bot");

    // 3. BLOQUE TRY: Aquí va la llamada al servidor y el procesamiento
    try {
        const res = await fetch("/api/pregunta", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ pregunta: text })
        });

        const data = await res.json();
        
        // Imprime en la consola F12 lo que responde el servidor para diagnosticar si es necesario
        console.log("Respuesta del servidor:", data);

        if (res.ok) {
            // Buscamos 'data.respuesta' o 'data.response' por si acaso, y si no existe, mostramos mensaje de respaldo
            const textoFinal = data.respuesta || data.response || "No se obtuvo respuesta del asistente.";
            loading.innerText = textoFinal;
        } else {
            loading.innerText = "❌ Error: " + (data.error || "Ocurrió un problema en el servidor.");
        }
        } catch (err) {
        // BLOQUE CATCH: Solo se ejecuta si no hay internet o el servidor Flask está apagado
        console.error("Error en fetch:", err);
        loading.innerText = "❌ Error al conectar con el servidor. Verifica que Flask esté corriendo.";
    }
});

function appendMsg(text, sender) {
    const chatBox = document.getElementById("chatBox");
    const div = document.createElement("div");
    div.className = `message ${sender}`;
    div.innerText = text;
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
    return div;
}