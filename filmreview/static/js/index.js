//Change movie rating's text based on the given movie's rating
document.addEventListener('DOMContentLoaded', function() {
    var ratingElements = document.querySelectorAll('.index-movie-rating');

    ratingElements.forEach(function(ratingElement) {
        var ratingText = ratingElement.textContent.trim();
        var rating = parseFloat(ratingText.replace('%', ''));

        if (rating > 75) {
            ratingElement.style.color = 'green';  
        } else if (rating > 60) {
            ratingElement.style.color = 'orange'; 
        } else {
            ratingElement.style.color = 'red'; 
        }
    });
});

// Read more button for a movie's overview, or a person's biography, if exceeds character limit
document.addEventListener("DOMContentLoaded", function() {
    const overviewElement = document.getElementById('movie-overview');
    const readMoreButton = document.getElementById('read-more-button');
    const maxLength = 250;
    const fullText = overviewElement.textContent.trim();

    if (fullText.length > maxLength) {
        const truncatedText = fullText.substring(0, maxLength) + '... ';
        overviewElement.textContent = truncatedText;
        readMoreButton.classList.remove('hidden');

        readMoreButton.addEventListener('click', function() {
            if (readMoreButton.innerText === 'Read more') {
                overviewElement.textContent = fullText;
                readMoreButton.innerText = 'Read less';
            } else {
                overviewElement.textContent = truncatedText;
                readMoreButton.innerText = 'Read more';
            }
        });
    }
});