// --- Simulação de Usuário Logado (Vindo do Login) ---
const loggedUser = {
    name: "Ana Pereira",
    matricula: "2024.10.05 - Turma 3B"
};

// --- Dados Iniciais (Simulando Banco de Dados) ---
const initialInventory = [
    { id: 1, name: "Caneta Azul", quantity: 50, unit: "un", icon: "fa-pen", category: "Papelaria" },
    { id: 2, name: "Caneta Vermelha", quantity: 30, unit: "un", icon: "fa-pen", category: "Papelaria" },
    { id: 3, name: "Bloco de Notas", quantity: 15, unit: "un", icon: "fa-note-sticky", category: "Papelaria" },
    { id: 4, name: "Papel A4 (Pacote)", quantity: 10, unit: "pct", icon: "fa-copy", category: "Papelaria" },
    { id: 5, name: "Cabo HDMI", quantity: 5, unit: "un", icon: "fa-plug", category: "Eletrônicos" },
    { id: 6, name: "Marcador de Quadro", quantity: 12, unit: "un", icon: "fa-pen-to-square", category: "Sala de Aula" },
    { id: 7, name: "Apagador", quantity: 8, unit: "un", icon: "fa-eraser", category: "Sala de Aula" },
    { id: 8, name: "Grampeador", quantity: 3, unit: "un", icon: "fa-stapler", category: "Escritório" },
    { id: 9, name: "Clips (Caixa)", quantity: 20, unit: "cx", icon: "fa-paperclip", category: "Escritório" },
];

// Estado da Aplicação
let inventory = JSON.parse(JSON.stringify(initialInventory)); // Cópia profunda
let cart = [];

// --- Funções de Renderização ---

function renderInventory(items = inventory) {
    const grid = document.getElementById('inventory-grid');
    grid.innerHTML = '';

    if (items.length === 0) {
        grid.innerHTML = '<div class="col-span-full text-center py-10 text-gray-500">Nenhum item encontrado.</div>';
        return;
    }

    items.forEach(item => {
        // Determinar cor baseada na disponibilidade
        const stockColor = item.quantity === 0 ? 'text-red-500' : (item.quantity < 5 ? 'text-orange-500' : 'text-green-600');
        const isOutOfStock = item.quantity === 0;

        const card = document.createElement('div');
        card.className = `bg-white p-4 rounded-lg shadow border-l-4 ${isOutOfStock ? 'border-red-400 opacity-75' : 'border-blue-500'} hover:shadow-md transition duration-200 fade-in`;

        card.innerHTML = `
                    <div class="flex justify-between items-start mb-3">
                        <div class="bg-gray-100 p-3 rounded-full">
                            <i class="fa-solid ${item.icon} text-xl text-gray-600"></i>
                        </div>
                        <span class="text-xs font-bold uppercase tracking-wide text-gray-400">${item.category}</span>
                    </div>
                    <h3 class="font-bold text-lg text-gray-800 mb-1">${item.name}</h3>
                    <p class="text-sm font-medium ${stockColor} mb-4">
                        <i class="fa-solid fa-box-open mr-1"></i> 
                        ${isOutOfStock ? 'Esgotado' : `${item.quantity} ${item.unit} disponíveis`}
                    </p>
                    
                    <div class="flex items-center gap-2 mt-auto">
                        <input type="number" id="qty-${item.id}" min="1" max="${item.quantity}" value="1" 
                            class="w-16 border rounded p-1 text-center focus:ring-blue-500 focus:border-blue-500 ${isOutOfStock ? 'bg-gray-100 text-gray-400' : ''}" 
                            ${isOutOfStock ? 'disabled' : ''}>
                        <button onclick="addToCart(${item.id})" 
                            class="flex-1 ${isOutOfStock ? 'bg-gray-300 cursor-not-allowed' : 'bg-blue-600 hover:bg-blue-700'} text-white py-1.5 px-3 rounded text-sm font-medium transition"
                            ${isOutOfStock ? 'disabled' : ''}>
                            Adicionar
                        </button>
                    </div>
                `;
        grid.appendChild(card);
    });
}

function renderCart() {
    const container = document.getElementById('cart-items');
    const counter = document.getElementById('cart-counter');

    container.innerHTML = '';

    if (cart.length === 0) {
        container.innerHTML = '<p class="text-gray-400 text-center italic mt-4"><i class="fa-solid fa-basket-shopping text-4xl mb-2 block opacity-20"></i>Seu carrinho está vazio.</p>';
        counter.classList.add('hidden');
        return;
    }

    counter.innerText = cart.length;
    counter.classList.remove('hidden');

    cart.forEach((item, index) => {
        const row = document.createElement('div');
        row.className = 'flex justify-between items-center bg-white p-3 rounded border border-gray-100 shadow-sm fade-in';
        row.innerHTML = `
                    <div>
                        <p class="font-semibold text-gray-800 text-sm">${item.name}</p>
                        <p class="text-xs text-gray-500">Qtd: <span class="font-bold text-blue-600">${item.requestedQty}</span> ${item.unit}</p>
                    </div>
                    <button onclick="removeFromCart(${index})" class="text-red-400 hover:text-red-600 p-1 transition" title="Remover">
                        <i class="fa-solid fa-trash"></i>
                    </button>
                `;
        container.appendChild(row);
    });
}

