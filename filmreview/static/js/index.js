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
    // Overview truncation and "Read more" functionality
    const overviewElement = document.getElementById('movie-overview');
    const readMoreButton = document.getElementById('read-more-button');
    const maxLength = 250;
    const fullText = overviewElement ? overviewElement.textContent.trim() : '';

    if (overviewElement && readMoreButton && fullText.length > maxLength) {
        const truncatedText = fullText.substring(0, maxLength) + '... ';
        overviewElement.textContent = truncatedText;
        readMoreButton.classList.remove('hidden');

        readMoreButton.addEventListener('click', function() {
            console.log('Read more button clicked'); 
            if (readMoreButton.innerText === 'Read more') {
                overviewElement.textContent = fullText;
                readMoreButton.innerText = 'Read less';
            } else {
                overviewElement.textContent = truncatedText;
                readMoreButton.innerText = 'Read more';
            }
        });
    }

    // Search suggestions functionality
    var searchInput = document.getElementById('nav-search-bar');

    if (searchInput) {
        searchInput.addEventListener('keyup', function() {
            var query = this.value;
            if (query.length > 1) {
                fetch(`/film/search_suggestions/?query=${encodeURIComponent(query)}`)
                .then(response => response.json())
                .then(suggestions => {
                    displaySuggestions(suggestions);
                })
                .catch(error => console.error('Error fetching suggestions:', error));
            } else {
                clearSuggestions();
            }
        });
    }

    function displaySuggestions(suggestions) {
        var suggestionsList = document.getElementById('suggestions');
        suggestionsList.innerHTML = '';
        suggestions.forEach(function(movie) {
            var li = document.createElement('li');
            
            var img = document.createElement('img');
            img.src = movie.poster_path || 'path/to/default_image.jpg';
            img.alt = movie.title;
            img.width = 80;

            var link = document.createElement('a');
            link.href = `/film/movie/${movie.id}/`;
            link.innerHTML = `${movie.title}<br>${movie.release_date}`;


            li.appendChild(img);
            li.appendChild(link);
            suggestionsList.appendChild(li);

            li.addEventListener('click', function() {
                window.location.href = link.href;
            });
        });
    }

    function clearSuggestions() {
        var suggestionsList = document.getElementById('suggestions');
        suggestionsList.innerHTML = '';
    }
});
