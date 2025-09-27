document.addEventListener('DOMContentLoaded', function () {
    const modifierLivreLinks = document.querySelectorAll('.modifier-livre');

    modifierLivreLinks.forEach(link => {
        link.addEventListener('click', function (event) {
            event.preventDefault();

            // Fetch book details using this.getAttribute('data-id') if needed

            const modifierLivreModal = new bootstrap.Modal(document.getElementById('modifierLivreModal'));
            modifierLivreModal.show();
        });
    });

    document.getElementById('editBookForm').addEventListener('submit', function(event) {
        event.preventDefault();

        const bookId = document.getElementById('editBookModal').getAttribute('data-book-id');
        const formData = {
            title: document.getElementById('editBookTitle').value,
            author: document.getElementById('editBookAuthor').value,
            category: document.getElementById('editBookCategory').value,
            isbn: document.getElementById('editBookISBN').value,
            publication_year: document.getElementById('editBookPublicationYear').value,
            publisher: document.getElementById('editBookPublisher').value,
            quantity: document.getElementById('editBookQuantity').value
        };

        fetch(`/books/update/${bookId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Livre modifié avec succès');
                location.reload();
            } else {
                alert(`Erreur: ${data.message}`);
            }
        })
        .catch(error => {
            console.error('Erreur:', error);
            alert('Une erreur inattendue s\'est produite');
        });
    });
});
