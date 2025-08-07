document.addEventListener('DOMContentLoaded', function() {
	const projectLink = document.querySelector('.about__navProject');
	const servicesLink = document.querySelector('.about__navServices');
	const projectsSection = document.querySelector('.projects');
	const servicesSection = document.querySelector('.services');

	projectLink.addEventListener('click', function(e) {
		e.preventDefault(); // отменяем переход по ссылке
		projectLink.classList.add('about__navActive');
		servicesLink.classList.remove('about__navActive');
		projectsSection.classList.add('active');
		servicesSection.classList.remove('active');
	});

	servicesLink.addEventListener('click', function(e) {
		e.preventDefault(); // отменяем переход по ссылке
		servicesLink.classList.add('about__navActive');
		projectLink.classList.remove('about__navActive');
		projectsSection.classList.remove('active');
		servicesSection.classList.add('active');
		
	});


	//services__popup
	const items = document.querySelectorAll('.services__item');

	items.forEach(item => {
	const popup = item.querySelector('.services__popup');
	const closeBtn = item.querySelector('.services__popupClose');
	const wrapper = item.querySelector('.services__popupWrapper');

	// Открыть popup при клике на itemWrapper
	item.querySelector('.services__itemWrapper').addEventListener('click', function () {
		// Закрыть все другие попапы
		document.querySelectorAll('.services__popup.active').forEach(p => {
		p.classList.remove('active');
		});

		popup.classList.add('active');
	});

	// Закрыть popup по нажатию на крестик
	closeBtn.addEventListener('click', function (e) {
		popup.classList.remove('active');
		e.stopPropagation();
	});

	// Закрыть popup по клику вне окна
	popup.addEventListener('click', function (e) {
		if (!wrapper.contains(e.target)) {
		popup.classList.remove('active');
		}
	});
	});
});