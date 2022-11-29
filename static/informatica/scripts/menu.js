$(document).ready(() => {
    
    window.onscroll = () => {
        changeNavbarBg()
    }

    let navBar = $("#nav-bar");
    let body = $('body');
    let docEl = $(document.documentElement);
    let distanceFromTop = 1;


    function changeNavbarBg() {
        if (docEl.scrollTop() > distanceFromTop
            || body.scrollTop() > distanceFromTop) {
            navBar.addClass('scrolled-down');
        }
        else {
            navBar.removeClass('scrolled-down');
        }
    }

    $('.menu').on("click", function() {
        $('.nav-list').toggleClass('opened');
    })

});