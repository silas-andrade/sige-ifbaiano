document.addEventListener("DOMContentLoaded", function () {
    const passwordInput = document.getElementById("password");
    const toggleButton = document.getElementById("passwordToggle");

    toggleButton.addEventListener("click", function () {
        const isPassword = passwordInput.type === "password";

        passwordInput.type = isPassword ? "text" : "password";

        toggleButton.classList.toggle("show-password", isPassword);
    });
});


const input = document.getElementById("email");
const erro = document.getElementById("erro");

input.addEventListener("input", () => {
    if (emailValido(input.value)) {
        erro.textContent = "";
    } else {
        erro.textContent = "E-mail inválido";
    }
});
