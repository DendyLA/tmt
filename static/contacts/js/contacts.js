document.addEventListener("DOMContentLoaded", function () {
  const inputDisplay = document.querySelector("#id_phone_display");
  const hiddenInput = document.querySelector("#id_phone");
  const form = document.querySelector(".contact-form");
  const popup = document.querySelector(".form__popup");
  const popupClose = document.querySelector(".form__popupClose");

  const iti = window.intlTelInput(inputDisplay, {
      initialCountry: "tm",
      separateDialCode: true,
      nationalMode: false,
      utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js"
  });

  form.addEventListener("submit", function (e) {
      e.preventDefault(); // Отменяем стандартное поведение формы (перезагрузку страницы)

      // Получаем код страны из DOM
      const dialCodeElement = document.querySelector(".iti__selected-dial-code");
      const dialCode = dialCodeElement ? dialCodeElement.textContent.trim() : "";

      // Получаем номер, введённый пользователем
      const localNumber = inputDisplay.value.trim();

      // Склеиваем
      const fullNumber = `${dialCode}${localNumber}`;

      // Подставляем в скрытый input
      hiddenInput.value = fullNumber;
      console.log("📞 Отправляем:", fullNumber);

      // Показываем попап
      popup.classList.add("active");

      // Подготовим данные для отправки
      const formData = new FormData(form);

      // Отправляем данные через AJAX с использованием fetch
      fetch(form.action, {
          method: 'POST',
          body: formData,
      })
      .then(response => response.json())  // Преобразуем ответ в формат JSON
      .then(data => {
          console.log("Ответ от сервера:", data);
          form.reset(); // Очистка формы
          // Если сервер успешно обработал запрос, скрываем попап через 3 секунды
          setTimeout(function () {
              popup.classList.remove("active");
          }, 3000);
      })
      .catch(error => {
          console.error("Ошибка при отправке формы:", error);
      });
  });

  // Закрытие попапа при нажатии на кнопку закрытия
  popupClose.addEventListener("click", function () {
      popup.classList.remove("active");
  });

  // Закрытие попапа при клике вне form__popupWrapper
  popup.addEventListener("click", function (e) {
      if (!e.target.closest('.form__popupWrapper')) {
          popup.classList.remove("active");
      }
  });
});



let map = L.map('map').setView([37.959222, 58.421889], 16);

const customIcon = L.icon({
    iconUrl: '/static/contacts/img/marker.png', // путь до картинки
    iconSize: [40, 40],
    iconAnchor: [10, 30],
  });


  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; OpenStreetMap' // убираем ссылку/атрибуцию
  }).addTo(map);

  L.marker([37.959222, 58.421889], { icon: customIcon })
  .addTo(map)
  .bindPopup("<b>TMT Consulting Group</b>", {offset: L.point(5, -20)});
