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
});
