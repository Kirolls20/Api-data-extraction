
//------------- countdown-----------------------------------//
     // Set the countdown duration in seconds
  // Set the countdown duration in seconds
  const countdownDuration = 30;

// Function to update the countdown
function updateCountdown() {
    // Set the date we're counting down to (current time + countdown duration)
    const countDownDate = new Date().getTime() + countdownDuration * 1000;

    // Update the countdown every 1 second
    const countdown = setInterval(function() {
        // Get the current date and time
        const now = new Date().getTime();

        // Calculate the time remaining
        const distance = countDownDate - now;

        // Calculate minutes and seconds
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Display the countdown
        document.getElementById("countdown").innerHTML = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;

        // If the countdown is over, reset the countdown
        if (distance < 0) {
            clearInterval(countdown);
            document.getElementById("countdown").innerHTML = '0:30';
            updateCountdown(); // Restart the countdown
        }
    }, 1000);
}

// Initial call to start the countdown
updateCountdown();