document.addEventListener('DOMContentLoaded', function () {
    $("#sleep").click(function(){
        $('.overview').fadeToggle(100);
        $('#loading-overlay').fadeToggle(100);
        window.location.href = '/some/new/page';
        return false;
    });
});
