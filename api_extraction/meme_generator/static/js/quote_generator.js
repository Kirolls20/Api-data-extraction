// Make Ajax request 
document.addEventListener('DOMContentLoaded',function(){
    fetch('/quote-api/')
        .then(response => response.json())
        .then(data => {
            console.log(data.quotes)
            var quote = document.getElementById('quote');
            var author = document.getElementById('author');
            if (data.quotes){
                data.quotes.forEach(function(item,index){
                    setTimeout( () => {
                        console.log(item.quote)
                        quote.innerHTML = item.quote;
                        author.innerHTML = item.author;
                    }, index*28000);
                })
            }
        })
        .catch(error => console.error('Error:', error));
});
