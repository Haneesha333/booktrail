const recommendationsList = document.getElementById('recommendations');

function renderRecommendations(recommendations) {
    recommendationsList.innerHTML = '';

    recommendations.forEach(book => {
        const card = document.createElement('div');
        card.className = 'book-card';

        card.innerHTML = `
            <img src="${book.image_url}" alt="${book.title}">
            <h3>${book.title}</h3>
            <p><strong>Author:</strong> ${book.author}</p>
            <p><strong>Genre:</strong> ${book.genre}</p>
            <p>${book.description}</p>
        `;

        recommendationsList.appendChild(card);
    });
}

