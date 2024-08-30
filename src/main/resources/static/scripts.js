function updateLayout() {
    const isMobile = window.innerWidth <= 768;

    if (isMobile) {
        document.querySelector('.mobile').style.display = 'block';
        document.querySelector('.desktop').style.display = 'none';
    } else {
        document.querySelector('.mobile').style.display = 'none';
        document.querySelector('.desktop').style.display = 'block';
    }
}

document.addEventListener('DOMContentLoaded', function() {
    updateLayout();
    window.addEventListener('resize', updateLayout);
});