// --- Lógica de Negócios ---

function addToCart(id) {
    const itemIndex = inventory.findIndex(i => i.id === id);
    const item = inventory[itemIndex];
    const inputEl = document.getElementById(`qty-${id}`);
    const qty = parseInt(inputEl.value);

    // Validações
    if (isNaN(qty) || qty <= 0) {
        showToast("Por favor, insira uma quantidade válida.", "error");
        return;
    }
    if (qty > item.quantity) {
        showToast(`Desculpe, só temos ${item.quantity} unidades disponíveis.`, "error");
        return;
    }

    // Verificar se já está no carrinho
    const existingInCart = cart.findIndex(c => c.id === id);

    if (existingInCart !== -1) {
        // Atualizar quantidade no carrinho
        const newTotal = cart[existingInCart].requestedQty + qty;
        if (newTotal > (item.quantity + cart[existingInCart].requestedQty)) {
            // Nota: A lógica aqui simplificada assume que item.quantity no array inventory é o que SOBROU. 
            // Mas para simplificar a UI, vamos decrementar do estoque visual.
            showToast("Quantidade total excede o estoque.", "error");
            return;
        }
        cart[existingInCart].requestedQty += qty;
    } else {
        // Adicionar novo
        cart.push({ ...item, requestedQty: qty });
    }

    // Atualizar estoque localmente
    item.quantity -= qty;
    inputEl.value = 1; // Resetar input

    renderInventory(filterItemsLogic()); // Re-renderizar mantendo filtro
    renderCart();
    showToast(`${qty}x ${item.name} adicionado!`, "success");
}

function removeFromCart(index) {
    const cartItem = cart[index];
    const inventoryItem = inventory.find(i => i.id === cartItem.id);

    // Devolver ao estoque
    inventoryItem.quantity += cartItem.requestedQty;

    // Remover do carrinho
    cart.splice(index, 1);

    renderInventory(filterItemsLogic());
    renderCart();
    showToast("Item removido do pedido.", "info");
}

function filterItems() {
    renderInventory(filterItemsLogic());
}

function filterItemsLogic() {
    const term = document.getElementById('searchInput').value.toLowerCase();
    return inventory.filter(item => item.name.toLowerCase().includes(term));
}

function scrollToCart() {
    document.getElementById('cart-panel').scrollIntoView({ behavior: 'smooth' });
}

function finalizeRequest() {
    // Removida validação de inputs manuais, usa dados do loggedUser
    if (cart.length === 0) {
        showToast("Seu carrinho está vazio.", "error");
        return;
    }

    // Aqui você enviaria os dados para um backend (Firebase, SQL, Planilha Google, etc.)
    console.log("Enviando pedido:", {
        user: loggedUser.name,
        uid: loggedUser.matricula,
        items: cart
    });

    // Mostrar modal de sucesso
    document.getElementById('successModal').classList.remove('hidden');
    document.getElementById('successModal').classList.add('flex');
}

function closeModal() {
    // Resetar aplicação
    document.getElementById('successModal').classList.add('hidden');
    document.getElementById('successModal').classList.remove('flex');

    cart = [];
    // Não limpamos usuário, pois ele continua logado
    // Nota: Em um app real, recarregaríamos os dados do servidor.
    // Aqui, mantemos o estoque reduzido para simular que foi pego.
    renderCart();
    renderInventory();
}

// --- UI Utilities ---

function showToast(message, type = "info") {
    const toast = document.getElementById('toast');
    const msgEl = document.getElementById('toast-message');

    msgEl.innerText = message;

    // Cores do Toast
    toast.className = `fixed bottom-4 right-4 px-6 py-3 rounded shadow-lg transform transition-all duration-300 z-50 flex items-center translate-y-0 opacity-100 ${type === 'error' ? 'bg-red-600 text-white' :
            type === 'success' ? 'bg-green-600 text-white' :
                'bg-gray-800 text-white'
        }`;

    setTimeout(() => {
        toast.classList.add('translate-y-20', 'opacity-0');
    }, 3000);
}

// Inicialização
document.addEventListener('DOMContentLoaded', () => {
    // Exibir dados do usuário logado
    document.getElementById('user-display-name').innerText = loggedUser.name;
    document.getElementById('user-display-id').innerText = loggedUser.matricula;

    renderInventory();
});