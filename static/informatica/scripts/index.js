$(document).ready(() => {
	/*
	 * CONFIG DOS SLIDERS  #####################################
	 */
	const homeCarousel = new Swiper('.home-carousel', {
		direction: 'horizontal',
		loop: true,
		spaceBetween: -1,
		speed: 500,

		// autoplay: {
		//   delay: 3500,
		//   disableOnInteraction: false
		// },

		pagination: {
			el: '.swiper-pagination',
			clickable: true
		},

		navigation: {
			nextEl: '.swiper-button-next',
			prevEl: '.swiper-button-prev',
		},
	});
	const newsCarousel = new Swiper('.news-carousel', {
		direction: 'horizontal',
		loop: false,
		slidesPerView: "auto",
		spaceBetween: 32,
		hashNavigation: {
			watchState: true,
		},

		navigation: {
			nextEl: '.swiper-button-next',
			prevEl: '.swiper-button-prev',
		},
	});
});
