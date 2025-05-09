document.addEventListener('DOMContentLoaded', function() {
	
	const sliderItems = document.querySelectorAll('.slider__item');
	
	sliderItems.forEach(item => {
	  item.addEventListener('click', function() {
		// Удаляем классы active у всех элементов
		document.querySelectorAll('.slider__item.active').forEach(activeItem => {
		  activeItem.classList.remove('active');
		});
		document.querySelectorAll('.slider__title.active').forEach(activeTitle => {
		  activeTitle.classList.remove('active');
		});
		
		// Добавляем класс active текущему элементу и его заголовку
		this.classList.add('active');
		this.querySelector('.slider__title').classList.add('active');
	  });
	});
  });

document.querySelectorAll('.slider__item').forEach(item => {
    item.addEventListener('click', function(e) {
        e.preventDefault();

        if (this.classList.contains('active')) {
            window.location.href = this.getAttribute('href');
        }
    });
	const items = document.querySelectorAll('.feedbacks__item');
	let currentIndex = 0;

	function showNextItem() {
		// Убираем активный
		items[currentIndex].classList.remove('active');

		// Устанавливаем следующий индекс
		currentIndex = (currentIndex + 1) % items.length;

		// Добавляем активный
		items[currentIndex].classList.add('active');
	}

	setInterval(showNextItem, 5000); // каждые 5 секунд


	//player
	// var playerElement = document.getElementById('player');
    // var videoUrl = playerElement.dataset.videoUrl;  // Считываем URL видео из data-атрибута

    // if (videoUrl) {
    //     let player = new Playerjs({
    //         id: "player",  // id элемента
    //         file: videoUrl,
	// 		mute: 1
    //     });
    // } else {
    //     console.error("Видео не найдено!");
    // }
	

	const playerContainer = document.getElementById("playerInfo");

    if (playerContainer) {
        const videoUrl = playerContainer.dataset.videoUrl;
		const poster = playerContainer.dataset.poster;

        if (videoUrl) {
            const player = new Playerjs({
                id: "playerInfo",
                file: videoUrl,
				mute: 0,
				poster: poster
            });
        } else {
            console.warn("Видео не найдено в data-video-url");
        }
    }
});


