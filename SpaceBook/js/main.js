async function buscarLivros() {
    const titulo = document.querySelector('input[type="text"]').value;
    const genero = document.querySelector('select').value;
  
    const url = new URL('http://localhost:5000/api/books/');
  
    if (titulo) url.searchParams.append('titulo', titulo);
    if (genero && genero !== "Todos os gêneros") {
      url.searchParams.append('genero', genero);
    }
  
    try {
      const response = await fetch(url);
      const livros = await response.json();
      renderizarLivros(livros);
    } catch (error) {
      console.error("Erro ao buscar livros:", error);
    }
  }
  document.addEventListener('DOMContentLoaded', () => {
    const loginBtn = document.querySelector('.login-btn');
    if (loginBtn) {
      loginBtn.addEventListener('click', () => {
        // ação do botão
      });
    }
  });
   
  function renderizarLivros(livros) {
    const container = document.getElementById('book-container');
    container.innerHTML = '';
  
    livros.forEach(livro => {
      const card = document.createElement('div');
      card.className = 'book';
  
      card.innerHTML = `
        <img src="https://via.placeholder.com/150x200?text=Livro" />
        <div class="book-title">${livro.titulo}</div>
        <p><strong>Autor:</strong> ${livro.autor}</p>
        <p><strong>Gênero:</strong> ${livro.genero}</p>
        <p><strong>Ano:</strong> ${livro.ano}</p>
        <p><strong>Nota:</strong> ⭐ ${livro.nota ?? "Sem nota"}</p>
      `;
  
      container.appendChild(card);
    });
  }
  
  // Eventos
  document.querySelector('.search-bar button').addEventListener('click', buscarLivros);
  document.addEventListener('DOMContentLoaded', buscarLivros);
  