
// Carousel Initializing

 
const swiper = new Swiper('.swiper', {
    spaceBetween: 30,
    centeredSlides: true,      
    // Optional parameters
    loop: true,
    
    autoplay: {
        delay: 3500,
        disableOnInteraction: false,
    },
    // If we need pagination
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
  
    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  
    // And if we need scrollbar
    scrollbar: {
      el: '.swiper-scrollbar',
    },
  });
