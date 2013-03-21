$(function(){
	layout_trix();
});


function layout_trix(){
	$('#v-wrap').css('height',$(window).height()-40);
	$('#v-wrap').hide().delay(100).fadeIn();
}
