
window.replainSettings = { id: '328a1019-cf35-433c-b4f4-0555e0667585' };
(function(u){var s=document.createElement('script');s.async=true;s.src=u;
var x=document.getElementsByTagName('script')[0];x.parentNode.insertBefore(s,x);
})('https://widget.replain.cc/dist/client.js');

new WOW().init(
  {
    offset: 10,
  }

);
AOS.init();


$(document).ready(function(){

  $('.customer-logos').slick({
      slidesToShow: 4,
      slidesToScroll: 1,
      autoplay: true,
      autoplaySpeed: 3500,
      arrows: false,
      dots: false,
      pauseOnHover: false,
      responsive: [
        {
          breakpoint: 1024,
          settings: {
              slidesToShow: 3
          }
      },{
          breakpoint: 768,
          settings: {
              slidesToShow: 2
          }
      }, {
          breakpoint: 520,
          settings: {
              slidesToShow: 1
          }
      }]
  });
  
  });




  // Crol to top
  var $btnTop = $(".btn-top");
  $(window).on("scroll",function(){
    if($(window).scrollTop() >= 20)
    {
      $btnTop.fadeIn();
    }
    else{
      $btnTop.fadeOut();
    }
  });
  $btnTop.on("click",function(){
    $("html,body").animate({scrollTop:0},1200)
  });



  $(document).ready(function(){
    // invoke the carousel
        $('#myCarousel').carousel({
          interval:6000
        });
    
    // scroll slides on mouse scroll 
    $('#myCarousel').bind('mousewheel DOMMouseScroll', function(e){
    
            if(e.originalEvent.wheelDelta > 0 || e.originalEvent.detail < 0) {
                $(this).carousel('prev');
          
          
            }
            else{
                $(this).carousel('next');
          
            }
        });
    
    //scroll slides on swipe for touch enabled devices     
       $("#myCarousel").on("touchstart", function(event){
     
            var yClick = event.originalEvent.touches[0].pageY;
          $(this).one("touchmove", function(event){
    
            var yMove = event.originalEvent.touches[0].pageY;
            if( Math.floor(yClick - yMove) > 1 ){
                $(".carousel").carousel('next');
            }
            else if( Math.floor(yClick - yMove) < -1 ){
                $(".carousel").carousel('prev');
            }
        });
        $(".carousel").on("touchend", function(){
                $(this).off("touchmove");
        });
    });
        
    });

    