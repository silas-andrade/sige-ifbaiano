let emailVisible = false
    let passwordVisible = false
    
    function toggleEmail() {
      const field = document.getElementById('emailField')
      const icon = document.getElementById('emailIcon')
    
      emailVisible = !emailVisible
    
      if (emailVisible) {
        field.style.filter = 'none'
        icon.classList.replace('fa-eye', 'fa-eye-slash')
      } else {
        field.style.filter = 'blur(4px)'
        icon.classList.replace('fa-eye-slash', 'fa-eye')
      }
    }
    
    function togglePassword() {
      const field = document.getElementById('passwordField')
      const icon = document.getElementById('passwordIcon')
    
      passwordVisible = !passwordVisible
    
      if (passwordVisible) {
        field.textContent = 'Senha protegida (não exibida)'
        field.style.filter = 'none'
        icon.classList.replace('fa-eye', 'fa-eye-slash')
      } else {
        field.textContent = '**************'
        field.style.filter = 'blur(4px)'
        icon.classList.replace('fa-eye-slash', 'fa-eye')
      }
    }