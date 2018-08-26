$(document).ready(function () {
    $(".tst1").on("click", function () {
        $.toast({
            heading: 'Welcome to Capitalism',
            text: 'Remember: Greed is Good!',
            position: 'top-right',
            loaderBg: '#10B802',
            icon: 'info',
            hideAfter: 3000,
            stack: 1
        });

    });

});
