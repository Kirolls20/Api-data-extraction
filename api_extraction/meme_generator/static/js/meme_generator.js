// JavaScript code to make an AJAX request after page load
document.addEventListener('DOMContentLoaded', function () {
    // Make an AJAX request to get the delayed names using fetch
    fetch('/delayed_name/')
        .then(response => response.json())
        .then(data => {
            var text = document.getElementById('text');
            var image = document.getElementById('pic');
            if (data.names) {
                
                // Update the list with the delayed names
                data.names.forEach(function (item,index) {
                        setTimeout(function () {
                            console.log(`text:${item.name} pic:${item.pic}`);
                            text.innerHTML = item.name
                            image.src = item.pic
                        }, index* 10000);
                            // 10000 milliseconds = 10 seconds
                });
            }
        })
        .catch(error => console.error('Error:', error));
});