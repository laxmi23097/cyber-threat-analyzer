async function checkThreat() {
    const duration = parseFloat(document.getElementById("duration").value);
    const protocol = parseInt(document.getElementById("protocol").value);
    const packets = parseFloat(document.getElementById("packets").value);

    const resultEl = document.getElementById("result");
    const containerEl = document.getElementById("result-container");

    if (isNaN(duration) || isNaN(protocol) || isNaN(packets)) {
        alert("Please enter valid numbers for all fields!");
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ duration, protocol, packets })
        });

        const data = await response.json();

        if (data.error) {
            resultEl.innerText = "Error: " + data.error;
            containerEl.className = "";
        } else {
            resultEl.innerText = "Prediction: " + data.prediction;

            // Add background + text color classes
            if (data.prediction === "Threat Detected") {
                containerEl.className = "threat";
            } else {
                containerEl.className = "normal";
            }
        }
    } catch (err) {
        resultEl.innerText = "Error connecting to server!";
        containerEl.className = "";
        console.error(err);
    }
}