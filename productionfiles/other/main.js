    //global javascript for scroll animations(service, projects,contact,about pages)
    const sr = ScrollReveal(
        {
            distance: '60px',
            duration: 1500,
            delay: 300,
            reset: true
        }
    )
    sr.reveal('.services h2', {delay:100, origin: 'top'})
    sr.reveal('.clientarea-text', {delay:100, origin: 'top'})
    sr.reveal('.ourteam-card', {delay:100, origin: 'top'})
    sr.reveal('.ourteam h2', {delay:100, origin: 'top'})
    sr.reveal('.aboutus h2', {delay:50, origin: 'top'})
    sr.reveal('.about-container-1 h2, .about-container-2 h2, .about-container-4 h2,.about-container-5 h2', {delay:100, origin: 'top'})
    sr.reveal('.contact-container .cols-1 h2', {delay:50, origin: 'top'})
    sr.reveal('.contact-container .cols-2 h3, .def h2, .t-services h2, .whyus h2', {delay:50, origin: 'top'})
    sr.reveal('.about-container-3 .column-1, .about-container-3 .column-2, .about-container-3 .column-3', {delay:100, origin: 'bottom'})
    sr.reveal('.about-container-4 .column-2 ul li, .about-container-5 .column-2 img, .whyus .whyus-card', {delay:100, origin: 'bottom'})
    sr.reveal('.about-container-5 .column-1 ul li, .about-container-2 .column-2 .text .card-r', {delay:100, origin: 'bottom'})
   