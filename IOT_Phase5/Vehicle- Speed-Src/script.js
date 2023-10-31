document.addEventListener("DOMContentLoaded", function () {
    const speedDisplay = document.getElementById("speed");
    const startButton = document.getElementById("startButton");
    const stopButton = document.getElementById("stopButton");
    let measuring = false;
    let speed = 0;

    startButton.addEventListener("click", function () {
        if (!measuring) {
            measuring = true;
            simulateSpeedMeasurement();
            startButton.disabled = true;
            stopButton.disabled = false;
        }
    });

    stopButton.addEventListener("click", function () {
        if (measuring) {
            measuring = false;
            clearInterval(speedUpdateInterval);
            startButton.disabled = false;
            stopButton.disabled = true;
        }
    });

    function simulateSpeedMeasurement() {
        const speedUpdateInterval = setInterval(function () {
            // Simulate speed measurement (replace with actual sensor data)
            speed = Math.floor(Math.random() * 100); // Random speed between 0 and 99 km/h

            // Update the speed display
            speedDisplay.innerText = speed;
        }, 1000); // Update every 1 second
    }
});
