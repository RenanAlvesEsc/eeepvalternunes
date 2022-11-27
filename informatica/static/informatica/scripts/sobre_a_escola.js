$(document).ready(() => {
    /*
	 * CONFIG DOS SLIDERS  #####################################
	 */
    const photoSlider = new Swiper('.photo-slider', {
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
  