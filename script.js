let secretNumber = Math.floor(Math.random() * 100) + 1;
let attempts = 0;
const maxAttempts = 5; // isku dayada ugu badan

const guessInput = document.getElementById("guessInput");
const guessBtn = document.getElementById("guessBtn");
const message = document.getElementById("message");
const attemptsDisplay = document.getElementById("attempts");
const restartBtn = document.getElementById("restartBtn");

guessBtn.addEventListener("click", () => {
    const userGuess = Number(guessInput.value);
    attempts++;

    if (!userGuess || userGuess < 1 || userGuess > 100) {
        message.textContent = "⚠ Please enter a number between 1 and 100!";
        return;
    }

    if (userGuess === secretNumber) {
        message.textContent = `🎉 Correct! The number was ${secretNumber}.`;
        message.style.color = "#00ff99";
        endGame();
    } 
    else if (userGuess > secretNumber) {
        message.textContent = "📉 Too high! Try again.";
        message.style.color = "#ffcc00";
    } 
    else {
        message.textContent = "📈 Too low! Try again.";
        message.style.color = "#ffcc00";
    }

    attemptsDisplay.textContent = `Attempts: ${attempts} / ${maxAttempts}`;

    // Check if attempts are finished
    if (attempts >= maxAttempts && userGuess !== secretNumber) {
        message.textContent = ` Game Over! The number was ${secretNumber}.`;
        message.style.color = "#ff4d4d";
        endGame();
    }

    guessInput.value = "";
});

function endGame() {
    guessBtn.disabled = true;
    guessInput.disabled = true;
    restartBtn.style.display = "inline-block";
}

restartBtn.addEventListener("click", () => {
    secretNumber = Math.floor(Math.random() * 100) + 1;
    attempts = 0;
    attemptsDisplay.textContent = `Attempts: 0 / ${maxAttempts}`;
    message.textContent = "";
    guessBtn.disabled = false;
    guessInput.disabled = false;
    guessInput.value = "";
    restartBtn.style.display = "none";
});
