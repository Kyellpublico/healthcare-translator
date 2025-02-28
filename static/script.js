async function translateText() {
    const text = document.getElementById("inputText").value;
    const srcLang = document.getElementById("sourceLang").value;
    const destLang = document.getElementById("targetLang").value;

    if (!text.trim()) {
        alert("Please enter text to translate.");
        return;
    }

    try {
        const response = await fetch(`/translate/?text=${encodeURIComponent(text)}&src_lang=${srcLang}&dest_lang=${destLang}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" }
        });

        if (!response.ok) throw new Error("Translation failed");

        const data = await response.json();
        document.getElementById("translatedText").textContent = data.translated;
    } catch (error) {
        alert("Error: " + error.message);
    }
}

async function speakText() {
    const text = document.getElementById("translatedText").textContent;
    const lang = document.getElementById("targetLang").value;

    if (!text.trim()) {
        alert("No translated text to speak.");
        return;
    }

    try {
        const response = await fetch(`/speak/?text=${encodeURIComponent(text)}&lang=${lang}`);
        if (!response.ok) throw new Error("Text-to-speech failed");

        const audio = new Audio(response.url);
        audio.play();
    } catch (error) {
        alert("Error: " + error.message);
    }
}

function startSpeechRecognition() {
    if (!('webkitSpeechRecognition' in window)) {
        alert("Your browser does not support speech recognition. Try Google Chrome.");
        return;
    }

    const recognition = new webkitSpeechRecognition();
    recognition.lang = document.getElementById("sourceLang").value;
    recognition.interimResults = false;
    recognition.maxAlternatives = 1;

    recognition.onstart = function() {
        console.log("Listening...");
    };

    recognition.onspeechend = function() {
        recognition.stop();
    };

    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript;
        document.getElementById("inputText").value = transcript;
    };

    recognition.start();
}
