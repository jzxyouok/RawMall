var pageMarketIndex_wrapperScroller;


$(function() { 
    
     // pageMarketIndex_wrapperScroller = new IScroll('#pageMarketIndex_wrapper', { mouseWheel: true, click:true});
    
    //init FlexSlider
    $("#pageMarketIndex_wrapper>#scroller div.flexslider").flexslider({
        animation:'slide',
        directionNav:false
    }); 
    $('#pageMarketIndex_wrapper div.flexslider ol.flex-control-nav a').html('&nbsp;');
    

    
    // setTimeout(function(){
    //     pageMarketIndex_wrapperScroller.refresh();
    // }, 1000)
    
    FastClick.attach(document.body);

}); 
window.FastClick={
    attach:function(s){

    }
}

var myScroll;

function loaded () {
    myScroll = new IScroll('#wrapper', { scrollX: true, scrollY: false, mouseWheel: true });
}

document.addEventListener('touchmove', function (e) { e.preventDefault(); }, false);

$(function(){
    var pageHeader_menuScroll; 
    pageHeader_menuScroll = new IScroll('#pageHeader_wrapper div#menu', { mouseWheel: true,click:true});

$('#pageHeader_wrapper div.itemsAll').click(function(){
    $this=$(this);
if($this.hasClass('reserve')){//收起
    $this.removeClass('reserve');
    $('#pageHeader_wrapper div.itemsList').css('transform','translateY(-130%)').css('-webkit-transform','translateY(-130%)').find('div.list').addClass('zoomOut').removeClass('zoomIn'); ;
    $('#pageHeader_wrapper div.itemsSelectAll').css('opacity',0);
    $('#pageHeader_wrapper div.itemsSelect').css('opacity',1);
    $('#pageHeader_wrapper div.header').removeClass('all');
    $('.itemsListMask').hide();
}else{//展开
    $this.addClass('reserve');
    $('#pageHeader_wrapper div.itemsList').css('transform','translateY(0px)').css('-webkit-transform','translateY(0px)').find('div.list').each(function(){
        $(this).css('animation-delay',$(this).index()/14+'s').addClass('zoomIn').removeClass('zoomOut'); 
    });
    $('#pageHeader_wrapper div.itemsSelectAll').css('opacity',1);
    $('#pageHeader_wrapper div.itemsSelect').css('opacity',0); 
    $('#pageHeader_wrapper div.header').addClass('all');
    $('#pageHeader_wrapper div.itemsListMask').show().click(function(){
        $this.removeClass('reserve');
        $('#pageHeader_wrapper div.itemsList').css('transform','translateY(-130%)').css('-webkit-transform','translateY(-130%)').find('div.list').addClass('zoomOut').removeClass('zoomIn'); 
        $('#pageHeader_wrapper div.itemsSelectAll').css('opacity',0);
        $('#pageHeader_wrapper div.itemsSelect').css('opacity',1);
        $('#pageHeader_wrapper div.header').removeClass('all');
        $(this).hide();
    })
}
});
//展开个人中心菜单
$('#pageHeader_wrapper img.headerFace').click(function(){  
    $('#pageHeader_wrapper div#menu').css('transform','translateX(0px)').css('-webkit-transform','translateX(0px)');
    $('#pageHeader_wrapper div.clientCenterMask').show().click(function(){
        $('#pageHeader_wrapper div#menu').css('transform','translateX(-100%)').css('-webkit-transform','translateX(-100%)');
        $('#pageHeader_wrapper div.clientCenterMask').hide();
    })
});
FastClick.attach(document.body);

});