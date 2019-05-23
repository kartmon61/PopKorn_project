$(document).ready( function() {
    //header, footer include
    $("header").load("header.html");
    $("footer").load("footer.html");

    /*/배너 누르면 이동 
    $(".fotorama").on("click",function(){
        var href= $(this).find("a").attr('href');
        location.href=href;
    });
    */
    });