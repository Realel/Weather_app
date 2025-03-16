document.addEventListener("DOMContentLoaded", function () {
    const themeToggle = document.getElementById("theme-toggle");
    const body = document.body;

    // Проверяем, есть ли сохранённая тема в localStorage
    if (localStorage.getItem("theme") === "dark") {
        body.classList.add("dark");
        themeToggle.textContent = "🌙";
    }

    themeToggle.addEventListener("click", function () {
        body.classList.toggle("dark");

        // Сохраняем состояние темы
        if (body.classList.contains("dark")) {
            localStorage.setItem("theme", "dark");
            themeToggle.textContent = "🌙";
        } else {
            localStorage.setItem("theme", "light");
            themeToggle.textContent = "🌞";
        }
    });
});
document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("weather-form");
    const loading = document.getElementById("loading");
    const weatherContainer = document.getElementById("weather-container");

    form.addEventListener("submit", function () {
        loading.style.display = "block"; // Показываем индикатор загрузки
        weatherContainer.style.opacity = "0"; // Прячем контейнер
        weatherContainer.style.transform = "scale(0.8)"; // Уменьшаем перед анимацией
    });

    // Ждем появления контейнера после загрузки страницы
    setTimeout(() => {
        weatherContainer.style.opacity = "1";
        weatherContainer.style.transform = "scale(1)";
    }, 500);
});
