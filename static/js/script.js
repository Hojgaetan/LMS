document.addEventListener('DOMContentLoaded', function () {
    // Animation d'entrée pour les éléments
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Observer tous les éléments avec animation
    document.querySelectorAll('.card, .table-responsive').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'all 0.6s cubic-bezier(0.4, 0, 0.2, 1)';
        observer.observe(el);
    });

    // Effet de parallaxe subtil pour les cartes
    document.addEventListener('mousemove', (e) => {
        const cards = document.querySelectorAll('.stats-card');
        const mouseX = e.clientX / window.innerWidth;
        const mouseY = e.clientY / window.innerHeight;

        cards.forEach((card, index) => {
            const speed = (index + 1) * 0.5;
            const x = (mouseX - 0.5) * speed;
            const y = (mouseY - 0.5) * speed;
            
            card.style.transform = `translate(${x}px, ${y}px)`;
        });
    });

    // Gestion des modals avec animations améliorées
    const modifierLivreLinks = document.querySelectorAll('.modifier-livre');

    modifierLivreLinks.forEach(link => {
        link.addEventListener('click', function (event) {
            event.preventDefault();
            const modifierLivreModal = new bootstrap.Modal(document.getElementById('modifierLivreModal'));
            modifierLivreModal.show();
        });
    });

    // Amélioration du formulaire d'édition avec validation en temps réel
    document.getElementById('editBookForm').addEventListener('submit', function(event) {
        event.preventDefault();

        // Animation de chargement
        const submitBtn = this.querySelector('button[type="submit"]');
        const originalText = submitBtn.innerHTML;
        submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status"></span>Modification...';
        submitBtn.disabled = true;

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
                showNotification('Livre modifié avec succès', 'success');
                location.reload();
            } else {
                showNotification(`Erreur: ${data.message}`, 'error');
            }
        })
        .catch(error => {
            console.error('Erreur:', error);
            showNotification('Une erreur inattendue s\'est produite', 'error');
        })
        .finally(() => {
            submitBtn.innerHTML = originalText;
            submitBtn.disabled = false;
        });
    });

    // Fonction pour afficher des notifications modernes
    function showNotification(message, type = 'info') {
        const toastContainer = document.querySelector('.toast-container');
        const toastId = 'toast-' + Date.now();
        
        const iconMap = {
            success: 'bi-check-circle-fill',
            error: 'bi-exclamation-triangle-fill',
            warning: 'bi-exclamation-circle-fill',
            info: 'bi-info-circle-fill'
        };

        const colorMap = {
            success: 'text-bg-success',
            error: 'text-bg-danger',
            warning: 'text-bg-warning',
            info: 'text-bg-info'
        };

        const toastHTML = `
            <div id="${toastId}" class="toast align-items-center ${colorMap[type]} border-0" role="alert" aria-live="assertive" aria-atomic="true">
                <div class="d-flex">
                    <div class="toast-body d-flex align-items-center">
                        <i class="bi ${iconMap[type]} me-2"></i>
                        ${message}
                    </div>
                    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
            </div>
        `;
        
        toastContainer.insertAdjacentHTML('beforeend', toastHTML);
        
        const toastElement = document.getElementById(toastId);
        const bsToast = new bootstrap.Toast(toastElement, {
            autohide: true,
            delay: 5000
        });
        
        toastElement.addEventListener('hidden.bs.toast', function () {
            toastElement.remove();
        });
        
        bsToast.show();
    }

    // Amélioration des interactions avec les boutons
    document.querySelectorAll('.btn').forEach(btn => {
        btn.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
        });
        
        btn.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });

    // Effet de typing pour les titres (optionnel)
    function typeWriter(element, text, speed = 100) {
        let i = 0;
        element.innerHTML = '';
        
        function type() {
            if (i < text.length) {
                element.innerHTML += text.charAt(i);
                i++;
                setTimeout(type, speed);
            }
        }
        
        type();
    }

    // Smooth scroll pour les liens d'ancrage
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Lazy loading pour les images (si présentes)
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    imageObserver.unobserve(img);
                }
            });
        });

        document.querySelectorAll('img[data-src]').forEach(img => {
            imageObserver.observe(img);
        });
    }
});