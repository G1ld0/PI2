// catalogo.js

function filterBooks() {
    const searchInput = document.getElementById('search').value.toLowerCase();
    const bookGrid = document.getElementById('book-grid');
    const books = bookGrid.getElementsByClassName('grid-item');

    // Verifica se o campo de busca está vazio
    if (searchInput.trim() === '') {
        // Se estiver vazio, exibe todos os livros
        for (let i = 0; i < books.length; i++) {
            books[i].style.display = '';
        }
        return; // Sai da função
    }

    // Filtra os livros com base no título
    for (let i = 0; i < books.length; i++) {
        const title = books[i].getElementsByTagName('h2')[0].innerText.toLowerCase();
        if (title.includes(searchInput)) {
            books[i].style.display = '';
        } else {
            books[i].style.display = 'none';
        }
    }
}

function sortBooks() {
    const bookGrid = document.getElementById('book-grid');
    const books = Array.from(bookGrid.getElementsByClassName('grid-item'));
    const sortValue = document.getElementById('sort').value;

    books.sort((a, b) => {
        if (sortValue === 'author') {
            const authorA = a.getAttribute('data-author').toLowerCase();
            const authorB = b.getAttribute('data-author').toLowerCase();
            return authorA.localeCompare(authorB);
        } else if (sortValue === 'date') {
            const dateA = new Date(a.getAttribute('data-date'));
            const dateB = new Date(b.getAttribute('data-date'));
            return dateA - dateB;
        }
        return 0; // Retorna 0 se não houver classificação
    });

    // Limpa o grid e adiciona os livros classificados de volta
    bookGrid.innerHTML = '';
    books.forEach(book => bookGrid.appendChild(book));
}