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
