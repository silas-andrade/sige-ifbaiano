let cart = []

  function addToCart(id, name, stock) {
    stock = parseInt(stock)
    const existing = cart.find(i => i.id === id)

    if (existing) {
      if (existing.quantity < stock) existing.quantity++
    } else {
      cart.push({ id, name, quantity: 1 })
    }

    renderCart()
    updateHiddenInputs()
  }

  function removeFromCart(id) {
    cart = cart.filter(i => i.id !== id)
    renderCart()
    updateHiddenInputs()
  }

  function renderCart() {
    const el = document.getElementById('cart-items')
    const badge = document.getElementById('cart-count-badge')

    const total = cart.reduce((a, i) => a + i.quantity, 0)

    if (total > 0) {
      badge.textContent = total
      badge.classList.remove('hidden')
    } else {
      badge.classList.add('hidden')
    }

    if (!cart.length) {
      el.innerHTML = '<p>Seu carrinho está vazio.</p>'
      return
    }

    el.innerHTML = cart.map(item => `
      <div class="flex justify-between items-center mb-2">
        <span>${item.name} (x${item.quantity})</span>
        <button onclick="removeFromCart('${item.id}')" class="text-red-600">
          <i class="fa-solid fa-trash"></i>
        </button>
      </div>
    `).join('')
  }

  function updateHiddenInputs() {
    const container = document.getElementById('cart-hidden-inputs')
    container.innerHTML = ''
    cart.forEach(item => {
      container.innerHTML += `
        <input type="hidden" name="items[]" value="${item.id}:${item.quantity}">
      `
    })
  }