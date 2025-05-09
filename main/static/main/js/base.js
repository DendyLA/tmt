AOS.init({
    once: true,
});

document.querySelector('.hamburger').addEventListener('click', function () {
    this.classList.toggle('is-active');
    
    nav = document.querySelector('.nav')
    if(nav.classList.contains('nav__active') === true){
        nav.classList.remove('nav__active')
    }else{
        nav.classList.add('nav__active')
    }
});


document.querySelector('.sub__form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const form = e.target;
    const response = await fetch(form.action, {
        method: 'POST',
        headers: { 'X-Requested-With': 'XMLHttpRequest' },
        body: new FormData(form)
    });
    const result = await response.json();
    const messageBox = document.querySelector('.footer__messages');

    // Показываем плашку
    messageBox.classList.add('active');

    // Через 3 секунды убираем плашку (если не нажал крестик)
    const timeout = setTimeout(() => {
        messageBox.classList.remove('active');
    }, 3000);

    // Если нажал на крестик — убрать плашку и очистить таймер
    const exitBtn = messageBox.querySelector('.footer__exit');
    exitBtn.addEventListener('click', () => {
        messageBox.classList.remove('active');
        clearTimeout(timeout);
    });

    messageBox.addEventListener('click', (e) => {
        if (e.target === messageBox){
            messageBox.classList.remove('active');
            clearTimeout(timeout);
        }

    });
});



const header = document.querySelector('.header');
const placeholder = document.querySelector('.header__placeholder');
let isFixed = false;

function setPlaceholderHeight() {
    const headerHeight = header.offsetHeight;
    placeholder.style.height = isFixed ? `${headerHeight}px` : '0';
}

window.addEventListener('scroll', () => {
    const scrollY = window.scrollY;

    if (scrollY > 700 && !isFixed) {
        header.classList.add('header--fixed');
        isFixed = true;
        setPlaceholderHeight();
    } else if (scrollY <= 700 && isFixed) {
        header.classList.remove('header--fixed');
        isFixed = false;
        setPlaceholderHeight();
    }
});

window.addEventListener('resize', setPlaceholderHeight);
window.addEventListener('load', setPlaceholderHeight);


