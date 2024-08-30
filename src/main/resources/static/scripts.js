function updateLayout() {
    const isMobile =
        /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) ;

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
