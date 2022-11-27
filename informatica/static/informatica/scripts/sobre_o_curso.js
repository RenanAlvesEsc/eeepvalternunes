$(document).ready(() => {
	/*
	 * CONFIG DO SLIDER  #####################################
	 */
	const eventsCarousel = new Swiper('.events-index', {
		direction: 'horizontal',
		loop: false,

		pagination: {
			el: '.swiper-pagination',
			clickable: true
		},

		navigation: {
			nextEl: '.swiper-button-next',
			prevEl: '.swiper-button-prev',
		},
	});
})

