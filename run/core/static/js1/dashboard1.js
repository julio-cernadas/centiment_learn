 $(document).ready(function () {
     // toat popup js
     $.toast({
         heading: 'Welcome to Byte Tweeter',
         text: 'Remember: Tweet Wisely!',
         position: 'top-right',
         loaderBg: '#398fe5',
         icon: 'icon',
         hideAfter: 3000,
         stack: 1
     })

     // counter
     $(".counter").counterUp({
         delay: 100,
         time: 900
     });

     var sparklineLogin = function () {
         $('#sparklinedash').sparkline([6, 8, 7, 10, 8, 10, 9, 11], {
             type: 'bar',
             height: '30',
             barWidth: '4',
             resize: true,
             barSpacing: '5',
             barColor: '#008738'
         });
         $('#sparklinedash2').sparkline([6, 8, 7, 10, 8, 10, 9, 11], {
             type: 'bar',
             height: '30',
             barWidth: '4',
             resize: true,
             barSpacing: '5',
             barColor: '#008738'
         });
         $('#sparklinedash3').sparkline([6, 8, 7, 10, 8, 10, 9, 11], {
             type: 'bar',
             height: '30',
             barWidth: '4',
             resize: true,
             barSpacing: '5',
             barColor: '#008738'
         });
         $('#sparklinedash4').sparkline([11, 9, 10, 8, 10, 7, 8, 6], {
             type: 'bar',
             height: '30',
             barWidth: '4',
             resize: true,
             barSpacing: '5',
             barColor: '#ff1e1e'
         });
         $('#sparklinedash5').sparkline([6, 8, 7, 10, 8, 10, 9, 11], {
             type: 'bar',
             height: '30',
             barWidth: '4',
             resize: true,
             barSpacing: '5',
             barColor: '#008738'
         });
     }
     var sparkResize;
     $(window).on("resize", function (e) {
         clearTimeout(sparkResize);
         sparkResize = setTimeout(sparklineLogin, 500);
     });
     sparklineLogin();
 });
